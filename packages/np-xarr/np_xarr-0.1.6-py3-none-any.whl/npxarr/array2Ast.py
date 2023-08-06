import ast  # type: ignore
from operator import add
from typing import *

from cytoolz import merge_with, itemmap, compose, reduce

from .definedTypes import Indice, Shape, InIndex, OutIndex, IndexMap, LabelInIndice
from .definedException import AstSyntaxError
from .utils import allSame


class Array2Ast(ast.NodeTransformer):
    def __init__(self, node: str):
        nodeAST = ast.parse(node)
        self.node = self.visit(nodeAST.body[0].value)
        self.shape = self.getShape()

    def getIndex(self) -> None:
        for elt in ast.walk(self.node):
            if isinstance(elt, ast.Name):
                name = elt.id
                indice = self.getIndice(elt)
                self.updateIndex(name, indice)

    def updateIndex(self, name: str, indice: Indice) -> None:
        raise NotImplementedError

    def getIndice(self, node: ast.AST) -> Indice:
        if hasattr(node, "index"):
            if hasattr(node, "parent"):
                return (*self.getIndice(node.parent), node.index)
            else:
                return node.index,
        else:
            return ()

    def getShape(self) -> Shape:
        def _getShape(outerShape: Shape, node) -> Sequence:
            if isinstance(node, ast.List):
                shapes = [
                    _getShape((*outerShape, node.length), elt)
                    for elt in ast.iter_child_nodes(node)
                    if not isinstance(elt, ast.Ellipsis)
                ]
                if allSame(shapes):
                    return shapes[0]
                else:
                    raise AstSyntaxError("Illegal array shape")
            else:
                return outerShape

        return _getShape((), self.node)

    @staticmethod
    def visit_Num(node: ast.Num) -> ast.Name:
        return ast.copy_location(ast.Name(id=str(node.n)), node)

    def visit_Attribute(self, node: ast.Attribute) -> ast.Name:
        return ast.copy_location(ast.Name(id=self.attribute2id(node)), node)

    def visit_Call(self, node: ast.Call) -> ast.Name:
        func = node.func.id
        if not isinstance(node.args[0], (ast.Name, ast.Num)):
            raise AstSyntaxError('Illegal arguments for function {}.'.format(func))
        param = self.visit(node.args[0])
        param.func = func
        return ast.copy_location(param, node)

    def visit_Starred(self, node: ast.Starred) -> ast.Name:
        param = node.value
        if not isinstance(param, (ast.Name, ast.Num)):
            raise Exception('Illegal unpacking item.')
        param = self.visit(param)
        param.starred = True
        return ast.copy_location(param, node)

    @staticmethod
    def attribute2id(node: Union[ast.Attribute, ast.Name]) -> str:
        def _attribute2id(node, attrs: Sequence[str]) -> Sequence[str]:
            if isinstance(node, ast.Attribute):
                return _attribute2id(node.value, (node.attr, *attrs))
            elif isinstance(node, ast.Name):
                return (node.id, *attrs)
            else:
                raise AstSyntaxError("Illegal input elements")

        return ".".join(_attribute2id(node, ()))

    def visit_List(self, node: ast.List) -> ast.List:
        newList = ast.List(elts=[])
        res = []
        for (i, elt) in enumerate(ast.iter_child_nodes(node)):
            if isinstance(elt, ast.Load):
                continue
            elt = self.visit(elt)
            elt.parent = newList
            elt.index = i
            res.append(elt)
        newList.elts = res
        newList.length = (
            -1 if (not newList.elts) or isinstance(newList.elts[-1], ast.Ellipsis) else len(newList.elts)
        )
        return ast.copy_location(newList, node)


class InArray2Ast(Array2Ast):
    def __init__(self, node: str):
        super().__init__(node)
        self.index: InIndex = {}
        self.getIndex()

    def updateIndex(self, name: str, indice: Indice) -> None:
        self.index.update({name: indice})


class OutArray2Ast(Array2Ast):
    def __init__(self, node: str):
        super().__init__(node)
        self.index: OutIndex = {}
        self.funcs: Dict[str, List[Indice]] = {}
        self.funcsIndex: Dict[str, IndexMap] = {}
        self.starred: List[Indice] = []
        self.starredIndex: IndexMap = {}
        self.getIndex()
        self.getFuncsIndex()
        self.getStarredIndex()

    def updateIndex(self, name: str, indice: Indice) -> None:
        self.index.update({indice: name})

    def getFuncsIndex(self):
        for elt in ast.walk(self.node):
            if isinstance(elt, ast.Name):
                indice = self.getIndice(elt)
                if hasattr(elt, "func"):
                    self.funcs = merge_with(
                        lambda x: reduce(add, x, []), self.funcs, {elt.func: [indice]}
                    )
        for key in self.funcs.keys():
            self.funcsIndex[key] = itemmap(
                lambda kv, key=key: (kv[0], (int(kv[0] in self.funcs[key]),)), self.index
            )

    def getStarredIndex(self):
        for elt in ast.walk(self.node):
            if isinstance(elt, ast.Name):
                indice = self.getIndice(elt)
                if hasattr(elt, "starred"):
                    self.starred.append(indice)
        self.starredIndex = itemmap(
            lambda kv: (kv[0], (int(kv[0] in self.starred),)), self.index
        )


class FakeInArray2Ast(InArray2Ast):
    def __init__(self):
        super().__init__('[]')
        self.shape = None

    def updateIndex(self, name: str, indice: Indice) -> None:
        super().updateIndex(name, indice)
        if self.shape is None:
            self.shape = tuple([-1] * len(indice))
        if len(self.shape) != len(indice):
            raise AstSyntaxError('Wrong input shape.')

    def getShape(self) -> Shape:
        return ()


class LabelOutArray2Ast(OutArray2Ast):
    def __init__(self, node: str):
        self.inAsts: Dict[int, InArray2Ast] = {}
        self.indexMap: Dict[Indice, LabelInIndice] = {}
        super().__init__(node)

    def getIndexMap(self) -> Dict[Indice, LabelInIndice]:
        return self.indexMap

    def getInAsts(self) -> List[InArray2Ast]:
        num = max(list(self.inAsts.keys()))
        return [self.inAsts.get(i, FakeInArray2Ast()) for i in range(num + 1)]

    def updateIndex(self, name: str, indice: Indice) -> None:
        self.index.update({indice: name})
        numInAst = ord(name[0]) - ord('a')
        indexInAst = tuple(map(lambda x: int(x), name[1:]))
        self.indexMap.update({indice: (numInAst, indexInAst)})
        if numInAst in self.inAsts:
            self.inAsts[numInAst].updateIndex(name, indexInAst)
        else:
            self.inAsts[numInAst] = FakeInArray2Ast()
            self.inAsts[numInAst].updateIndex(name, indexInAst)

#!/usr/bin/env python
# coding: utf-8
from typing import Union, Optional

from cytoolz.curried import valmap, groupby, compose, valfilter, identity, map, nth, reduce

from .array2Ast import InArray2Ast, OutArray2Ast, LabelOutArray2Ast
from .indexConverter import *
from .utils import *
from .definedException import AstSyntaxError, LinearError, TransformError


class X0:
    def __init__(
            self, inArrs: Union[List[str], str], outArr: Optional[str] = None, f: Dict[str, Callable] = {}, num: int = 0
    ) -> None:
        self.num = num
        self.f = f
        if outArr is not None:
            self.inAsts = [InArray2Ast(inArr) for inArr in inArrs]
            self.outAst = OutArray2Ast(outArr)
            self.indexMap = self.getIndexMap([inAST.index for inAST in self.inAsts], self.outAst.index)
        else:
            self.outAst = LabelOutArray2Ast(inArrs)
            self.inAsts = self.outAst.getInAsts()
            self.indexMap = self.outAst.getIndexMap()
        self.funcsMap = self.getFuncsMap(self.outAst.funcsIndex)
        self.starredMap = self.getStarredMap(self.outAst.starredIndex)
        self.indexConverters = self.getIndexConverters(self.indexMap)
        self.insDispatcher = self.getInsDispatcher(self.indexMap)
        self.converter = self.converterCreator(
            self.insDispatcher, self.indexConverters, self.funcsMap, self.starredMap, self.f
        )

    def __call__(
            self,
            inArrs: Sequence[np.ndarray],
            outShape: Shape = (-1,),
            extraShape: Shape = (0,),
            f: Dict[str, Callable] = {},
    ) -> np.ndarray:
        f2 = self.f if f == {} else f
        return self.converter(inArrs, outShape, extraShape, f2)

    def __repr__(self) -> str:
        if isinstance(self.insDispatcher, UnitIndexConverter):
            _repr = self.indexConverters[0].__repr__("y")
        else:
            _repr = "\n".join(
                [
                    repr(self.insDispatcher),
                    "[",
                    "\n".join(
                        [
                            "  in{}: {}".format(i, indexConverter.__repr__("y"))
                            for (i, indexConverter) in enumerate(self.indexConverters)
                        ]
                    ),
                    "]",
                ]
            )
        if self.funcsMap != {}:
            _repr += "\n"
            _repr += "\n".join(
                [
                    "funcs: [",
                    "\n".join(
                        [
                            "  {}: {}".format(func, indexConverter.__repr__(suf="1"))
                            for (func, indexConverter) in self.funcsMap.items()
                        ]
                    ),
                    "]",
                ]
            )

        if not isinstance(self.starredMap, UnitIndexConverter):
            _repr += "\n"
            _repr += "star: {}".format(self.starredMap.__repr__(suf="1"))
        return _repr.replace("\n\n", "\n")

    def getIndexMap(
            self, insIndex: List[InIndex], outIndex: OutIndex
    ) -> Dict[Indice, LabelInIndice]:
        labeledInsIndex = [
            valmap(lambda x, i=i: (i, x), inIndex)
            for (i, inIndex) in enumerate(insIndex)
        ]
        return valmap(self.getCorrespondIndex(labeledInsIndex), outIndex)

    @staticmethod
    def getCorrespondIndex(
            labeledInsIndex: List[Dict[str, LabelInIndice]]
    ) -> Callable[[str], LabelInIndice]:
        def _getCorrespondIndex(x: str) -> LabelInIndice:
            index = [
                indice
                for indice in map(
                    lambda labeledInIndex: labeledInIndex.get(x), labeledInsIndex
                )
                if indice is not None
            ]
            if len(index) > 1:
                raise AstSyntaxError("Name {} appears in multiple inputs.".format(x))
            elif len(index) == 0:
                raise AstSyntaxError("Name {} not found in inputs.".format(x))
            else:
                return index[0]

        return _getCorrespondIndex

    def getInsDispatcher(self, indexMap: Dict[Indice, LabelInIndice]) -> IndexConverter:
        return self.createIndexConverter(
            valmap(lambda x: (x[0],), indexMap), (len(self.inAsts),), self.outAst.shape, True
        )

    def getIndexConverters(
            self, indexMap: Dict[Indice, LabelInIndice]
    ) -> List[IndexConverter]:
        return [
            self.getIndexConverter(
                i,
                compose(
                    valmap(lambda v: v[1]),
                    valfilter(lambda v, i=i: v[0] == i),
                )(indexMap),
            )
            for i in range(len(self.inAsts))
        ]

    def getIndexConverter(self, i: int, indexMap: IndexMap, boole: bool = False) -> IndexConverter:
        indexMap = {k: v for (k, v) in sorted(indexMap.items(), key=lambda kv: kv[0])}
        inShape = self.inAsts[i].shape
        outShape = self.outAst.shape
        return self.createIndexConverter(indexMap, inShape, outShape, boole)

    def createIndexConverter(
            self, indexMap: IndexMap, inShape: Shape, outShape: Shape, boole: bool = False
    ) -> IndexConverter:
        if indexMap == {}:
            return NullIndexConverter()
        if boole and set(indexMap.values()) == {(0,)}:
            return UnitIndexConverter(len(self.outAst.shape), 1)
        try:
            indiceConverters = list(reduce(
                lambda ls, i: ls + [self.getIndiceConverter(valmap(lambda v, i=i: v[i], indexMap), ls, boole)],
                range(len(inShape)), [[(0, 0, 0, 1)] * len(outShape)]))[1:]
            if not indiceConverters:
                return ZeroIndexConverter()
            genCoeffs = lambda func, func0=identity: [func0([func(c) for c in l]) for l in indiceConverters]
            linearCoeffs = genCoeffs(nth(0))
            bs = genCoeffs(nth(1), sum)
            indexModCoeffs = genCoeffs(nth(2))
            indexModValues = genCoeffs(nth(3))
            if boole:
                return LinearIndiceConverter(linearCoeffs[0], bs[0], inShape[0], indexModCoeffs[0], indexModValues[0])
            else:
                return LinearIndexConverter(linearCoeffs, bs, inShape, indexModCoeffs, indexModValues)
        except LinearError:
            if all([s != -1 for s in outShape]):
                return FixIndexConverter(indexMap)
            else:
                raise TransformError("Fail to find a transform.")

    def getIndiceConverter(
            self, indiceMap: Dict[Indice, int], ls: List[List[Sequence[float]]], boole: bool = False
    ) -> List[Sequence[float]]:
        def _createIndiceConverter(
                innerIndiceMap: Dict[Indice, int], coeffs: List[Sequence[float]], oi: int,
                _ls: List[List[Sequence[float]]], _boole: bool = False
        ) -> List[Sequence[float]]:
            if list(innerIndiceMap.keys())[0] is ():
                return coeffs
            else:
                innerIndiceMapGroup: Dict[int, List[Tuple[Indice, int]]] = compose(
                    valmap(compose(
                        lambda v: sorted(v, key=lambda k: k[0]),
                        map(lambda l: (l[0][1:], l[1])))),
                    groupby(lambda kv: kv[0][0]))(innerIndiceMap.items())
                outArr = list(innerIndiceMapGroup.keys())
                inArr = list(valmap(lambda v: v[0][-1], innerIndiceMapGroup).values())
                coeff = self.getIndiceTransformCoeffs(outArr, inArr, oi, _ls, _boole)
                nextInnerIndiceMapGroup: Dict[int, Dict[Indice, int]] = valmap(dict, innerIndiceMapGroup)
                coeffsList = [
                    _createIndiceConverter(
                        self.applyIndiceTransform(nextInnerIndiceMap, key, coeff),
                        [*coeffs, coeff], oi + 1, _ls, _boole
                    )
                    for key, nextInnerIndiceMap in nextInnerIndiceMapGroup.items()
                ]
                if allSame(coeffsList):
                    return coeffsList[0]
                else:
                    raise LinearError

        return _createIndiceConverter(indiceMap, [], 0, ls, boole)

    def getIndiceTransformCoeffs(
            self, outArr: List[int], inArr: List[int], oi: int, ls: List[List[Sequence[float]]], boole: bool = False
    ) -> Sequence[float]:  # (a, b, c, d, modValue) for (floor(a*x)+b+floor(c*mod(x, modValue))+d)
        points = np.array([outArr, inArr]).T
        l = len(points)
        if l == 1:
            if boole:
                return 0, points[0][1], 0, 1
            else:
                if ls[-1][oi][0] == 0:
                    x, y = points[0]
                    return 1, y - x, 0, 1
                else:
                    return 0, 0, 0, 1
        diff = points[1:] - points[:-1]
        k = lambda p: p[1] / p[0]
        if all([k(diff[0]) == k(p) for p in diff]):
            x, y = points[0]
            return k(diff[0]), y - np.floor(x * k(diff[0])), 0, 1
        factors = [i for i in range(2, l - 1) if l % i == 0]
        for f in factors:
            period = np.split(np.vstack([diff, diff[f - 1]]), l / f)
            if all([np.array_equal(period[0], x) for x in period[1:]]):
                modValue = np.sum(np.array(period[0])[:, 0])
                break
        else:
            raise LinearError
        a, b = self.getIndiceTransformCoeffs(outArr[::f], inArr[::f], oi, ls)[:2]
        c, d = self.getIndiceTransformCoeffs(
            outArr[:f], np.array(inArr[:f]) - (np.floor(a * np.array(outArr[:f])) + b), oi, ls
        )[:2]
        return a, b + d, c, modValue

    def getFuncsMap(self, funcsIndex: Dict[str, IndexMap]) -> Dict[str, IndexConverter]:
        return valmap(lambda v: self.createIndexConverter(v, (2,), self.outAst.shape, True), funcsIndex)

    def getStarredMap(self, starredMap: IndexMap) -> IndexConverter:
        return self.createIndexConverter(starredMap, (2,), self.outAst.shape, True)

    def converterCreator(
            self,
            insDispatcher: IndexConverter,
            indexConverters: List[IndexConverter],
            funcsIndex: Dict[str, IndexConverter],
            starredIndex: IndexConverter,
            f: Dict[str, Callable] = {},
    ) -> ArrayConverter:
        def arrayCreator(
                inArrs: Sequence[np.ndarray],
                outShape: Shape = (-1,),
                extraShape: Shape = (0,),
                f2: Dict[str, Callable] = f,
        ) -> np.ndarray:
            if len(inArrs) != len(self.inAsts):
                raise ValueError("Wrong input arrays number. Expected {}, got {}.".format(len(self.inAsts), len(inArrs)))
            for i in range(len(inArrs)):
                if not self.validShape(inArrs[i].shape, self.inAsts[i].shape):
                    raise ValueError("Wrong shape of No.{} input array.".format(i))

            def indice2Arr(indice: Indice) -> Union[np.ndarray, float]:
                whichIn = insDispatcher(indice)[0]
                doFuncs: Dict[str, bool] = valmap(lambda v: bool(v(indice)[0]), funcsIndex)
                whichFunc = list(valfilter(identity, doFuncs).keys())
                if not whichFunc:
                    func = lambda x: x
                else:
                    if whichFunc[0] not in f2:
                        raise ValueError("No function called {}.".format(whichFunc[0]))
                    func = f2[whichFunc[0]]
                return func(
                    self.getInputElement(inArrs[whichIn], tuple(indexConverters2[whichIn](indice)))
                )

            outShape = self.getOutShape(inArrs, insDispatcher, indexConverters, outShape)
            outShape = self.mergeShape(outShape, extraShape)

            indexConverters2: List[IndexConverter] = [
                indexConverter.setModValues(inArr.shape)
                for (indexConverter, inArr) in zip(indexConverters, inArrs)
            ]

            if all([isinstance(indexConverter, FixIndexConverter) for indexConverter in indexConverters2]):
                eltsBlock = self.buildEltsBlock(indice2Arr, (), outShape, starredIndex)
                return np.array(eltsBlock)

            if not self.validShape(self.outAst.shape, outShape):
                raise ValueError("Wrong shape of No. {} output array.".format(self.num))

            eltsBlock = self.buildEltsBlock(indice2Arr, (), outShape, starredIndex)
            return np.array(eltsBlock)

        return arrayCreator

    @staticmethod
    def getInputElement(inArr, index):
        return inArr if index == () else inArr[index]

    @staticmethod
    def validShape(knownShape: Shape, givenShape: Shape) -> bool:
        if len(givenShape) > len(knownShape):
            return False
        return all(
            [
                True
                if (knownShape[i] == -1 or givenShape[i] == -1)
                else givenShape[i] == knownShape[i]
                for i in range(len(givenShape))
            ]
        )

    def buildEltsBlock(
            self, foo: Callable[[Indice], Any], innerShape: Shape, outerShape: Shape, starredIndex: IndexConverter
    ):
        if outerShape is ():
            return foo(innerShape)
        if len(outerShape) > 1:
            return [
                self.buildEltsBlock(foo, (*innerShape, i), outerShape[1:], starredIndex)
                for i in range(outerShape[0])
            ]
        else:
            if not any([starredIndex((*innerShape, i))[0] for i in range(outerShape[0])]):
                return [
                    self.buildEltsBlock(foo, (*innerShape, i), outerShape[1:], starredIndex)
                    for i in range(outerShape[0])
                ]
            else:
                res = []
                for i in range(outerShape[0]):
                    if starredIndex((*innerShape, i))[0]:
                        for t in self.buildEltsBlock(foo, (*innerShape, i), outerShape[1:], starredIndex):
                            res.append(t)
                    else:
                        res.append(self.buildEltsBlock(foo, (*innerShape, i), outerShape[1:], starredIndex))
                return res

    @staticmethod
    def applyIndiceTransform(
            IndiceMapGroup: Dict[Indice, int], key: int, coeff: Sequence[float]
    ) -> Dict[Indice, int]:
        a, b, c, d = coeff
        return valmap(
            lambda v: v - (np.floor(a * key) + b + np.floor(c * (key % d))),
            IndiceMapGroup,
        )

    def getOutShape(
            self,
            inArrs: Sequence[np.ndarray],
            insDispatcher: IndexConverter,
            indexConverters: List[IndexConverter],
            outShape: Shape,
    ) -> Shape:
        knownOutShape = self.outAst.shape
        if all([s != -1 for s in knownOutShape]):
            return knownOutShape
        outShape = tuple(
            [max(knownOutShape[i], outShape[i]) for i in range(len(outShape))]
            + list(knownOutShape[len(outShape):])
        )

        sts = [(indexConverter.setModValues(-1), [i - 1 for i in inArr.shape[:len(inAST.shape)]])
               for (indexConverter, inArr, inAST) in zip(indexConverters, inArrs, self.inAsts)]

        genStOut = lambda func: [func(i=i, s=s) for (i, s) in enumerate(outShape) if s != -1]
        b_ub = genStOut(lambda i, s: s - 1)
        bs = genStOut(lambda i, s: 0)
        As = genStOut(lambda i, s: [1 if i == j else 0 for j in range(len(outShape))])
        Cs = genStOut(lambda i, s: [0] * len(outShape))
        Ds = genStOut(lambda i, s: [1] * len(outShape))
        stOut = (LinearIndexConverter(As, bs, -1, Cs, Ds), b_ub)

        neededDimPos = [
            i for (i, s) in enumerate(outShape) if (not np.any([st[0].nthBound(i) for st in sts])) and (s == -1)
        ]
        if len(neededDimPos) > 1:
            raise ValueError("Length needed for dim {} of output array.".format(neededDimPos))

        innerPts = InnerPtsDeque()
        innerPts.append(InnerPts(tuple([0] * len(outShape))))
        boundaryPts = []

        def st(x):
            whichIn = insDispatcher(x)[0]
            stConverter, stUp = sts[whichIn]
            return np.all(np.array(stConverter(x)) <= np.array(stUp)) and \
                   np.all(np.array(stConverter(x)) >= 0) and \
                   np.all(np.array(stOut[0](x)) <= np.array(stOut[1])) and \
                   all([any([xi <= bdptsi for i, (xi, bdptsi) in enumerate(zip(x, bdpts)) if outShape[i] == -1]) for
                        bdpts in boundaryPts])

        while innerPts:
            pts = innerPts[0]
            isInner = False
            for npts in pts.nextPts():
                if (npts in innerPts) or (st(npts) and all([ppts in innerPts for ppts in npts.previousPts()])):
                    isInner = True
                    if npts not in innerPts:
                        innerPts.append(npts)
            innerPts.popleft()
            if not isInner:
                boundaryPts.append(pts)
        isValidBoundaryPts = lambda x: all(
            [True if outShape[i] == -1 else x.toShape()[i] == outShape[i] for i in range(len(outShape))])
        validBoundaryPts = list(filter(isValidBoundaryPts, boundaryPts))
        if len(validBoundaryPts) > 1:
            raise ValueError("Multiple output shape valid. Output shape needed for No.{} array.".format(self.num),
                            [pts.toShape() for pts in validBoundaryPts])
        shape = validBoundaryPts[0].toShape()
        if not all([True if outShape[i] == -1 else shape[i] == outShape[i] for i in range(len(outShape))]):
            raise ValueError("Wrong given output shape for No.{} array.".format(self.num))
        return shape

    @staticmethod
    def mergeShape(outShape: Shape, extraShape: Shape) -> Shape:
        return tuple(
            [outShape[i] + extraShape[i] if i < len(extraShape) else outShape[i] for i in range(len(outShape))])


class X:
    def __init__(
            self,
            inArrs: Union[List[str], str],
            outArrs: Optional[Union[List[str], str]] = None,
            f: Dict[str, Callable] = {},
            simpleParams=True
    ) -> None:
        self.inArrs = inArrs.replace(" ", "").split(";") if isinstance(inArrs, str) else inArrs
        self.f = f
        self.simpleParams = simpleParams
        if outArrs is not None:
            self.outArrs = outArrs.replace(" ", "").split(";") if isinstance(outArrs, str) else outArrs
            self.converters = [
                X0(self.inArrs, outArr, f, i) for (i, outArr) in enumerate(self.outArrs)
            ]
        else:
            self.outArrs = self.inArrs  # TODO
            self.converters = [
                X0(inArr, outArrs, f, i) for (i, inArr) in enumerate(self.inArrs)
            ]

    def __call__(
            self,
            inArrs: Union[np.ndarray, Sequence[np.ndarray]],
            outShapes: Union[Shape, Sequence[Shape]] = [],
            extraShapes: Union[Shape, Sequence[Shape]] = [],
            f: Dict[str, Callable] = {},
    ) -> Sequence[np.ndarray]:
        addList = lambda x: [x] if not isinstance(x, list) else x
        inArrs = addList(inArrs)
        outShapes = addList(outShapes)
        extraShapes = addList(extraShapes)
        if f == {}:
            f = self.f
        if not outShapes:
            outShapes = [(-1,)] * len(self.converters)
        if not extraShapes:
            extraShapes = [(0,)] * len(self.converters)
        if len(self.outArrs) == 1 and self.simpleParams:
            return tuple(
                arrayConverter(inArrs, outShape, extraShape, f)
                for (arrayConverter, outShape, extraShape) in zip(
                    self.converters, outShapes, extraShapes
                ))[0]
        else:
            return tuple(
                arrayConverter(inArrs, outShape, extraShape, f)
                for (arrayConverter, outShape, extraShape) in zip(
                    self.converters, outShapes, extraShapes
                ))

    def __repr__(self) -> str:
        if len(self.converters) == 1:
            return self.converters[0].__repr__()
        return "\n".join(
            [
                "out{}: {}".format(i, converter)
                for (i, converter) in enumerate(self.converters)
            ]
        )

    def __len__(self) -> int:
        return len(self.converters)

    def __getitem__(self, key: int) -> X0:
        return self.converters[key]

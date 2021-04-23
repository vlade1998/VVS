from enum import Enum

class InvalidTriangle(Exception):
    pass

class TriangleType(Enum):
    EQUILATERAL = 1
    ISOSCELES = 2
    SCALENE = 3

class Triangle:

    def __init__(self, sideA, sideB, sideC):
        if(sideA <= 0 or sideB <= 0 or sideC <= 0):
            raise InvalidTriangle

        if(
            sideA >= sideB + sideC or
            sideB >= sideA + sideC or
            sideC >= sideA + sideB
        ):
            raise InvalidTriangle

        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC 

    def classify(self):
        if(self.sideA == self.sideB and self.sideB == self.sideC):
            return TriangleType.EQUILATERAL
        if(self.sideA == self.sideB or self.sideB == self.sideC or self.sideA == self.sideC):
            return TriangleType.ISOSCELES
        return TriangleType.SCALENE

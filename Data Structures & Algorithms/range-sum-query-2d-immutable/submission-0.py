class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sums += self.matrix[i][j]

        return sums
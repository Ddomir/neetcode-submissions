class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.numMatrix = []

        # First row
        rowSum = 0
        rowArr = []
        for num in matrix[0]:
            rowSum += num
            rowArr.append(rowSum)
        self.numMatrix.append(rowArr)

        # All other rows
        for row in range(1, len(matrix)):
            rowSum = 0
            rowArr = []
            for i, num in enumerate(matrix[row]):
                rowSum += num
                rowArr.append(rowSum + self.numMatrix[row - 1][i])
            self.numMatrix.append(rowArr)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0: # Top left aligned
            return self.numMatrix[row2][col2]
        elif row1 == 0: # Top aligned, space on left
            return (self.numMatrix[row2][col2] - self.numMatrix[row2][col1 - 1])
        elif col1 == 0: # Left aligned
            return (self.numMatrix[row2][col2] - self.numMatrix[row1 - 1][col2])
        else:
            return (self.numMatrix[row2][col2] - self.numMatrix[row2][col1 - 1]
                    - self.numMatrix[row1 - 1][col2] + self.numMatrix[row1 - 1][col1 - 1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
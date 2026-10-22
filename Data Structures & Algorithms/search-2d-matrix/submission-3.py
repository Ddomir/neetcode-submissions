class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRow, highRow = 0, len(matrix) - 1

        while lowRow <= highRow:
            midRow = lowRow + (highRow - lowRow) // 2
            print(str(highRow) + " " + str(midRow) + " " + str(lowRow) + " ")


            if target in matrix[midRow]: # If in Row
                return True
            
            if target < matrix[midRow][0]:
                highRow = midRow - 1
            else:
                lowRow = midRow + 1

        return False
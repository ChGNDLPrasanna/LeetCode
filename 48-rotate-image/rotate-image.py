class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for row in range(n):
            for column in range(row+1,n):
                matrix[row][column], matrix[column][row] =matrix[column][row],matrix[row][column]
        for row in range(n):
            matrix[row] = matrix[row][::-1]






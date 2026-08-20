class Solution(object):

    def l1(self, matrix, top, bottom, right, left, result):

        if top > bottom or left > right:
            return

        # Top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])

        # Right column
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        # Bottom row
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][i])

        # Left column
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])

        # Go inside
        self.l1(matrix, top + 1, bottom - 1, right - 1, left + 1, result)


    def spiralOrder(self, matrix):
        result = []

        if not matrix:
            return result

        self.l1(matrix,0,len(matrix) - 1,len(matrix[0]) - 1 ,0,result)
        return result
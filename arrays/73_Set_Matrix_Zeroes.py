class Solution:

    def setZeros(self,row,col,hsetRow,hsetCol,matrix):
        for i in range(len(matrix[row])):
            hsetRow[(row,col)].append((row,i))
        for i in range(len(matrix)):
            hsetCol[(row,col)].append((i,col))

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hsetRow = defaultdict(list)
        hsetCol = defaultdict(list)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    self.setZeros(row,col,hsetRow,hsetCol,matrix)
        
        for positions in hsetRow.values():
            for row, col in positions:
                matrix[row][col] = 0

        for positions in hsetCol.values():
            for row, col in positions:
                matrix[row][col] = 0

        

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9): # rows
            for j in range(9):# cols

  
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3,j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3,j//3)].add(board[i][j])
                # print(rows[i])

        return True
# time:O(n^2)
# space : O(n^2 + n/3)

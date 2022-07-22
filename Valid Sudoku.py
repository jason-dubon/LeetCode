class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = defaultdict(set)
        
        for r in range(len(board)):
            row = set()
            col = set()
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    row.add(board[r][c])
                    
                    if board[r][c] in squares[(r // 3, c //3)]:
                        return False
                    squares[(r // 3, c //3)].add(board[r][c])
                
                # flipping the indicies to also go through each column in the nested for loop
                if board[c][r] != ".":
                    if board[c][r] in col:
                        return False
                    col.add(board[c][r])
              
        return True
        
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Check horizontal
        
        for x in range(9):
            s = set()
            for y in range(9):
                if board[x][y] != ".":
                    if board[x][y] not in s:
                        s.add(board[x][y])
                    else:
                        return False
         
        # Check vertical
        for x in range(9):
            s = set()
            for y in range(9):
                if board[y][x] != ".":
                    if board[y][x] not in s:
                        s.add(board[y][x])
                    else:
                        return False
                    
        # Check squares
        for x in range(0,9,3):
            for y in range(0,9,3):
                s = set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j] != ".":
                            if board[i][j] not in s:
                                s.add(board[i][j])
                            else:
                                return False
        
        
        
        
        return True

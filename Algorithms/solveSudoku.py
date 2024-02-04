import copy

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        
        
        solvedTiles = self.get_num_solved_tiles(board)
        print(f'Initial solved tiles: {solvedTiles} ({(solvedTiles / 81) * 100}%)')
        self.display(board, False)
        print('Running solving pass')
        

        improved = True

        while improved:
            self.deterministic_solver_1(board) # Deterministic solving attempt
            if self.get_num_solved_tiles(board) > solvedTiles:
                improved = True
                print(f'Deterministic solver 1 found {self.get_num_solved_tiles(board) - solvedTiles} new positions')
                solvedTiles = self.get_num_solved_tiles(board)
                print(f'Solved tiles: {solvedTiles} ({(solvedTiles / 81) * 100}%)')
                self.display(board, False)
                
            else:
                improved = False
                print('No new solutions found using deterministic solver 1.')
                print('Attempting to solve with deterministic solver 2.')
                
                self.deterministic_solver_2(board) # Secondary deterministic solving attempt
                
                if self.get_num_solved_tiles(board) > solvedTiles:
                    improved = True
                    print(f'Deterministic solver 2 found {self.get_num_solved_tiles(board) - solvedTiles} new positions')
                    solvedTiles = self.get_num_solved_tiles(board)
                    print(f'Solved tiles: {solvedTiles} ({(solvedTiles / 81) * 100}%)')
                    self.display(board, False)
                else:
                    improved = False
                    print('No new solutions found using deterministic solver 2.')
                    
                    
                
                
                
                

        print()
        self.display(board, False)


    def random_solver_position(self, board):
        position = (-1,-1)
        for x in range(9):
            for y in range(9):
                if len(board[x][y]) >= 2:
                    position = (x,y)

        return(position)
        


    # Calculates an optimal pass through the board using easy strategy
    def deterministic_solver_1(self, board):
        # For each tile, determine from the known positions, what the set of possible positions is.
        for x in range(9):
            for y in range(9):
                
                # Which is unsolved
                if board[x][y] == "." or len(board[x][y]) >= 2 or board[x][y] == "":
                    vSet = self.get_v_set(board, y)
                    hSet = self.get_h_set(board, x)
                    bSet = self.get_b_set(board, x, y)
                    
                    # Place the set of all possible values. If set has size 1, we are done.
                    intersection = self.getIntersection(vSet, hSet, bSet)

                    if intersection == "":
                        print('Error: Empty intersection')
                    
                    board[x][y] = intersection

    # Calculates an optimal pass through the board using harder strategy
    def deterministic_solver_2(self, board):
        # For each unknown position, determine for each possible value if that value could occur in vert, hori, or box.
        for x in range(9):
            for y in range(9):

                # Each position
                if len(board[x][y]) >= 2:

                    # If a position is not yet known, we can determine if each possible value at this position could be placed elsewere in the vertical line.
                    vertical_possible_values = set()
                    for i in range(9):
                        if i != y:
                            for j in board[x][i]:
                                vertical_possible_values.add(j)
                    
                    # For each possible value at x,y
                    for i in board[x][y]:
                        if i not in vertical_possible_values:
                            # found a solution
                            board[x][y] = i
                            print(f"DEBUG: Solver 2 found that {i} should be placed at position {x,y}")

                            return True


                    



        
                        
                    
    def get_num_solved_tiles(self, board):
        c = 0
        for x in range(9):
            for y in range(9):
                if board[x][y] != "." and len(board[x][y]) == 1:
                    c += 1
        return c


    def get_v_set(self, board, y):
        occuringSet = set()
        for i in range(9):
            # Known position
            if board[i][y] != "." and len(board[i][y]) == 1: 
                occuringSet.add(board[i][y])

        allSet = set(["1","2","3","4","5","6","7","8","9"])

        permittedSet = allSet.difference(occuringSet)

        return permittedSet

    def get_h_set(self, board, x):
        occuringSet = set()
        for i in range(9):
            # Known position
            if board[x][i] != "." and len(board[x][i]) == 1: 
                occuringSet.add(board[x][i])

        allSet = set(["1","2","3","4","5","6","7","8","9"])

        permittedSet = allSet.difference(occuringSet)

        return permittedSet

    def get_b_set(self, board, x, y):
        occuringSet = set()
        for i in range((x//3)*3, (x//3)*3+3):
            for j in range((y//3)*3, (y//3)*3+3):
                if board[i][j] != "." and len(board[i][j]) == 1: 
                    occuringSet.add(board[i][j])

        allSet = set(["1","2","3","4","5","6","7","8","9"])    
        permittedSet = allSet.difference(occuringSet)
        return permittedSet

    def getIntersection(self, s1, s2, s3):
        return ''.join(list(s1.intersection(s2.intersection(s3))))

    def display(self, board, nice):
        for y in range(9):
            print('|', end='')
            for x in range(9):
                if len(board[x][y]) <= 1:
                    print(board[x][y], end='')
                    
                else:
                    if nice:
                        print('?', end='')
                    else:
                        print(board[x][y], end='')
                print('|', end='')
            print()
        print()

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
            

s = Solution()

b1 = [
[".",".","9","7","4","8",".",".","."],
["7",".",".",".",".",".",".",".","."],
[".","2",".","1",".","9",".",".","."],
[".",".","7",".",".",".","2","4","."],
[".","6","4",".","1",".","5","9","."],
[".","9","8",".",".",".","3",".","."],
[".",".",".","8",".","3",".","2","."],
[".",".",".",".",".",".",".",".","6"],
[".",".",".","2","7","5","9",".","."]]

b2 = [
["23","23","23","23","25","23","23","23","23"],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."],
["12",".",".",".",".",".",".",".","."]]



s.solveSudoku(b2)

#print(s.get_v_set(b,0))
#print(s.get_h_set(b,0))
#print(s.get_b_set(b,0,0))
#print(s.getIntersection(s.get_v_set(b,0), s.get_h_set(b,0), s.get_b_set(b,0,0)))












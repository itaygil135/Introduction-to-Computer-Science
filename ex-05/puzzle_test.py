import puzzle_solver
import sys

word_list = [ "FOR", "BREAK", "LOOP"]
puzzle = [
            [ 'F', 'a','P', 'O','O', 'L'],
            [ 'b', 'O','m', 'c','d', 'e'],
            [ 'f', 'B','R', 'E','A', 'K'],
            [ 'g', 'h','i', 'F','O', 'R']]            


#print(sys.argv[0])    
#print (len(sys.argv))
#print (sys.argc)    
#-----------------   program body  ----------------
puzzle_solver.solve_puzzle(puzzle,word_list)

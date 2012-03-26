#THREE GOLD STARS
import sys
#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

def check_list(p, n):
    for item in range(1,n):
        #print item
        if item not in p:
            return False
    return True
        

def check_sudoku(tocheck):
    n = len(tocheck)
    #print 'length = ',n
    row_check = True
    col_check = True
    for row in tocheck:
        if check_list(row, n) == False:
            row_check = False
    #create list of column elements and checking them
    column = []
    for number in range(1,n):
        for row in tocheck:
            column.append(row[number])
        if check_list(column,n) == False:
            col_check = False
        #print column
        column = []
    if row_check == False or col_check == False:
        return False
    else:
        return True
    
#check_sudoku(incorrect)
#check_sudoku(correct)
    

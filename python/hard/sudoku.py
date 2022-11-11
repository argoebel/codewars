# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

import copy

def sudoku(puzzle):
    numbers = [x for x in range(1,10)]
    tried = [[[] for y in range(1,10)] for x in range(1,10)]
    
    attempt = copy.copy(puzzle)

    rowIndex = 0
    colIndex = 0


    while rowIndex < len(attempt[0]):
        while colIndex < len(attempt[0][0]):
            if puzzle[rowIndex][colIndex] == 0:
                if colIndex == 8:
                    colIndex = 0
                    rowIndex += 1
                else:
                    colIndex += 1
            else:

                column = [y[colIndex] for y in attempt if y[colIndex] != 0]
                options = [option for option in numbers if option not in column and option not in tried[rowIndex][colIndex]]

                print()
                print(column)
                print(options)

                if len(options) == 0:
                    tried[rowIndex][colIndex] = []
                    if colIndex == 0:
                        colIndex = 8
                        rowIndex -= 1                
                else:
                    tried[rowIndex][colIndex].append(options[0])
                    attempt[rowIndex][colIndex] = options[0]

            rowIndex += 1
    
    
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
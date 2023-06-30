# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

import copy
def sudoku(puzzle):
    numbers = [x for x in range(1,10)]
    tried = [[[] for y in range(1,10)] for x in range(1,10)]
    attempt = copy.deepcopy(puzzle)
    
    rowIndex = 0
    colIndex = 0
    lastVal = 1

    while rowIndex < len(attempt) and rowIndex >= 0:
        while colIndex < len(attempt[0]) and colIndex >= 0:
            if puzzle[rowIndex][colIndex] == 0:
                column = [y[colIndex] for y in attempt if y[colIndex] != 0]
                row = attempt[rowIndex]
                rowRange = rowIndex // 3
                colRange = colIndex // 3

                ninth = [items[colRange*3:colRange*3+3] for items in attempt[rowRange*3:rowRange*3+3]]
                ninth = ninth[0] + ninth[1] + ninth[2]

                options = [option for option in numbers if option not in column and option not in tried[rowIndex][colIndex] and option not in row and option not in ninth]

                if len(options) == 0:
                    lastVal = -1
                    tried[rowIndex][colIndex] = []
                    attempt[rowIndex][colIndex] = 0
                else:
                    lastVal = 1
                    tried[rowIndex][colIndex].append(options[0])
                    attempt[rowIndex][colIndex] = options[0]
            
            colIndex += lastVal

        if lastVal == 1:
            rowIndex += 1
            colIndex = 0
        else:
            rowIndex -= 1
            colIndex = 8
    
    return attempt

# import copy
# def sudoku(puzzle):
#     numbers = [x for x in range(1,10)]
#     tried = [[[] for y in range(1,10)] for x in range(1,10)]
#     attempt = copy.deepcopy(puzzle)
    
#     rowIndex = 0
#     colIndex = 0
#     lastVal = 1

#     while rowIndex < len(attempt):
#         while colIndex < len(attempt[0]) and colIndex >= 0:
#             if puzzle[rowIndex][colIndex] == 0:
#                 column = [y[colIndex] for y in attempt if y[colIndex] != 0]
#                 row = attempt[rowIndex]
#                 rowRange = (rowIndex+1) // 3
#                 colRange = (colIndex+1) // 3

#                 ninth = [items[colRange*3:colRange*3+3] for items in attempt[rowRange*3:rowRange*3+3]]
#                 ninth = ninth[0] + ninth[1] + ninth[2]

#                 options = [option for option in numbers if option not in column and option not in tried[rowIndex][colIndex] and option not in row and option not in ninth]


#                 if len(options) == 0:
#                     lastVal = -1
#                     tried[rowIndex][colIndex] = []
#                     attempt[rowIndex][colIndex] = puzzle[rowIndex][colIndex]
#                 else:
#                     lastVal = 1
#                     tried[rowIndex][colIndex].append(options[0])
#                     attempt[rowIndex][colIndex] = options[0]
#             colIndex += lastVal
#         if lastVal == 1:
#             rowIndex += 1
#             colIndex = 0
#         else:
#             rowIndex -= 1
#             colIndex = 8
    
#     return attempt

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))
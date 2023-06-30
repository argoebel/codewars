# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python
import numpy as np


def transpose(matrix):
    newMatrix = []
    for i in range(len(matrix[0])):
        demo = []
        for j in range(len(matrix)):
            demo.append(matrix[j][i])
        newMatrix.append(demo)
    return newMatrix

transpose([[1,2,3]])
transpose([[1, 2, 3], [4, 5, 6]])
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def transpose(matrix):
    return np.transpose(np.matrix(matrix)).tolist()
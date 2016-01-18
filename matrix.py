import random

def vectorMatrixMultiplication(vector, matrix):
    return [sum([vector[x]*matrix[n][x] for x in range(len(vector))]) for n in range(len(matrix))]


def matrix_multiplication(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        print "ERROR! Matrix1 column not equal to Matrix2 row! :D !!"
    else:
        return [[[sum([matrix1[m][x]*matrix2[x][n] for x in range(len(matrix1[m]))]) for n in range(len(matrix2))]] for m in range(len(matrix1))]


def generateMatrix_A(m, n):
    matrix_A = list()
    for i in range(m):
        row = list()
        for j in range(n):
            row.append(random.randint(0, 10))
        matrix_A.append(row)
    return matrix_A

def generateMatrix_B(l, k):
    matrix_B = list()
    for i in range(k):
        row = list()
        for j in range(l):
            row.append(random.randint(0, 10))
        matrix_B.append(row)
    return matrix_B

matrix_A = generateMatrix_A(300, 600)
print matrix_A
matrix_B = generateMatrix_B(900, 600)
print matrix_B
matrix_C = matrix_multiplication(matrix_A,matrix_B)
print matrix_C

f = open("ResMatrix.txt", 'w')
f.write(str(matrix_A) +'\n')
f.write(str(matrix_B) +'\n')
f.write(str(matrix_C) +'\n')
f.close()

###Patrick Leung
###vector matrix multiplication
def vectorMatrixMultiplication(vector, matrix): 
    return [sum([vector[x]*matrix[n][x] for x in range(len(vector))]) for n in range(len(matrix))] 

##vector example
vector = [1,2]
matrix = [[1,2],[5,6]]    
vectorMatrixMultiplication(vector,matrix) 

####matrix multiplication
#range(len(matrix1[m])) = no. of rows in matrix 1 = no. of row in the result
# range(len(matrix2)) = no. of columns in matrix 2 = no. of column in the result 
#checking: no. of columns in matrix 1 must equal to no. of rows in matrix 2
def matrix_multiplication(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        print "ERROR! Matrix1 column not equal to Matrix2 row! :D !!"
    else:
        return [[[sum([matrix1[m][x]*matrix2[x][n] for x in range(len(matrix1[m]))]) for n in range(len(matrix2))]] for m in range(len(matrix1))] 

#example 1
matrix1 = [[0,-3,-1,4],[-4,-2,5,6],[7,8,1,2]]
matrix2 = [[0,3,-1,4],[9,-3,5,6],[7,8,10,1],[11,12,2,13]]
matrix_multiplication(matrix1,matrix2)

#example 2
matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
matrix_multiplication(matrix1,matrix2)

#example 3  (not working)
matrix1 = [[1,2,3],[4,5,6]]
matrix2 = [[1,2],[5,6]]
matrix_multiplication(matrix1,matrix2)

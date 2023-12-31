from CheckDim import checkDim
from MatrixImporter import matrixCsvImporter
from MatrixExporter import matrixExporter

def matrixSum(matrix1,matrix2):
    newmatrix = []
    if checkDim(matrix1,matrix2) == False: #We check if they are the same dimension, the error messages are already within the function so no need to make an else statement
        for subl1,subl2 in zip(matrix1,matrix2):
            submatrix = []
            for num1,num2 in zip(subl1,subl2):
                submatrix.append(num1 + num2) #we add the numbers 1 by 1 and add them to the submatrix
            newmatrix.append(submatrix)
    return newmatrix

m1 = matrixCsvImporter("Matrix calculator\MatrixGrid.csv")
m2 = matrixCsvImporter("Matrix calculator\MatrixGrid.csv",2)
matrixExporter("Matrix calculator\MatrixResult.csv",matrixSum(m1,m2))
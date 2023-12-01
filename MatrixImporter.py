def matrixCsvImporter(filename: str, num = 1): #this is the function that allows us to import matrices from csv files
    with open(filename) as f:
        liste = f.read().split() #we transform our file into a lists
    Matrix = [] #this is our matrix
    for i in liste:
        sublist = i.split(",_,")#we separate the elements of the two matrices into a new sublist
        for i in range(0,len(sublist),num): #the num represents the matrix we are working with (1 = first matrix, 2 = second matrix)
            sublist2 = sublist[i].split(",") #We create a new list out fo the string by spliting them on the commass
            sublist3 = []
            for  j in sublist2:
                sublist3.append(float(j)) #we convert the elements into floats and append them to list
        Matrix.append(sublist3) #we append each row to the Matrix at the end of the loop
    return Matrix

#print(matrixCsvImporter("Matrix calculator\MatrixGrid.csv"))
#print(matrixCsvImporter("Matrix calculator\MatrixGrid.csv",2))
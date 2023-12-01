def matrixCsvImporter(filename: str, num = 1):
    with open(filename) as f:
        liste = f.read().split()
    Matrix = []
    for i in liste:
        sl = i.split(",_,")
        for i in range(0,len(sl),num):
            sl2 = sl[i].split(",")
            sl3 = []
            for  j in sl2:
                sl3.append(int(j))
        Matrix.append(sl3)
    return Matrix

#print(matrixCsvImporter("Matrix calculator\MatrixGrid.csv"))
#print(matrixCsvImporter("Matrix calculator\MatrixGrid.csv",2))
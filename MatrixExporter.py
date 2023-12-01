def matrixExporter(filename: str, matrix: list):
    with open(filename,"w") as f:
        for sublist in matrix:
            for number in sublist:
                f.write(str(number) + ",")
            f.write("\n")
                
#matrixExporter("Matrix calculator\MatrixResult.csv", [[2, 4, 6, 8, 12], [2, 4, 6, 8, 13], [5, 7, 9, 8, 12], [5, 7, 8, 9, 13], [6, 8, 9, 11, 13]])
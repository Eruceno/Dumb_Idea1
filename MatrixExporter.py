def matrixExporter(filename: str, matrix: list): #this is function that allows us to transport our matrix into a csv file
    with open(filename,"w") as f:
        for sublist in matrix:
            for number in sublist:
                f.write(str(number) + ",") #we separates every elements in the list with commas
            f.write("\n") #we go to next line when we go from a list to another
                
#matrixExporter("Matrix calculator\MatrixResult.csv", [[2, 4, 6, 8, 12], [2, 4, 6, 8, 13], [5, 7, 9, 8, 12], [5, 7, 8, 9, 13], [6, 8, 9, 11, 13]])
Bye = False #this is a global variable that allows us to turn off our recursive function 
Dim = 1 #this is the variable in which the dimension of our matrix is stored altough we are not using it here
def checkDim(matrix1: list,matrix2: list):
    global Dim 
    global Bye
    if len(matrix1) == len(matrix2) and Bye == False:
        for i,j in zip(matrix1,matrix2):
            if isinstance(i, list) and isinstance(j,list) and Bye == False:
                Dim += 1
                if len(i) == len(j) and Bye == False:
                    checkDim(i,j) #if our elements of the two lists are lists of the same lenght, we start the process all over again
                else:
                    print("Addition impossible, matrices ne sont pas de même Taille")
                    Bye = True #if the lenghts are not the same we escape
            elif (isinstance(i,list) and not isinstance(j,list)) or (not isinstance(i,list) and isinstance(j,list)):
                print("Addition impossible, les matrices ne sont pas de même dimension") #if one of the element is a list and the other is not we escape
                Bye = True
                break 
    else: Bye == False #if none of the subelements are lists and the other conditions are verified we return False to say everything is oks
    return Bye#,Dim//2
#print(checkDim([[[1,2,4],[3,3,4]],[[2,3,4],[3,3,4]]],[[[1,2,4],[3,3,4]],[[2,3,4],[3,3,4]]]))
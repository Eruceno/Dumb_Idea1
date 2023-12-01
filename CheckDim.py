Bye = False
Dim = 1
def checkDim(l1,l2):
    global Dim
    global Bye
    if len(l1) == len(l2) and Bye == False:
        for i,j in zip(l1,l2):
            if isinstance(i, list) and isinstance(j,list) and Bye == False:
                Dim += 1
                if len(i) == len(j) and Bye == False:
                    checkDim(i,j)
                else:
                    print("Addition impossible, matrices ne sont pas de même Taille")
                    Bye = True
            elif (isinstance(i,list) and not isinstance(j,list)) or (not isinstance(i,list) and isinstance(j,list)):
                print("Addition impossible, les matrices ne sont pas de même dimension")
                Bye = True
                break
    else: Bye == False
    return Bye#,Dim//2
#print(checkDim([[[1,2,4],[3,3,4]],[[2,3,4],[3,3,4]]],[[[1,2,4],[3,3,4]],[[2,3,4],[3,3,4]]]))
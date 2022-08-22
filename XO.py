

def isWin (mtx):
    winner1 = False 
    score1=1
    aaa=0
    
    for i in range(3):
        aaa=0
        while (aaa<3 and i<3 and score1<3):
            aaa=aaa+1
            if mtx[i][score1-1]==mtx[i][score1]:
                score1=score1+1
                print (mtx[i][score1],score1,i)
                
                if score1==2:
                    winner1=True
                    return (winner1)
                    
            else:
                score1=1
                break
            
                
    for i in range(3):
            aaa=0
            while (aaa<3 and i<3 and score1<3):
                aaa=aaa+1
                if mtx[score1-1][i]==mtx[score1][i]:
                    score1=score1+1
                    print (mtx[score1][i],score1,i)
                    
                    if score1==2:
                        winner1=True
                        return (winner1)
                        
                else:
                    score1=1
                    break
    if mtx[0][0]==mtx[1][1]==mtx[2][2] or mtx[0][2]==mtx[1][1]==mtx[2][0]:
        winner1=True
        return (winner1)
               
    return winner1
i=0  
winn=False
matrix=[["X","A","kk"],
        ["D" ,"DD","ksk" ],
        ["FDF" ,"DD" , "kk"]
        ]
print (isWin(matrix))
"""while (winn == False and i<10):
    row=int(input("player x enter row"))
    column1=int(input("player x enter column"))
    matrix[row][column1]="x"
    winn=isWin(matrix)
    print (matrix)       
    if winn==True:
        print ("player 1 won",matrix)
        break
    else:
        row2=int(input("player O enter row"))
        column2=int(input("player O enter column"))
        matrix[row2][column2]="O"
        winn=isWin(matrix)
        if winn==True:
            print ("player 1 won",matrix)
            break
    i=i+1
    print (matrix)        


"""
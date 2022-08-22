

def isWin (mtx):
    winner1 = False 
    score1=1
    
    for i in range(3):
            if mtx[i][score1-1]==mtx[i][score1]==mtx[i][score1+1] and  (mtx[i][score1-1]=="X" or mtx[i][score1-1]=="O") and  (mtx[i][score1+1]=="X" or mtx[i][score1+1]=="O"):
                
                print (mtx[i][score1],score1,i)
                winner1=True
                return (winner1)
                    
                
    for i in range(3):
        if mtx[score1-1][i]==mtx[score1][i]==mtx[score1+1][i] and (mtx[score1-1][i]=="X" or mtx[score1-1][i]=="O") and  (mtx[score1+1][i]=="X" or mtx[score1+1][i]=="O"):
                
            print (mtx[i][score1],score1,i)
            winner1=True
            return (winner1)
    if mtx[0][0]==mtx[1][1]==mtx[2][2] or mtx[0][2]==mtx[1][1]==mtx[2][0] and (mtx[1][1]=="O" or mtx[1][1]=="X") :
        winner1=True
        return (winner1)
               
    return winner1
iForTie=0  
winn=False
matrix=[[" "," "," "],
        [" " ," "," " ],
        [" " ," " , " "]
        ]
while (winn == False and iForTie<10):
    iForTie +=1
    while winn!=True:
        row=int(input("player x enter row: "))
        column1=int(input("player x enter column: "))
        
        if matrix[row][column1]=="X" or matrix[row][column1]=="O":
            print("enter another coordinate")
        else:
            matrix[row][column1]="X"
            winn=isWin(matrix)
            break
    for i in range(3):
            
        print ("\n" +matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n")             
    if winn==True:
        print ("player 1 won")
        break
            
    else:
        while winn!=True:
            row2=int(input("player O enter row: "))
            column2=int(input("player O enter column: "))
            if matrix[row2][column2]=="X" or matrix[row2][column2]=="O":
                    print("enter another coordinate")
            else:
                matrix[row2][column2]="O"
                winn=isWin(matrix)
                break
        for i in range(3):
            
            print ("\n" +matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n")     
        if winn==True:
            print ("player 2 won")
            break
    if iForTie==10:
        print("its a tie")           
for i in range(3):
            
    print (matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n") 

    i=i+1


"""צריך להוסיף בדיקה שלא מכניסים בתא שכבר יש בו X או O"""


from tkinter import N


def isWin (mtx):
    winner1 = False 
    score1=1
    
    for i in range(3):
            if mtx[i][score1-1]==mtx[i][score1]==mtx[i][score1+1] and (mtx[i][score1-1]=="X" or mtx[i][score1-1]=="O"):
                
                print (mtx[i][score1],score1,i)
                winner1=True
                return (winner1)
                    
                
    for i in range(3):
        if mtx[score1-1][i]==mtx[score1][i]==mtx[score1+1][i] and (mtx[score1-1][i]=="X" or mtx[score1-1][i]=="O"):
                
            print (mtx[i][score1],score1,i)
            winner1=True
            return (winner1)

    if mtx[0][0]==mtx[1][1]==mtx[2][2] or mtx[0][2]==mtx[1][1]==mtx[2][0] and (mtx[0][0]=="O" or mtx[0][0]=="X") :
        winner1=True
        return (winner1)
               
    return winner1
i=0  
winn=False
matrix=[["a","b","c"],
        ["d" ,"e","f" ],
        ["g" ,"h" , "i"]
        ]
print (isWin(matrix))
while (winn == False and i<10):
    row=int(input("player x enter row: "))
    column1=int(input("player x enter column: "))
    matrix[row][column1]="x"
    winn=isWin(matrix)
    for i in range(3):
        print (matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n")       
    if winn==True:
        print ("player 1 won",matrix)
        for i in range(3):
            
            print (matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n") 
        break
    else:
        row2=int(input("player O enter row: "))
        column2=int(input("player O enter column: "))
        matrix[row2][column2]="O"
        winn=isWin(matrix)
        if winn==True:
            print ("player 2 won")
            for i in range(3):
                print (matrix[i][0]+" "+matrix[i][1]+" " +matrix[i][2]+"\n")
            break
    i=i+1
    print (matrix)        



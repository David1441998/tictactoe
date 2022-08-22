mA = [[1, 2],
    [3, 4],
    [5, 6]]
matrix=[]
"""print (mA[1][1] , "דשג")"""
for i in range(3):
    a=[]
    for j in range(3):
       a.append(int(input("enter num")))
    matrix.append(a)    

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()     
    
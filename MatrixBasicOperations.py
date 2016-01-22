#!usr/bin Python 3.5.1
#####  N * N Matrix Mathematical Basic Operations like Addition, Substraction, Multiplication and multiplication of matrix by number   #####

# Author Narendra Prasath

##    First Matrix n*n Initialization
def readMatrix1():
    for i in range(0,m):
        for j in range(0,n):
            matrix = [[0 for i in range(n)] for j in range(m)]
    print("****First Matrix Initial Values ****")
    print(matrix)
    for i in range(m):
        for j in range(n):
            print("enter the values in Row", i+1,"and Column ", j+1)
            matrix[i][j] = int(input("enter value"))
    return matrix

##    Second Matrix n*n Initialization    
def readMatrix2():
    for a in range(0,m):
        for b in range(0,n):
            matrix2 = [[0 for a in range(m)] for b in range(n)]
    print("****Second Matrix Initial values****")
    print(matrix2)
    for x in range(m):
        for y in range(n):
            print("enter the values in Row", x+1,"and Column ", y+1)
            matrix2[x][y] = int(input("enter value"))
    return matrix2
##     Add two matrix
def addMatrix(mat1,mat2):
    print("The first matrix is",mat1)
    print("The second matrix is",mat2)
    for i in range(0,m):
        for j in range(0,n):
            addMat = [[0 for i in range(n)] for j in range(m)]
    for a in range (0,m):
        for b in range(0,n):
            addMat[a][b] = mat1[a][b] + mat2[a][b]
    print("The Addition Matrix will be ",addMat)
##      Subtract two matrix
def subMatrix(mat1,mat2):
     for i in range(0,m):
        for j in range(0,n):
            subMat = [[0 for i in range(n)] for j in range(m)]
     for a in range (0,m):
        for b in range(0,n):
            subMat[a][b] = mat1[a][b] - mat2[a][b]
     print("The Substraction Matrix will be ",subMat)

##      Multiplication of two matrix
def mulMatrix(mat1,mat2):
    for i in range(0,m):
        for j in range(0,n):
            mulMat = [[0 for i in range(n)] for j in range(m)]
    sum = 0
    for i in range(0,m):
        for j in range(0,n):
            for k in range(0,m):
                sum = sum + mat1[i][k] * mat2[k][j]
            mulMat[i][j] = sum;
            sum = 0;
    print("The Multiplication Matrix will be ",mulMat)

##      Multiplication of a matrix by a number
def numMatrix(mut1,mat2):
    n = int(input('Enter a number to multiply with matrix'))
    for i in range(0,m):
        for j in range(0,n):
            MatbyNo = [[0 for i in range(n)] for j in range(m)]
    print("----1. First Matrix-----")
    print("----1. Second Matrix-----")
    Choice = int(input('Choose a matrix'))
    if Choice == 1:
        for a in range (0,m):
            for b in range(0,n):
                MatbyNo[a][b] = mat1[a][b] * n
        print("The first Matrix multiply by a no will be ",MatbyNo)
    elif Choice == 2:
        for a in range (0,m):
            for b in range(0,n):
                MatbyNo[a][b] = mat2[a][b] * n
        print("The second Matrix multiply by a no will be  ",MatbyNo)
    else:
        print("Invalid try ... Try again")  
        
##      Display the options
def display():
    print("-------------------")
    print("---SELECT CHOICE---")
    print(" 1. Addition of n*n matrix  ")
    print(" 2. Substration of n*n matrix  ")
    print(" 3. Multiplication of n*n matrix  ")
    print(" 4. Multiplication of n*n matrix by a Number ")
    choice = int (input('Enter your number'))
    if choice == 1:
        print("Would you like to perform Addition of Two n*n matrixs")
        addMatrix(mat1,mat2)
    elif choice == 2:
        print("Would you like to perform Substracion of Two n*n matrixs")
        subMatrix(mat1,mat2)
    elif choice == 3:
        print("Would you like to perform Multiplication of Two n*n matrixs")
        mulMatrix(mat1,mat2)
    elif choice == 4:
        print("Would you like to perform Multiplication of matrix by a number")
        numMatrix(mat1,mat2)
    else:
        print("Invalid try ... Try again")  

           
#MAIN function
print("--------------------")
print("Define n*n two matrix")
print("--------------------")
m = int(input('number of rows and columns m = '))
n = m    
mat1 = readMatrix1()
print("The First matrix is")
print(mat1)
mat2 = readMatrix2()
print("The Second matrix is")
print(mat2)
for k in range(4): 
    display()
    


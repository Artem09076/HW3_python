n= int(input())
matrix=[]

for i in range(n): #запрос n

    row = input().split(' ') #каждая строка разделяется на элементы

    if len(row) == n:

        matrix.append(row) #если кол-во элементов равно n, то строка добавляется в список a


def IsSymmetric(matrix,n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
        return True

if  IsSymmetric(matrix,n):
    print("YES")
else:
    print("NO")

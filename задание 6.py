n= int(input())
matrix=[]

for i in range(n): 

    row = input().split(' ') #строка разделяется на элементы

    if len(row) == n:

        matrix.append(row) #если количество элементов равно n, то строка добавляется в список 


def IsSymmetric(matrix,n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:#Если числа с индексами i и j не равны симметричным то по логике массив не симметричный
                return False
        return True

if  IsSymmetric(matrix,n):#Здесь если функция вывела True то пишем No если False то No
    print("YES")
else:
    print("NO")

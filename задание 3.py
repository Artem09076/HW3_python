arr = list(map(int, input().split()))

last_el=arr[-1]#Сохранием последний элемент списка
for i in range(len(arr)-2,-1,-1):#Ну мы здесь перебираем элементы списка слева на право с предпоследнего 
    arr[i+1]=arr[i]#Сдвигаем каждый элемент вправо на ождну позицию

arr[0]=last_el#Присвиваем последнему значению нулевой индекс
print(*arr)

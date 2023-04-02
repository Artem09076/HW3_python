x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
def can_eat(x1,x2,y1,y2):#Конь съедает фигуру если разность по x 2 и по y 1 и наоборот и мы просто проверяем по условию
    if x1-x2==2 and y1-y2==1:
        return True
    elif x1-x2==1 and y1-y2==2:
        return True
    else:
        return False

print(can_eat(x1,x2,y1,y2))
    

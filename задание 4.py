arr=["Манная", "Гречневая", "Пшённая" ,"Овсяная" ,"Рисовая"]
n=int(input())
for i in range(n):
    
    if i<=4:
        cer=arr[i]
    else:
        cer=arr[i%5]
    print(cer)


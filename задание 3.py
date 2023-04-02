arr = list(map(int, input().split()))

past_el=arr[-1]

for i in range(len(arr)-2,-1,-1):
    arr[i+1]=arr[i]

arr[0]=past_el
print(*arr)
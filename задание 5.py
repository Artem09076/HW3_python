arr = list(map(int, input().split()))
def equal_pairs(arr):
    s=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                s += 1
    return s

count=equal_pairs(arr)
print(count)
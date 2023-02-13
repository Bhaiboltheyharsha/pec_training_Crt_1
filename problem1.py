n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            count = count+1
if count > n//2:
    print(arr[i])
else:
    print("invaild")
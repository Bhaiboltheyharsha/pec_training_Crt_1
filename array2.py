n = int(input())
arr = list(map(int, input().split()))
k = int(input())
res = []
for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i]+arr[j] == k:
            res.append([arr[i], arr[j]])
print(res)
ans = []
for i in res:
    if i not in ans:
        ans.append(i)
print(len(ans))

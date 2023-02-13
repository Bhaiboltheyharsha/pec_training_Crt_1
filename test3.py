size = int(input())
max = count = flag = 0
bininput = input()
arr = list(bininput)
for i in range(0, size):
    if arr[i] == '1':
        count = count+1
        flag = 1
    elif arr[i] == '0' and flag == 1:
        count = 0
        flag = 0
    if count > max:
        max = count
print(max)

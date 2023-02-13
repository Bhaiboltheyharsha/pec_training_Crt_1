l = [1, 2, 3, 4, 5]
key = int(input("enter key"))
temp = False
for i in range(0, len(l)):
    if l[i] == key:
        print(i)
        temp = True
        break
if temp == False:
    print("Not Found")

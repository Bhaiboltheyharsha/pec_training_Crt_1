size=int(input())
d={}
for i in range(size):
    key=input()
    value=input()
    d.update({
        key:value
    })
print(d)
key=input()
if key in d:
    print(d[key])
else:
    print('invalid input')
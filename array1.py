arr1=[[1,2,3],[2,4,5],[5,67,9]]
q=[]
for i in range(len(arr1)):
    el=[]
    for j in range(len(arr1)):
        el.append(arr1[j][i])
    q.append(el)
print(q)

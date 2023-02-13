l2=list(map(int,input().split(' ')))
l3=[]
for i in l2:
	if l2.count(i)>int(len(l2)/2):
		l3.append(i)
	else:
		l3.append('No Majority Element Found')
l3=set(l3)
if len(l3)>1:
	for j in list(l3):
		print(j,' ')
else:
	print(list(l3)[0])
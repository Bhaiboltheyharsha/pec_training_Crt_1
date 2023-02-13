'''import numpy as np
numbers = list('12345')
a = list((map(int, numbers)))
print(a)
np.square(a)'''


def Sqaure(l, i):
    if i < len(l):
        print(l[i]*l[i])
        i = i+1
        Sqaure(l, i)
    else:
        return


Numbers = '12345'
l = list(map(int, Numbers))
i = 0
Sqaure(l, i)

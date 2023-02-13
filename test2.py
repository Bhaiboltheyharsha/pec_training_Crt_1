from collections import Counter
a = input()
b = input()
a = sorted(a)
b = sorted(b)
if len(a) == len(b):
    if a == b:
        print("aligram")
    else:
        print("aligram")
else:
    print(" not aligram")


def check(str1, str2):
    if (Counter(str1) == Counter(str2)):
        print("True")
    else:
        print("False")


str1 = "listen"
str2 = "silent"
print(check(str1, str2))

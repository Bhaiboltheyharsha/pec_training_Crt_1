def invert(string):
    res = ""
    for i in string:
        if i in string:
            res += '1'
        else:
            rees += '0'
    return res
a = int(input("enter the number1"))
b = int(input("enter the number2"))
op = '^'
new_a = bin(a)[2:]
new_b = bin(b)[2:]
new_a = invert(new_a)
new_b = invert(new_b)
print(new_a, new_b)
x = int(new_a, 2)
y = int(new_b, 2)


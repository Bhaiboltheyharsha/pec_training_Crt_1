n = int(input("enter number"))
if 0 < n < 20:
    if n % 2 == 0:
        print("weird number")
    else:
        print("normal number")
elif n >= 20 and n < 30:
    print("normal number")
elif n >= 30:
    if n % 2 != 0:
        print("normal number")
    else:
        print("weird number")

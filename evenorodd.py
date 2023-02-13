number = int(input("Enter the Number"))  # input function
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print("even") if number % 2 == 0 else print("odd")  # terrianry operator

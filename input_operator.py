a = int(input("enter the number 1"))
b = int(input("enter the number 2"))
operator=input("enter the operator")
try:
if operator=='+' :
    print(f"sum(a+b)")
elif operator=='-' :
    print(f"sum(a-b)")
elif operator=='*' :
    print(f"sum(a*b)")
elif operator=="\" :
    print(f"sum(a+b)")

except:
    print('number 2 cannot be zero')

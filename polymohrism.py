class a:
    def method_1(self,a,b):
        print(a+b)
class b(a):
    def method_1(self,a,b):
        print(a*b)
    def method_1(self,abc):#method overloading
        print("value is",abc)

obj = b()
obj.method_1(10,20,50)
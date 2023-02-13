class animal():
    pass
class dog(animal):
    def speak(self):
        print("bark")
class cat(animal):
    def speak(self):
        print("meow")
class lion(animal):
    def speak(self):
        print("roar")
obj = lion()
obj.speak()
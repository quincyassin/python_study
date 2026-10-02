# Python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

class Dog(Animal):          # ← 括号里写父类名
    def __init__(self, name):
        super().__init__(name)   # ← 和 Java 的 super() 一样
    
    def speak(self):
        return f"{self.name}：汪汪汪"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name}：喵喵喵"

animals = [Dog("旺财"), Cat("咪咪"), Dog("小黑")]

for animal in animals:
    print(animal.speak())
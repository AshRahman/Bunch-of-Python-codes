class NewAdd():
    def __init__(self,value):
        self.value = value
        
    def __add__(self,other):
        return (self.value*2)+(other.value*2)
    
a = NewAdd(2)
b = NewAdd(3)

c = a+b
print(c)

class MyInt():
    def __init__(self, value):
        self.__value = value
    def __int__(self):
        return self.__value
    def __add__(self,other):
        return self.__value + int(other) * int(other)
    
x = MyInt(2)
y = MyInt(3)

z = x+y

print(z)
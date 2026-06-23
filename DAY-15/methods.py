class Product:

    name = "Dell"
    price = 720
    config = {}

    def __init__(self,conf):
        self.config = conf

    @classmethod  
    def handleDefinition(cls):
        print("I class method")
        print(cls.name)

    @staticmethod
    def printHello():
        print("Hello")

    # factory function
    @staticmethod
    def create(option = {}):
        conf = {
            "devMod":True
        }
        return Product(conf)

p = Product.create()

Product.handleDefinition()

Product.printHello()


class Math():
    PI = 3.14

    @staticmethod
    def square(number):
        return number*number
    
    @classmethod
    def areaOfCircle(cls,radius):
        return cls.PI * (radius*radius)


print(Math.square(12))
print(Math.areaOfCircle(10))

''
''
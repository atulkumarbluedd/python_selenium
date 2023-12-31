class calculator:
    num=100
    valu1=9

    def getData(self, a, b):
        self.a=50
        self.b=6
        return self.a+self.b
        print("i am now executing this outside the class")
    def __init__(self,c,d):
        self.valu1=d
        print("heell")
        print(self.valu1)

# here we are outside the class
# to create constructor using _init_(self) // here classname is not same as class name.
# here when we are creating object then default constructor is called
# the variables which we define inside the constructor are called instance variables.
# for every object the instance variables can be different
# class varaibles are same for the class
# self is mendatory when we define method inside the class.
# we have two type of constructor default and parameterize constructor.
# if you want to call variables inside the method then always self dot variable name
# for the class variable it is class.variableName or self.variableName
#
obj=calculator(3,4)
sums=obj.getData(5,6)
print(sums)
print(obj.num)
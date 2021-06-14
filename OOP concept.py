#class

#syntax
    #class MyClass:

 #it contains data field to store the data and methods for defining behaviours



#object

    #object is an instance of a class

    #syntax
        #myc=MyClass()

    #myc, is object of class MyClass

 #self special char. of python

class Demo:             
    def myfunction(self):   
       print("function class")

    def show(self,name):
        print("value is",name)

d1=Demo()
d1.myfunction() 
d1.show("riddhi")




class demo1:
    def fun1(self,n1,n2):
        ans=n1+n2
        print("Ans is:",ans)

#create a object of demo1
myc=demo1()

#calling function
myc.fun1(10,20)





#constructors

#class fun. that instantiates an object to predefined values
# begind with __init__()
# 2 types- 1.default 2.parameterized


class Demo:             
    def myfunction(self):   
       print("function class")

    def show(self,name):
        print("value is",name)

    def __init__(self):         #default constructor
        print("demo class")

d1=Demo()
d1.myfunction() 
d1.show("riddhi")



#parameterized constructor
class Demo:             
    def myfunction(self):   
       print("function class")

    def show(self,name):
        print("value is",name)

    def __init__(self,nm):         
        print("demo class")
        print("name is",nm)


d1=Demo("xyz")
d1.myfunction() 
d1.show("riddhi")

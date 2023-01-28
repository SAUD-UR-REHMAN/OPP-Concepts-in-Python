################################
##### SIMPLE CLASS METHODS #####
################################ 

# class Student:
#     def pro():
#         print("He is a good student.")
#     def age(self):
#         print("He is 34 yo student.")


# s1 = Student()
# s1.pro()
# s1.age()
# #### OR #####
# Student().age()

##############################################
####### PASSING ARGUMENT AND PARAMETERS ######
##############################################

# class Student:
    
#     def __init__(self,name,age):
#         self.n= name  
#         self.a= age
#         self.school = "Public school"
        
#     def name(self,na):
#         print(f"His name is {na}.& {self.school}")
#     def age(self):
#         print(f"He is {self.a} yo student.")
        
# s1 = Student("saud",20)  
# s1.n = "ali"
# s1.name("saud ur rehman")
# s1.age()
# s2 = Student("muneeb",22)  
# s2.name("muneeb ur rehman")
# s2.age()


#######################################
######### TYPES OF METHODS ############
#######################################


# class Student:
#     school = "Public School"

# #### STATIC METHODS ########
'''Here we will not pass any parameter'''

#     @staticmethod
#     def info():
#         print("this is an info class")

# ##### CLASS METHODS ##########

'''Here we will call a class variable using cls parameter'''
#     @classmethod
#     def schol_name(cls):
#         return cls.school


# ###### INSTANCE METHODS #######

'''This is as simple as a method commonly used'''
#     def prop(self,name,age):
#         print(f"The name is {name}")    
#         print(f"The age is {age}")
#         print(f"The is {self.school}")
        
# s1 = Student()
# s1.info()
# s1.schol_name()
# s1.prop("saud",20)        



#############################################
######## CLASS IN SIDE A CLASS ##############
#############################################

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.lap = self.Laptop() ### Object of the inner class
#     def stu_data(self):
#         print(self.name,self.age)
    
#     class Laptop:
#         def __init__(self):
#             self.brand = "hp"
#             self.core = "i5"
#             self.ram = 8
#         def lap_data(self):
#             print(self.brand,self.core,self.ram)
            
# s1 = Student("saud",20)
# s1.stu_data()
# s1.Laptop().lap_data()                        





#############################################
############### INHERITANCE #################
#############################################
'''
Inheritance in Python is a mechanism that allows a
class to inherit properties and methods from another
class, known as the parent class or superclass. The
class that inherits from the parent class is known 
as the child class or subclass. This allows for code
reuse and reduces the complexity of code by allowing
related classes to share common functionality.
'''

### 1 Multilevel --> inheritence ##########
'''
Multilevel Inheritance is a feature of object-oriented
programming languages like Python where a child class 
inherits from a parent class and the parent class also 
inherits from a grandparent class, and so on. This 
allows for a hierarchical structure of classes where a
subclass can inherit properties and methods from not 
just one parent class, but multiple levels of parent classes.
'''

# ### Class A is a Supper or Parent Class ###
# class A:
#     def fea1(self):
#         print("product1")
#     def fea2(self):
#         print("product2")
# ### Class B is a Supper or Parent Class of C and child class of A ###  
# ### It can access the data of class A ########      
# class B(A):
#     def fea3(self):
#         print("product3")
#     def fea4(self):
#         print("product4")
# ### Class C is a child class of B and grand child class of A ### 
# ### It can access the data of class A and B ########         
# class C(B):
#     def fea5(self):
#         print("product5")
#     def fea6(self):
#         print("product6")

# ### printing output ###        
# s1 = C()
# s1.fea1()
# s1.fea3()
# s1.fea6()        
        
        

#### 2 Multiple --> inheritence ##########
'''
Multiple Inheritance is a feature of object-oriented
programming languages like Python where a class can 
inherit properties and methods from multiple classes,
known as the parent classes or superclasses. This 
allows a class to have multiple behaviors and properties,
which can make the code more flexible and reusable.
'''

# ### Class A is a Supper or Parent Class for C ###
# class A:
#     def fea1(self):
#         print("product1")
#     def fea2(self):
#         print("product2")
# ### Class B is also a Super class or paret class for C ####
# ### B can't access data from outside of itself ###      
# class B:
#     def fea3(self):
#         print("product3")
#     def fea4(self):
#         print("product4")
# ### Class C is a child class of A  ### 
# ### It can access the data of class A and B  ########         
# class C(A,B):
#     def fea5(self):
#         print("product5")
#     def fea6(self):
#         print("product6")

# ### printing output ###        
# s1 = C()
# s1.fea1()
# s1.fea3()
# s1.fea6()


#############################################
############### Super Method ################
#############################################
'''
The super() method in Python is used to call a method
from a parent class. It is typically used in the 
implementation of a child class to call a method that
has been overridden in the child class but also needs 
to make use of the implementation from the parent class.
The super() method can be used in two ways:
1- super().method() - to call a method from the parent class
2- super(ChildClass, self).method() - to call a method from
   the parent class, where ChildClass is the current class 
   and self is the current instance of the class.
'''

# ## Class A is a Supper or Parent Class for C ###
# class A:
#     def __init__(self):
#         print("init of class A")
#     def fea1(self):
#         print("product1")
#     def fea2(self):
#         print("product2")
# ## Class B is a Supper or Parent Class for C ###      
# class B:
#     def __init__(self):
#         print("init of class B")
#     def fea3(self):
#         print("product3")
#     def fea4(self):
#         print("product4")
                
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("init of class C")
#         super().fea1()
#     def fea5(self):
#         print("product5")
#     def fea6(self):
#         print("product6")

# ''' Here the Class A & B both are the super classes
# for class C but C will give priority to the class
# which is given at the left side as C(A,B) ''' 

# s1 = C()        
        
        
        
#############################################
############### Abstraction #################
############# Abstract class ################
#############################################
'''
1- Python by default doesn't allow to creat abstract classes
2- There is a build-in module use which we can creat abstract classes
     ``from abc import ABC,abstractclassmethod``
3- We can't make object fro the abstract class
4- we can't make an object from the child class of the abstract parent class
5- we have to define all the functions in the child class that are defined in abstract parent class
6- There should be atleast one abstract method inside abstract class(otherwise it will not be an abstract class)
7- Abstract class is actually a templet for working.
      
'''
        
# from abc import ABC,abstractclassmethod

# class Student(ABC): 
#     @abstractclassmethod   # this decorator will make the method abstract
#     def atribute(self):
#         pass

# class Data(Student):
#     def atribute(self):
#         print("its working")           

# s1 = Data()
# s1.atribute()



#############################################
############### Polymorphism ################
#############################################

''' 
1- The ability of a function or method to work with multiple type of inputs.
2- Same function will work with different inputs.
3- it has following types.........
+ Operator overloading
+ Fuction/Method overloading
+ Fuction/Method overriding
+ Duck Typing

'''

#############################################
########### Operator overloading ############
#############################################
'''
1- when evre we are adding,subracting,multipying two number
or perform different operation.Behind the seen we are 
actually calling some functions.
2- Here in operator overloading the same operator method 
   is used with diffrent types of parameters
'''
# # when we add a + b like this
# a = 5
# b = 6
# print(a+b)
# '''behine the seen actally we are calling a function __add__(self,other)'''
# print(int.__add__(a,b))

# '''Now both the print results are same'''

# """ The problem comes when we add a string to and integer """
#                        # like
                       
# c = 5
# d = '6'
# print(int.__add__(c,d)) 
# #OR
# print(c + d)   


""" THE CONCEPT COMES WHEN WE ARE WORKING WITH CLASSES """

'''step-1'''
##
# class Student:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
# s1 = Student(2,4)
# s2 = Student(6,8)

# #now if we do like
# print(s1 + s2)

'''step-2'''
##
# class Student:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     # make a function for addition
#     # this is called operator ovrloading as we can use it as we want
#     #Different types of attributes are passed and same working is performed
#     def __add__(self,other):
#         a = self.a + other.a
#         b = self.b + other.b   
#         r = Student(a,b)
#         return r
        
# s1 = Student(2,4)
# s2 = Student(6,8)
# # 
# ##### OR #######
# #
# s1 = Student("saud","muneeb")
# s2 = Student("rehman","rehman")

# r = s1 + s2
# print(r.b)



#############################################
######## Fuction/Method overloading #########
#############################################


''' 
1- This concept is same as operator overloading.
2- In this case a function with same name is used
for diffrent number of arrguments.
'''

'''Expalination with example'''
'''This will give an error if two arguments are given'''

# class Calculater:
#     def sum(self,a,b):
#         r = a+b
#         print(r)
#     def sum(self,a,b,c):
#         r = a+b+c
#         print(r)
    
# s1 = Calculater()    
# s1.sum(2,3)


''' Now the method or function overloading can be performed by This method'''
######### Method is ########

# class Calculater:
#     def sum(self,a=None,b=None,c=None):
#         if a != None and b != None and c != None:
#             r = a + b + c
#         elif a != None and b != None :
#             r = a + b
#         else:
#             r = a        
#         return r
    
# s1 = Calculater()
# ### here you can pass 1, 2 or 3 arguments as you wish    
# print(s1.sum(2))




#############################################
######### Fuction/Method overriding #########
#############################################
'''
Method overriding is an ability of any object-oriented
programming language that allows a subclass or child
class to provide a specific implementation of a method
that is already provided by one of its super-classes or
parent classes. When a method in a subclass has the same name,
same parameters or signature and same return type(or sub-type)
as a method in its super-class, then the method in the subclass
is said to override the method in the super-class.
'''

# class Parent:
#     def __init__(self):
#         print("init in parent class")
#     def show(self):
#         print("functionin parent class")
# class Child(Parent):
#     def __init__(self):
#         print("init in child class")  
            
# obj1 = Child()
# obj1.show() 
  
  
#############################################
################ Duck Typing ################
#############################################             

'''
Duck Typing is a term commonly related to dynamically
typed programming languages and polymorphism. The 
idea behind this principle is that the code itself 
does not care about whether an object is a duck, but
instead it does only care about whether it quacks.
e.g.
If it walks like a duck, and it quacks like a duck, then it must be a duck.
'''

# class Duck:
#     def quak(self):
#         print("Duck is quaking")
# class Cat:
#     def quak(self):
#         print("I'm mewoing but i can also quak")

# def sound(obj):
#     obj.quak()
    

# sound1 = Duck()
# '''OR'''
# sound1 = Cat()
# ''' 
# In both the cases the output will be printed
# bcoz the function sound will not take care of
# what an object actaully is. it will just call
# the function if it is present in the class.
# AND THAT'S CALLED DUCK TYPING.
# '''

# b = sound1
# # print(b)
# sound(b)
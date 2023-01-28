################################
##### SIMPLE CLASS METHODS #####
################################ 

class Student:
    def pro():
        print("He is a good student.")
    def age(self):
        print("He is 34 yo student.")


s1 = Student()
s1.pro()
s1.age()
#### OR #####
Student().age()

##############################################
####### PASSING ARGUMENT AND PARAMETERS ######
##############################################

class Student:
    
    def __init__(self,name,age):
        self.n= name  
        self.a= age
        self.school = "Public school"
        
    def name(self,na):
        print(f"His name is {na}.& {self.school}")
    def age(self):
        print(f"He is {self.a} yo student.")
        
s1 = Student("saud",20)  
s1.n = "ali"
s1.name("saud ur rehman")
s1.age()
s2 = Student("muneeb",22)  
s2.name("muneeb ur rehman")
s2.age()


#######################################
######### TYPES OF METHODS ############
#######################################


class Student:
    school = "Public School"

#### STATIC METHODS ########

    @staticmethod
    def info():
        print("this is an info class")

##### CLASS METHODS ##########

    @classmethod
    def schol_name(cls):
        return cls.school

###### INSTANCE METHODS #######

    def prop(self,name,age):
        print(f"The name is {name}")    
        print(f"The age is {age}")
        print(f"The is {self.school}")
        
s1 = Student()
s1.info()
s1.schol_name()
s1.prop("saud",20)        



#############################################
######## CLASS IN SIDE A CLASS ##############
#############################################

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    def stu_data(self):
        print(self.name,self.age)
    
    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.core = "i5"
            self.ram = 8
        def lap_data(self):
            print(self.brand,self.core,self.ram)
            
s1 = Student("saud",20)
s1.stu_data()
s1.Laptop().lap_data()                        





#############################################
############### INHERITANCE #################
#############################################

### 1 Multilevel --> inheritence ##########

### Class A is a Supper or Parent Class ###
class A:
    def fea1(self):
        print("product1")
    def fea2(self):
        print("product2")
### Class B is a Supper or Parent Class of C and child class of A ###  
### It can access the data of class A ########      
class B(A):
    def fea3(self):
        print("product3")
    def fea4(self):
        print("product4")
### Class C is a child class of B and grand child class of A ### 
### It can access the data of class A and B ########         
class C(B):
    def fea5(self):
        print("product5")
    def fea6(self):
        print("product6")

### printing output ###        
s1 = C()
s1.fea1()
s1.fea3()
s1.fea6()        
        
        

#### 1 Multiple --> inheritence ##########

### Class A is a Supper or Parent Class for C ###
class A:
    def fea1(self):
        print("product1")
    def fea2(self):
        print("product2")
### Class B is also a Super class or paret class for C ####
### B can't access data from outside of itself ###      
class B:
    def fea3(self):
        print("product3")
    def fea4(self):
        print("product4")
### Class C is a child class of A  ### 
### It can access the data of class A and B  ########         
class C(A,B):
    def fea5(self):
        print("product5")
    def fea6(self):
        print("product6")

### printing output ###        
s1 = C()
s1.fea1()
s1.fea3()
s1.fea6()


#############################################
############### Super Method ################
#############################################


## Class A is a Supper or Parent Class for C ###
class A:
    def __init__(self):
        print("init of class A")
    def fea1(self):
        print("product1")
    def fea2(self):
        print("product2")
## Class B is a Supper or Parent Class for C ###      
class B:
    def __init__(self):
        print("init of class B")
    def fea3(self):
        print("product3")
    def fea4(self):
        print("product4")
                
class C(A,B):
    def __init__(self):
        super().__init__()
        print("init of class C")
        super().fea1()
    def fea5(self):
        print("product5")
    def fea6(self):
        print("product6")

''' Here the Class A & B both are the super classes
for class C but C will give priority to the class
which is given at the left side as C(A,B) ''' 

s1 = C()        
        
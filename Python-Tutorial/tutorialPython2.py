a,b=5,7
#simple if else
if a==b:
    print(a,b)
elif a>b:
    print(a)
else:
    print(b)

print(a) if a>b else print("b")
#a while loop
i=0
while i<5:
    print(i)
    i+=1
else:
    print(f"i is {i}")
    
# simple function

def myFunction(arg1,arg2):
    print(arg1,arg2)
    
#function with ambigious number of arguments
    
def argumentFunc(*args):
    print(args)

argumentFunc(1,2,3,4,5,6,7)        

#functions with KeyWord arguments
def kwfunc(**kwargs):
    print(kwargs)
    print(kwargs['first'])
kwfunc(first=1,second=2)

#lambda function is used for anonymous short function usually inside another functions
x = lambda a, b, c : a + b + c #x is name of lambda function args:operations
print(x(5, 6, 2))

#Class

class myClass: #class name
    myClassAttribute = "something" #class attribute not belong no any object

    def __init__(self,value): #object attribute assignment--self is reference to object itself
        self.value=value #writing like this is preferred
        self.actualthing =value #this writing is acceptable- actualthing is real attribute of object-value is just a variable 
    def __str__(self): #__str__ is function to control what to print with string
            return f"{self.value}+{myClass.myClassAttribute}"

obj1 = myClass(123)
print(obj1)


#inheritance

class childClass(myClass): #to create parent child class 
    def __init__(self, value, value2):
        self.value=value
        self.value2=value2
        
        
















        
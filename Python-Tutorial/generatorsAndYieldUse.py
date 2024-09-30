#generator and yield use

def generatorFunc(n): #generators return single value at a time instead of computing everthing at once
    yield n**2 #yield is statement works similiar to return -instead of ending function call like return we can use yield to continue to running 
    yield n**3
    print("End of function")
    
#generators are iterable this means code below is returns generators address 
print(generatorFunc(2))

#to access values we need code similiar like below 
for value in generatorFunc(2):
    print(value)
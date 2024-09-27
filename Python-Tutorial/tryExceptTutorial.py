#Error and exception handling
a=10 #int 10 a
b="10" #str 10 b

try: #we try to catch error in this block
    print(a+b) #codes can cause error
except TypeError: #if we can predict type of error we can write like this
    print("TypeError Occurred") #do things after this error type

except: #for general unpredictable error types
    print("any other undefined error")#do things for this 
else: #else statement can be used here
    print("Else can be used")
finally: #this block always runs use is up to you
    print("This one always run") #stuff to do
    
#simple try except code is like above 
#a real world problem use
#we ask a input from user and its needed to checked

def askNumber(): #♪function definition
    while True: #while loop-be careful about while True blocks it needs to break keyword otherwise it runs forever
        try: #try block
            inputNum=int(input("Please Enter a Number: "))#we ask an input from user and convert input to int if input is wrong it causes error
        except:#excep block for error
            print("Please Enter Correct Number!") # print to inform user input is incorrect
            continue #ends current iteration and begin next one
        else:#if user entered correctly we can provide feedback and make other operations
            print("Thx for Correctly entering")
            return inputNum
            break #! ! ! Very important for while True loops ! ! !
        finally: #optional
            print("finally code block executed")
            
askNumber() #call function

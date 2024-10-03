'''
Main Purpose of decorators are extending functions functiolity
decorator is wrapping an original old function to a new function
point of decorator is if an origina old functions inside code cant be changed or changing will cause serious errors
decorators are used imstead of changing original old function
'''
#Tutorial Decorator

def decoratorFunction(Func): #decorator functions take another function as parameter watch out for ()
    
    def wrappingFunc():  #our wrapping function inside of decorator function real thing done here
        print("Top of box") #things to do before original function runs 
        
        Func() #call parameter function
        
        print("Bottom of Box") #things to do after original function runs
        
    return wrappingFunc() #Watch out for scope if this line written inside of wrapper nothing happens


def originalFunc(): #original old function
    print("This is original Function")#there is codes problematic to change 
    print("Think this as a gift like jewelry itself") 
    


decoratorFunction(originalFunc) #call function without @

print("") #empty line to seperate below

'''

Example above is normal version of decorator use they can used without @
to use with @ just write @decoratorFunctionsName above original function
for this example it should be like below

@decoratorFunction
def originalFunc(): #original old function
    print("This is original Function")#there is codes problematic to change
    print("Think this as a gift like jewelry itself") 

Note: decorator funtions usually written after original function  
to run decorator functions they have to written top of original function
'''
#a real world example should be like below

def zeroDivisionGuard(function): #decorator function we will use this to prevent error
    def innerFunction(x,y): #wrapper function
        if y==0: # if statement to check is divisor(y) zero 
            return "Cannot divided by 0" #return statement if y is zero
        return function(x,y) #otherwise everything is normal here call function normally
    return innerFunction #call wrapper function inside of decorator function

@zeroDivisionGuard #decorator function applied to below function
def divide(x,y): #simple divident/divisor function if divisor is zero zerodivision error occurs
    return x/y # return result

#note: with use of @ functions can be called normally unlike above 
print(divide(4, 2))
print(divide(5, 0))



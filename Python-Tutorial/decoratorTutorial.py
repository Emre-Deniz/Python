'''
decorator is wrapping an original old function to a new function
point of decorator is if an origina old functions inside code cant be changed or changing will cause serious errors
decorators are used imstead of changing original old function
'''
def originalFunc(): #original old function
    print("This is original Function")#there is codes problematic to change
    print("Think this as a gift like jewelry itself") 
    
def decoratorFunction(originalFunc): #decorator functions take another function as parameter watch out for ()
    
    def wrappingFunc():  #our wrapping function inside of decorator function real thing done here
        print("Top of box") #things to do before original function runs 
        
        originalFunc() #call original function
        
        print("Bottom of Box") #things to do after original function runs
        
    return wrappingFunc() #Watch out for scope if this line written inside of wrapper nothing happens

decoratorFunction(originalFunc) #call function
#module creating tutorial

def myModuleFunc(): #just a normal function
    print("myModuleFunc is called")
    print("This Function from myTutorialModule.py")

    if __name__ =="__main__": #checking- is this file running directly or imported
        print("we are running myTutorialModule.py not imported")
    else:
        print("myTutorialModule.py is imported")
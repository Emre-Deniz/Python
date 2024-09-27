#to use our modules
#we need to describe module and function like this and they need to be in same directory(folder) unless they are packages
from myTutorialModule import myModuleFunc
myModuleFunc()

#we can create packages- folders contain __init__.py file registered as package folders and contents are become accessible

from MainPackageFolder.mainPackageScripts import myMainPackageFunc #we can use like above
myMainPackageFunc() 

from MainPackageFolder.SubPackageFolder import subPackageScripts #or we can use like this 
subPackageScripts.mySubPackageFunc()

# __name__ is for checking which module or script used right now
if __name__ =="__main__": # __main__ is means we are in our main running file
    print("we are using moduleTutorial.py not imported")
else:
    print("moduleTutorial.py is imported") 
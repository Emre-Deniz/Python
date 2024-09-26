# this is a comment line
"""
this is
can be used for
multiline 
comment
"""

#---Variables

#Python variables becomes created at the moment you assing a value and type can be changed easyly with another type assignment
x = 5

print(type(x)) # x is integer now- type is used to check variables type -print is used to print data on screen

x='Hello' # x is string now

# With casting we can specify type of variable
x = int(12)

# after casting x is permanently int and cant converted to other types like above

#single or double quotes doesnt matter
string="str"
STRING='str'
print(string)
print(STRING)

#both will write str also variable naames are case sensitive

#multiple values
x,y,z, = "car","tire","black"
print(x)
print(y)
print(z)
#prints strings
a=b=c=3
print(a)
print(b)
print(c)
#prints 3 3 3

good,day="Good","day"
print(good,day)
print(good+day)
# + in strings combines them watch out for space

#User inputs
print("Type Please")
userinput=input()
print("you typed",userinput)


#Strings

myStr="Greetings"
print(myStr[0])
for i in range(len(myStr)):
    print(myStr[i])
    
#instead of above

for s in myStr:
    print(s)
# to check strings contain some substring we use "in" for otherwise "not in"
print("ings" in myStr)
print("ings" not in myStr)

#Slicing
helloworld=" Hello World! "
print(helloworld[:6]) #0 to 6 index 6th index not included
print(helloworld[6:]) #6 to end
print(helloworld[6:-1])#6 to reverse index 1
print(helloworld[0:len(helloworld):2]) # 2 step

#String modifications
print(helloworld.upper()) #all uppercase
print(helloworld.lower()) #all lowercase
print(helloworld.strip()) #remove selected chars-whitespace for this one 
print(helloworld.replace('e','o')) #replace e with o
print(helloworld.split('W')) #split with choosen char-removes choosen char from result

#f strings
age=36
sometext=f"Bob is {age-6} years old"
print(sometext)

#filtering
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"] #removes apple

print(newlist)

#tuples cant be changed to operate on them first convert to a list and make changes after that convert back to tuple however you can concatenate 2 string tuples
aTuple=("string",3,  3.14,  True)
thisTuple=("apple","orange","banana")
toAddTuple=("car",) #single item tuple watch out for ,
thisTuple=thisTuple+toAddTuple
print(thisTuple)

#tuple unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

thisSet={"a","b","c"}
#sets cant contain duplicates 1 and true is a duplicate 0 and false too
#sets are random everytime and havent indexing
thisSet.add("d")
print(thisSet)
thatSet={"z","x"}
thisSet.update(thatSet)
print(thisSet)
thisSet.remove("c") #if element-c- not in the set error occurs use discard() instead
print(thisSet)
popped=thisSet.pop() #removes random element
print(popped)

#There are several ways to join two or more sets in Python.
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.

#Dictionary: Stores data with key:value  pairs
exampleDict={
    "name":"John",
    "age":55,
    "drives":True
    }
#no duplicates with same key last one will remain if there is any
print(exampleDict["name"]) #a way to gel values
print(exampleDict.get("name")) #another way to get a value
print(exampleDict.keys()) #writes all keys
print(exampleDict.values()) #writes all values
print(exampleDict.items())#writes key:value pairs

exampleDict["age"]=56 #changes value also update() can be used
exampleDict["surname"]="Brown"#add key:value pair-update)() can be used
print(exampleDict)

if "age" in exampleDict: print("yes")
    
exampleDict.pop("age") #removes item by given key      
print(exampleDict)
exampleDict.popitem() #removes last added item
print(exampleDict)
del exampleDict["drives"] #another way to remove item
print(exampleDict)

#beware del can delete dictionary itself if [] not used and can causes errors   
#clear() empties dictionary unlike del keyword

# dictionary2=dict1 means referancing not copying dictionary
#to copy dictionary dict2=dict1.copy() or dict2=dict(dict1)

#dictionaries can be nested(written in eachother)

















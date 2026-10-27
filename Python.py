##This is a python crash course 
#This is everything that was covered in Bro code crash course
print("My favourite food is pilau")
print("Na ni tamu ajab")
# This is my first python program
#variables
full_name = "Emmanuel Ochibo"
age = 19
gpa = 4.0
is_student = True


print(f"Hello {full_name}")
print(f"You are {age} years old")
print(f"Your gpa is {gpa}")
print(f"Are you a student?{is_student}")

if (is_student):
    print("You are going to be great")
else:
    print("You are going to be great regardless")

#arithmetic 
# remainder use %
# // use this while dividing to get the whole number
# / use this to just divide and get whatever you were meant to get

cars = 5
friends = 22
remaining_friends = friends % cars
print(f"Each car will have to carry a total of {friends // cars}")
#augumented assignment operators
#instead of writing something like this 
# x = x +1    do this instead x += 1
print(f"After settling comfortably the remaining friends were {remaining_friends}")
 # typecasting = the process of converting one data type to another
 # int() = converts to an integer
 #float() = converts to a floating point number
 #bool() = converts to a boolean value
# to get the type of variable use type() function

print(f"The type of variable full_name is {type(full_name)}")
gpa_1 = int(gpa)
print(f"The type of variable gpa is {type(gpa_1)}")
print(f"Gpa:{gpa}")
print(f"Gpa_1(The edited gpa into an integer):{gpa_1}")
#accepting user input

name = input("What is your name?")
print(f"Hello {name}")

# The next lesson is on if statements
# if statements are used to make and allow basic decision-making 
# Can only be executed iff the condition is true
if age >= 18:
    print(f"You can drive the vehicle")
elif age <= 18:
    print(f"You cannot drive a car")
else:
    print(f"What are you ?")
# The order of your if and elif statements matter alot.Let the larger one or the one with a  higher priority come first before the one with a lower priority



#The next statements will be on logical operators
# or = at least one of the conditions must be true
# and = both conditions must be true
# not = reverses the result of the condition(Not False,not true)

temp = int(input("What is the temperature outside?"))
if temp <= 30:
    print(f"It is cool outside")
else:
    print(f"It is not really cool outside")
# while loop used to repeat a certain block of code as long as the condition is true
#       we re-check the condition at the end of each iteration
#       if the condition is false we exit the loop and continue with the rest of the code
#for loop used to iterate over a sequence of elements(strings.list, tuples and sets)
#     repeats a block of code an exact number of times
# if statements iterate only once while while loops iterate until thee condition becomes false

sex = input("What is your sex?")
while sex =="":
    sex = input("What is your sex?")

for i in range(1,11) :
    print( i ,"I just means index but programmers just use i")
# syntax for a for loop >>>> for index in range(start,stop,step/increment):
import time
for i in range (10,0,-1):
    print(i)
    time.sleep(1)

#List [] = mutable, most flexible
#Tuple() immutable,faster
# Set{} = mutable(add/remove), unordered,
#          NO duplicates, best for membership testing

# variables can only contain one item while a list contains more than one
# for example

fruits =["apple" , "orange" ,"banana", "coconut"]
print(fruits[0]) # it will print the first thing in your list of list
for fruit in fruits:
    print(fruit, end=" ")
# You can also change the elements in the list at will....This is why it is said to be flexible
# For example:
#I want to change the initial fruit in Fruits to be a mango not an apple
fruits[0] = "mango"
print(f"{fruits[0]}")
fruits.append("mango")
print(f"{fruits}")
fruits.remove("banana")
print(f"{fruits}")
fruits.pop(0)
print(f"{fruits[0]}")
fruits.clear()
print(f"{fruits}")

#Tuple()= imutable and faster. This is because you cannot change anything once it has been written innit
#Another difference is that it is covered in a () unlike list covered in []
#Does not allow assignment...it cannot be changed once written
#Good while writing a set of value that does not need to be changed


#Sets{}.....From the beginning statement it seems to be the most difficult in this case
#sets can be added or removed,,does not support assignment of since it is unordered and does not allow duplicates......best used for membership testing
search = input("What fruit are you looking for")
if search in fruits:
    print(f"{search} was found")
else:
    print(f"{search} is not found")
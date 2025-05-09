# Inputs and Loops
# Keanu Kesha
# Date: 9 may 2025
# Version 2.0

# Ask the user a question and store their answer in a variable
# ask the user for their name and store it
name = input("Hello, what is your name? ") #store answer as string
print()# this adds a line break
print(f"Nice to meet you {name}\n")
# ask the user for two numbers then add them together
num1 = int(input("what is your first number please? ") )
num2 = int(input('what is your second number? ') )
print (f"if you entered your first number as {num1}\n")
print (f"if you entered your first number as {num2}\n")

# adding the two numbers together
sum = num1 + num2 
print (f"Your number is {sum} because {num1}+{num2}={sum}\n")

#multiplying the two inputs together
multiply = num1 *  num1
print(f"The two numbers multiplied together will result in {multiply}\n")

#test that the imput is stored correctly
print (name)
# to comment code out use ctrl + / 

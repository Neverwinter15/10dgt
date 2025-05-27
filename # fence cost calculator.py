# Fence cost calculator
# resycled chocolate milk program

        
def num_check(question):
    error = "please enter a number more then zero\n"
    while True:

        try:
            #ask user for number
            response = float(input(question))
    # check number is more then zero
            if response > 0: 
                return response
            else:
                print("enter number more then zero")

        except ValueError:
            print(error)
# Questions to ask user
keep_going = ""
while keep_going == "": 
    width =  num_check("Give me the width of the object in metres ")
     # to call(use a function write it's name)
    length = num_check("Give me the length of the object in metres ")
    print()
    cost = num_check("Give me the cost per metre $")
    print()
    # adding responses together
    perimeter = 2 * (width + length)
    print (f"The perimeter is {perimeter}m ")
    # multiply the responses
    print()
    perimeter_cost = 2 * (perimeter + cost)
    
# print responses
    print(f"The cost to build your fence is ${perimeter_cost}.")
    keep_going = input("would you like to continue? press enter to do this again or any key to quit ") 
    print()
print("thank you for using this calculator")
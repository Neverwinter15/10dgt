# area and peremiter code
# ask user for width and loop
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
            # video 5



# main routine

keep_going = ""
while keep_going == "":


# get width and height
    width = num_check("width: ")
    print (width)
    height = num_check("height: ")
    print(height)
    #  calculate area and perimeter

    area = width * height
    perimeter = 2 * (width+ height)

#output area and perimeter
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

#ask user if they want to keep going

    keep_going = input("press enter to keep going or any key to quit. ")
print("thank you for using our calculator")






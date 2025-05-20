# area and peremiter code

def num_check(question):
      while True:  

            try:
                # ask user for number
                response = float(input(question))
                # check number is more then zero
                if response > 0:
                        return response
                else:
                    print("please enter a number that is more then zero\n")

            except ValueError:
                print("Error")

            # video 5



# main routine
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()
 
for item in range(0, 2):
     height = num_check("height: ")
     print (height)

# calculate the area/ perimeter
area = (width * height)
perimeter = (width + width) + (height + height)
# output the area and perimeter and area
print(f" The area is {area}")
print(f"The perimeter is {perimeter}")
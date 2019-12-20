import sys
from datetime import datetime
# 1. Write a Python program to print the following string in a specific format
# (see the output).
# Twinkle, twinkle, little star,
#   How I wonder what you are!
#       Up above the world so high,
#       Like a diamond in the sky.
# Twinkle, twinkle, little star,
#   How I wonder what you are
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# 2. Write a Python program to get the Python version you are using
print("Current Python version is: ", sys.version)


# 3. Write a Python program to display the current date and time.
print("Date and time is: ", datetime.now())


# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
rad = int(input("enter radius of circle: "))
print(3.14*rad**2)
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
fullName = firstName+lastName
for i in fullName[::-1]:
    print(i ,end=" ")


# 6. Write a python program which takes two inputs from user and print them addition
input_one = input("Enter First Input: ")
input_two = input("Enter Second Input: ")
print(input_one + input_two)
#

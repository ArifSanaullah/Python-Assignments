# Question:1
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def isPositiveInteger(number):
    if int(number) > 0 :
        return True
    else:
        return False
def calcFactorial(number):
    factorial = 1
    if isPositiveInteger(number) == True:
        number = int(number)
        for i in range(1, number + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("Invalid input")

factCalc = input("Enter Number to calculate it's factorial: ")
calcFactorial(factCalc)



# Question:2
# Write a Python function that accepts a string and calculate the number of upper
# case letters and lower case letters.

# def caseCounter(string):
#     upper = 0
#     lower = 0
#     standardString = 'abcdefghijklmnopqrstuvwxyz'
#     for letter in string:
#         for sampleLetter in standardString:
#             if letter == sampleLetter:
#                 lower += 1
#             elif letter == sampleLetter.upper():
#                 upper += 1
#             else:
#                 print("Invalid input")
#     print("Upper Case Letter in the String are: {},\nLower Case letters in the String are: {}".format(upper, lower))
# string = input("Enter Any CamelCase String: ")
# caseCounter(string)



# Question:3
# Write a Python function to print the even numbers from a given list.

# randomList = [2, 3, 23, 54, 45, 23, 78, 56, 99, 24]
# for element in randomList:
#     if element % 2 == 0:
#         print(element)



# Question:4
# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same
# backward as forward, e.g., madam

# def isPalindrom(palWord):
#     firstHalf = []
#     secondHalf = []
#     if len(palWord) % 2 == 1:
#         oddList = (len(palWord) // 2)
#         for element in range(oddList):
#             firstHalf.append(palWord[element])
#         for element in range(-1, -(len(palWord)-oddList), -1):
#             secondHalf.append(palWord[element])
#     else:
#         print("Not palindrom Word")
#     palindrom = False
#     for element in range(len(firstHalf)):
#         if firstHalf[element] == secondHalf[element]:
#             palindrom = True
#     if palindrom == True:
#         print("{} is a Palindrom".format(palWord))
#     else:
#         print("Not a palindrom")
# palWord = input('Enter any word: ')
# isPalindrom(palWord)



# Question:5
# Write a Python function that takes a number as a parameter and check the
# number is prime or not.


# def isPositiveInteger(number):
#     try:
#         number = int(number)
#         return True
#     except:
#         return False

# def checkPrime(number):
#     isPrime = isPositiveInteger(number)
#     if isPrime:
#         number = int(number)
#         for i in range(2, number):
#             if (number % i == 0):
#                 print("Not a prime Number")
#                 print("{} times {} is a {}.".format(i, number // i, number))
#                 break
#         else:
#             print("{} is a prime number.".format(number))
#     else:
#         print("Enter positive integers only")
# number = input("Enter any number: ")
# checkPrime(number)



# Question: 6
# Suppose a customer is shopping in a market and you need to print all the items
# which user bought from market.
# Write a function which accepts the multiple arguments of user shopping list and
# print all the items which user bought from market.
# (Hint: Arbitrary Argument concept can make this task ease)

# def shoppingList(*items):
#     shoppingItems = []
#     while True:
#         item = input("Enter Shopping item [-1 to abort]: ")
#         if item != '-1':
#             shoppingItems.append(item)
#         else:
#             break
#     for item in range(len(shoppingItems)):
#         print("You purchased: {}".format(shoppingItems[item]))
# shoppingList()

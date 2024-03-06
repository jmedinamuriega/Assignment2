FINISH='''
------------------------------------------
           Exercise divider
------------------------------------------
'''

# # # Task 1: Code Correction
# # # You are provided with a Python script that uses conditional statements to
# tell if a number is positive, 
# negative, or zero, but it has some errors. Identify and fix them.

# # # Buggy Code:


# # # number = input("Enter a number: ")
# # # if number > 0:
# # #     print("The number is positive.")
# # # elif number = 0:
# # #     print("The number is zero.")
# # # else number < 0:
# # #     print("The number is negative.")

number = input("Enter a number: ")
if int(number) > 0:
    print("The number is positive.")
elif int(number) == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
print(FINISH)
# # # 2. The Story Brancher
# # # Task 1: Code Correction
# # # You are provided with a Python script that uses if-else structures for a story branching mechanism. There are some errors in the code. Identify and correct them.

# # # Buggy Code:


# # # choice = input("Do you choose the path to the left or right? ")
# # # if choice = "left":
# # #     print("You find a treasure chest!")
# # # elif choice = "right":
# # #     print("You encounter a dragon!")
# # # else:
# # #     print("Invalid choice!")
# # # 3. The Greatest Showdown
# # # Objective:
# # # Harness the power of conditional statements to compare and determine values.

choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

    
print(FINISH)
#The Greatest Showdown


# # # Task 1: Identify the Greatest
# # # Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.
# # # Task 2: Identify the Smallest
# # # Extend your program from Task 1 to also determine the smallest number among the three and print it out.

# # # Task 3: Equality Check
# # # Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".

print("select three numbers")
number1, number2, number3 =input("number 1:"),input("number2:"),input("number3:")
output=(" is the largest number")
list1=number1, number2, number3
print("the smallest number is "+ min(list1))
if int(number1)>int(number2) and int(number1)>int(number3):
    print(number1+output)
if int(number2)>int(number1) and int(number2)>int(number3):
    print(number2+output)
if int(number3)>int(number2) and int(number3)>int(number1):
    print(number3+output)
if int(number3)==int(number2)==int(number1):
    print("the three values are the same")
elif int(number3)==int(number1) or int(number3)==int(number2) or int(number2)==int(number1):
    print("two values are the same ")


print(FINISH)

# # # 4. Leap Year Explorer
# # # Objective:
# # # Dive deep into the intricacies of the calendar by exploring the concept of leap years.
# # # Task 1: Leap Year Checker
# # # Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

# # # Task 2: Century Verification
# # # Add functionality to your program from Task 1 to inform the user if the entered year is a century year (e.g., 1900, 2000) regardless of whether it's a leap year or not.

# # # Task 3: Time Traveler
# # # Enhance your program to indicate if the provided year is in the future, past, or is the current year, compared to the a year variable year=2020.

year=input("please put a year:")
if int(year)==int(2020):
    print("actual year")
elif int(year)<2020:
    print("that is in the past")
elif int(year)>2020:
    print("that is in the future")
if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print("is a leap year")
if int(year)%100==0:
    print("a century year")
else:
    print("not a leap year")
print('''
-----------------------------------------------------------------
that's the end of the asignment i hope u are having a good shift!
-----------------------------------------------------------------
''')
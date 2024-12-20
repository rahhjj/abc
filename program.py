# 7 marks from ts in final exam
print("hellow world")
'''
a = "python"
b = a.upper()
print(b)

a = "pYtHOn"
b = a.lower()
print(b)

a = "pYtHOn"
b = a.capitalize()
print(b)

a = "pYtHOn is a real nigga"
b = a.title()
print(b)

a = "pYtHOn is a real nigga"
b = a.swapcase()
print(b)

a = "pYtHOn"
b = a.center(10, '*') # can only pass 2 arguements first integer then others separated with comma
print(b) # do len of string - integer to find out how mnay spaces in both sides. 
         # for lhs (n+1)/2 for rhs (n-1)/2 in the case n is a odd number
        
        
a = "pYtHOn is a real nigga"
b = a.count('a')
print(b)

# find, rfind, index, rindex
# output **python**, *python, python*
a = 'python'
b = a.center(9, '*')
print(b)

a = 'python'
b = a.rjust(7, '*')
print(b)

a = 'python'
b = a.ljust(7, '*')
print(b)


# Example 1: Using maketrans and translate
a = "123abc"
b = a.maketrans("123", "abc")  # Creating a translation table
print(a.translate(b))  # Translating the string based on the table

# Example 2: maketrans but same input and output
a = "123abc"
b = a.maketrans("abc", "abc")  # Translation table where nothing changes
print(b)  # Printing the translation table (a dictionary)

# Example 3: maketrans with uppercase and lowercase mismatch
a = "123abc"
b = a.maketrans("Ab", "Ab")  # Incorrect as 'Ab' differs from lowercase 'a' and 'b'
print(b)

# Example 4: Checking startswith
a = "123abc"
b = a.startswith("23")  # Returns True/False
print(a)

# Example 5: Checking endswith
a = "123abc"
b = a.endswith("ab")  # Returns True/False
print(b)

# Example 6: Endswith for character comparison
a = "123abc"
b = 'a'.endswith("c")  # Returns False
print(b)


# Example 7: Using replace
a = "123abc"
print(a.replace('a', "1"))  # Replaces 'a' with '1'




print('{} {a} {}'.format('hello','programmer', a = 'python'))
a = 'python'
print(F'hello {0} {0}')


print('hello {} {} {}'.format(10, 20, 30, a = 40))

a = "python"
print('a'.isidentifier())

a = 213
b = 198
print(a ^ b)

a = 2j
print(a.imag, a.real)


s = '{1} is {0} years old.' .format(25, 'Bob')
print(s)

a = 'python programming'
print('yh' in a)


a = 'python'
b = 'programming'
print('{0} {0} {0}' .format(a,c = '10',b))

feb 17 phase test

enter_day = input("enter the number for day comparison")
if enter_day == 1:
    print("day is sunday")
elif enter_day == 2:
    print("enter day is monday")
elif enter_day == 3:
    print("enter day is tuesday")
elif enter_day == 4:
    print("enter day is wednesday")
elif enter_day == 5:
    print("enter day is thursday")
elif enter_day == 6:
    print("enter day is friday")
elif enter_day == 7:
    print("enter day is saturday")
else:
    print("number doesnot matches day")
    


# Question no. 1
# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".


a = int(input("enter first number"))
b = int(input("enter second number"))

if a == b:
    print("since a is equal to b it will print 1")
elif a > b:
    print("since a is greater than b it will print 2")
else:
    print("since the above conditions doesnot satisfy it will print 3")
    
# nested if else 6 marks


# question no 2
user_input = int(input("enter the number to be checked"))

remainder = user_input % 2

if remainder == 0:
    print("user input is an even number")
else:
    print("user input is an odd number")


# question no 3
number = int(input("enter number between 1 to 12:"))

if number == 1:
    print("It's January")
elif number == 2:
    print("It's Feburary")
elif number == 3:
    print("It's March")
elif number == 4:
    print("It's April")
elif number == 5:
    print("It's May")
elif number == 6:
    print("It's June")
elif number == 7:
    print("It's July")
elif number == 8:
    print("It's August")
elif number == 9:
    print("It's September")
elif number == 10:
    print("It's October")
elif number == 11:
    print("It's November")
elif number == 12:
    print("It's December")
else:
    print("ERROR! Please enter number within range")

# question no 4

raw_percentage = float(input("enter your perentage:"))

if raw_percentage < 25:
    print("your percentage grade is a F!")
elif raw_percentage >= 25 and raw_percentage < 45:
    print("your percentage grade is an E!")
elif raw_percentage >= 45 and raw_percentage < 50:
    print("your percentage grade is an D!")
elif raw_percentage >= 50 and raw_percentage < 60:
    print("your percentage grade is an C!")
elif raw_percentage >= 60 and raw_percentage < 80:
    print("your percentage grade is an B!")
elif raw_percentage >= 80:
    print("your percentage grade is an A!")
 
    
# question no 5

number = int(input("enter the number:"))
remainder = number % 7
if remainder == 0:
    print("Given input is divisible by 7")
else:
    print("Given input is not divisible by 7")


# question no 6
number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == '+':
    result = number1 + number2
    print("Your Answer is:", result)
elif operator == '-':
    result = number1 - number2
    print("Your Answer is:", result)
elif operator == '*':
    result = number1 * number2
    print("Your Answer is:", result)
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
        print("Your Answer is:", result)
    else:
        result = "Mathematical error (value tends to infinity)"
else:
    print("Invalid operator")

# question no 7

number= float(input("enter our number: "))
remainder = number % 5

if remainder == 0:
    print("Hello")
else:
    print("Bye")

#question no 8

number = int(input("enter the number: "))

if (number % 3 == 0 and number % 5 == 0):
    print(" FizzBuzz")
elif (number % 3 == 0 and number % 5 != 0):
    print("Buzz")
elif (number % 3 != 0 and number % 5 == 0):
    print("fizz")
elif (number % 3 != 0 and number % 5 != 0):
    print(number)


# Question no 9

char = input("enter a single character: ").lower()

if char.isalpha() and len(char) == 1:
    if char in "aeiou":
        print("The character is vowel")
    else:
        print("The character is consonant")
else:
    print("enter valid alphabet") 


# Question no 10

raw_marks = float(input("enter your marks: "))

if raw_marks < 70:
    print("You have failed!")
elif raw_marks >= 70 and raw_marks <= 79:
    print("your grade is a C!")
elif raw_marks >= 80 and raw_marks <= 89:
    print("your grade is a B!")
elif raw_marks >= 90 and raw_marks <= 100:
    print("your grade is an A!")
   
# question no 11

age = int(input("Enter your age: "))

if age < 13:
    print("You are categorized under Children category")
elif age >= 13 and age <= 19:
    print("You are categorized under Teenagers")
elif age > 19:
    print("You are categorized under Adults")

# question no 12

char = input("Enter a character which is either alphabet or number: ")

if len(char) == 1:
    if char.islower() == True:
        print("It is lowercase character")
    elif char.isupper() == True:
        print("It is a uppercase character")
    elif char.isdigit() == True:
        print("It is a number")
    else:
        print("It is a special character")
else:
    print("Enter a valid character")
  

# question no 13

color = input("enter one of three colors (Red, Yellow, Green): ")
if color == "Red":
    print("Stop!")
elif color == "Yellow":
    print("Get Ready")
elif color == "Green":
    print("Go")
else:
    print("enter valid colors(Red, Yellow, Green)")

# question no 14

Age = int(input("Enter your legal age: "))
Experience_years = float(input("Enter your experience years: "))

if Age > 18 and Experience_years >= 2:
    print ("Eligible")
else:
    print("Not Eligible")

# question no. 15

Temperature = float(input("Enter the current temperature in Celsius: "))

if Temperature >= 30:
    print("It's hot, Stay hydrated!")
elif Temperature >= 15 and Temperature < 30:
    print("Enjoy the weather!")
elif Temperature < 15:
    print("It's cold, wear warm clothes!")
      
# question no 16

Pizza = 10
Burger = 7
pasta = 8

customer_food = input("Enter food (Pizza, Burger, Pasta): ")

if customer_food == "Pizza":
    print("Pizza: $",Pizza)
elif customer_food == "Burger":
    print("Burger: $",Burger)
elif customer_food == "Pasta":
    print("Pasta: $",pasta)
else:
    print("enter food on the menu")

  

# question no 17

Height = float(input("Enter your height: "))

if Height >= 6:
    print("You are selected!")
else:
    print("You are not selected!")


# question no. 18

Age = float(input("Enter your age: "))

if Age >= 18:
    print("You are allowed to watch this movie!")
else:
    print("You are not allowed to watch this movie!")
    

# question no. 19
 
Username = input("Enter the username: ")
Password = input("Enter the passowrd: ")

if Username == "admin" and Password == "password123":
    print("Access Granted.")
else:
    print("Access Denied.")

# question no. 20

month_number = int(input("Enter current month: "))

if month_number >= 1 and month_number <= 12:
    if month_number == 12 or month_number == 1 or month_number == 2:
        print("Winter")
    elif month_number == 3 or month_number == 4 or month_number == 5: 
        print("Spring")
    elif month_number == 6 or month_number == 7 or month_number == 8:
        print("Summer")
    elif month_number == 9 or month_number == 10 or month_number == 11:
        print("Autumn")
else:
    print("Enter valid month number!")


# question no.21

salary = float(input("Enter your salary: "))
credit_score = float(input("Ennter your credit score: "))

if salary >= 50000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")

# question no 22

given_number = float(input("Enter your number: "))

if given_number >= 1 and given_number <= 100:
    print("given number is between 1 and 100 inclusive")    
else:
    print("given number is not between 1 and 100 inclusive")

''' 



 
    
    
    
    
    
    
    
    
    
    
    
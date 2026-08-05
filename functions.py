# Create a function that prints "Hello, World!".
def greet():
    print("Hello, World!")
greet()

# Create a function that prints your name.
def _name(name):
    print(name)
_name("Sandeepkumar")

# Create a function that prints today's date.
import datetime
def print_today_date():
    today = datetime.date.today()
    print("Today's date is:", today)
print_today_date()

# Create a function that prints numbers from 1 to 10.
def numbers(n):
    for i in range(1,n+1):
        print(i)
numbers(10)

# Create a function that prints the multiplication table of 5.
def multiplication_table(n):
    for i in range(n,n+1):
        for j in range(1,10+1):
            print(i,"x",j,"=",i*j)
multiplication_table(5)

# Create a function that prints all even numbers from 1 to 20.
def even_numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
even_numbers(20)

# Create a function that prints all odd numbers from 1 to 20.
def even_numbers(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
even_numbers(20)

# Create a function that prints a square pattern of stars (4 × 4).
def square_p(n):
    for i in range(1,n+1):
        stars = ''
        for j in range(1,n+1):
            stars += '* '
        print(stars)
square_p(4)

# Create a function that prints a right-angled triangle of stars.
def square_p(n):
    for i in range(1,n+1):
        stars = ''
        for j in range(1,i+1):
            stars += '* '
        print(stars)
square_p(4)

# Create a function that prints the message "Welcome to Python Programming".
def greet():
    print("Welcome to Python programming")
greet()

# Create a function that takes a name and prints a welcome message.
def welcome(name):
    print("welcome",name,end="!")
welcome("Sandeep")

# Create a function that takes two numbers and prints their sum.
def sum(a,b):
    print(a + b)
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum(a,b)

# Create a function that takes two numbers and prints their difference.
def sum(a,b):
    print(a - b)
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum(a,b)

# Create a function that takes two numbers and prints their product.
def sum(a,b):
    print(a * b)
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum(a,b)

# Create a function that takes two numbers and prints their division.
def sum(a,b):
    print(a/b)
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum(a,b)

# Create a function that takes a number and prints its square.
def square(n):
    print(n**2)
square(5)

# Create a function that takes a number and prints its cube.
def square(n):
    print(n*n*n)
square(2)

# Create a function that takes a number and checks whether it is even or odd.
def even_odd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(4)

# Create a function that takes a number and checks whether it is positive or negative.
def number(n):
    if n>0:
        print("Positive")
    else:
        print("Negative")
number(2)
number(-1)

# Create a function that takes a string and prints its length.
def string(s):
    print(len(s))
s = input("Enter string:")
string(s)
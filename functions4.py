# Section 1: Functions Without Parameters
# 1. Write a function welcome() that prints "Welcome to Python Programming".
def welcome():
    print("Welcome to Python Programming")
welcome()

# 2. Write a function display_details() that prints your name, age, and city.
# Function definition without parameters
def display_details():
    print("Name: Sandeep")
    print("Age: 21")
    print("City: Hyderabad")
display_details()

# 3. Write a function show_even_numbers() that prints all even numbers from 1 to 20.
def show_even_numbers():
    for i in range(1,21):
        if i%2==0:
            print(i)
show_even_numbers()

# 4. Write a function multiplication_table() that prints the multiplication table of 5.
def multiplication_table():
    for i in range(5,5+1):
        for j in range(1,11):
            print(i,"x",j,"=",i*j)
multiplication_table()

# Section 2: Functions With Parameters
# 5. Write a function greet(name) that accepts a name and prints a greeting message.
# Example:
# Input: Ravi
# Output: Hello Ravi
def greet(name):
    print(f"Hello {name}")
greet("Ravi")

# 6. Write a function add(a, b) that accepts two numbers and prints their sum.
def add(a,b):
    print(a+b)
add(28,9)

# 7. Write a function find_square(n) that accepts a number and prints its square.
def find_square(n):
    print(n*n)
find_square(5)

# 8. Write a function find_greatest(a, b, c) that accepts three numbers and prints the greatest number.
def find_greatest(a,b,c):
    if a > b and b > c:
        print(a,"greatest number")
    elif b > c and c > a:
        print(b,"greatest number")
    else:
        print(c,"greatest number")
find_greatest(10,30,20)

# Section 3: Functions Using return
# 9. Write a function add(a, b) that accepts two numbers and returns their sum. Display the returned value outside the function.
def add(a,b):
    return a+b
print(add(28,9))

# 10. Write a function is_even(n) that returns True if the number is even and False otherwise.
def is_even(n):
    if n%2==0:
        return "True"
    else:
        return "False"
print(is_even(2))

# 11. Write a function find_factorial(n) that calculates and returns the factorial of a number.
def find_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(find_factorial(5))

# 12. Write a function calculate_area(length, breadth) that returns the area of a rectangle.
def calculate_area(length,breadth):
    return length * breadth
print(calculate_area(5,10))

# Section 4: Positional Arguments
# 13. Create a function student_details(name, age, course) and call it using positional arguments.
def student_details(name,age,course):
    print(name,age,course)
student_details("Sandy",21,"Python")

# 14. Create a function calculate_bill(item, price, quantity) that returns the total bill amount.
# Call the function by passing all arguments positionally.
def calculate_bill(item, price, quantity):
    total = price * quantity
    print(f"Item: {item}, Total Bill: ₹{total}")
calculate_bill("Notebook", 50, 3)

# 15. Create a function employee_details(name, department, salary).
# Call the function using positional arguments and display the employee details.
def employee_details(name,department,salary):
    print(name,department,salary)
employee_details("Sandy","CSE",25000)

# Section 5: Default Arguments
# 16. Create a function greet(name, message="Good Morning").
# Call the function:
# By passing only the name.
# By passing both name and message.
# Observe the difference in output.
def greet(name,message='Good Morning'):
    print(name,message)
greet("Sandy")
greet("Sandy","Hi")

# 17. Create a function calculate_simple_interest(principal, rate=5, time=2) that returns simple interest.
# Call the function using:
# Only principal
# Principal and rate
# Principal, rate, and time
def calculate_simple_intrest(principal,rate=5,time=2):
    print(principal * rate * time / 100)
calculate_simple_intrest(10000)
calculate_simple_intrest(10000,6)
calculate_simple_intrest(10000,6,3)

# Section 6: Keyword Arguments
# 18. Create a function student_details(name, age, course).
# Call the function using keyword arguments in a different order.
# Function definition
def student_details(name, age, course):
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Course:{course}")
student_details(course="Python",age=21,name="Sandeep")
student_details(age=20,course="Data Science",name="meghana")
student_details(name="Rahul",course="Web Development",age=22)

# 19. Create a function product_details(product, price, quantity) that returns the total price.
# Call the function using keyword arguments in different orders.
def product_details(product,price,quantity):
    print(f"Product:{product}")
    print(f"Price:{price}")
    print(f"Quantity:{quantity}")
product_details(product="mobile",price=20000,quantity=1)
product_details(price=55000,quantity=1,product="AC")

# Section 7: Mixed Challenge — All Concepts
# 20. Create a function calculate_salary(name, basic_salary, bonus=5000).
# The function should:
# Accept name and basic_salary.
# Have a default value of 5000 for bonus.
# Calculate the total salary.
# Return the total salary.
# Call the function once using positional arguments.
# Call it again using keyword arguments.
# Call it a third time by using the default value for bonus.
def calculate_salary(name,basic_salary,bonus=5000):
    total_salary = basic_salary + bonus
    return total_salary
print(calculate_salary("Sandy",35000,4000))
print(calculate_salary(name="Meghana",basic_salary=55000,bonus=5400))
print(calculate_salary("Sandeep",70000))

    


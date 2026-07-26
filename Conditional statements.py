# 1. Check whether a number is positive, negative, or zero 
num = int(input('enter number:'))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


# 2. Check whether a number is even or odd  
num = int(input('enter number:'))
if num%2==0:
    print("even")
else:
    print("odd")


# 3. Find the largest of two numbers 
num1 =int(input('enter first number:'))
num2 =int(input('enter second number:'))
if num1>num2:
    print("largest")
else:
    print("largest") 


# 4. Find the largest of three numbers  
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter last number:"))
if a>b and a>c:
    print(a,"largest number")
elif b>c and c<a:
    print(b,"largest number")
else:
    print(c,"largest number")


# 5. Check whether a person is eligible to vote (age ≥ 18)  
age = int(input('enter age:'))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

    
# 6. Assign grades based on marks (A, B, C, Fail)
marks = 80
if marks>=75:
    print("grade A")
elif marks>=55:
    print("grade B")
elif marks>=35:
    print("grade C")
else:
    print("fail") 
    
    
# 7. Check whether a character is vowel or consonant 
ch = input("enter char:")
if ch in 'aeiouAEIOU':
    print("vowel")
else:
    print("consonant")
    
    
# 8. Check whether a number is divisible by both 3 and 5 
num = int(input('enter number:'))
if num%3==0 and num%5==0:
    print(num,"divisible by both 3 and 5")
else:
     print(num,"not divisible by both 3 and 5")
     
     
# 9. Check whether a character is uppercase, lowercase, digit, or special symbol  
char = input("Enter a character: ")
if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

# 10. Check whether a number is divisible by 7 
num = int(input("Enter number:"))
if num % 7 ==0:
    print(num,"is divisible by 7")
else:
    print(num,"not divisible by 7")
    
     
# 11. Check whether a person is a senior citizen (age ≥ 60)  
age = int(input("enter your age:"))
if age >= 60:
    print("senior citizen")
else:
    print("not senior citizen")
    
    
# 12. Check whether a year is a leap year  
year = int(input('enter year:'))
if year%4==0:
    print(year,"leap year")
else:
    print(year,"not leap year")
    
    
# 13. Build a *simple calculator (+, -, , /)  
# 14. Check whether a number is in range (1 to 100)  
num = int(input('enter number:'))
if num in range(1,100):
    print("True")
else:
    print("False")
    
    
# 15. Input marks of 3 subjects and check pass/fail (≥35 each)  
Dsa = 40
sppm = 36
cc = 30
if Dsa>=35 and sppm>=35 and cc>=35:
    print("pass")
else:
    print("Fail")
    
    
# 16. Check whether a number is a multiple of 3 and 5 (separately)  
num = int(input("number:"))
if num%3==0 and num%5==0:
    print("satisfy")
else:
    print("Not satisfy")
    
    
# 17. Simulate ATM withdrawal (check sufficient balance)  
withdrawl_amount = int(input("enter the amount:"))
balance = 20000
if withdrawl_amount < balance:
    print("Transaction sucessful")
else:
    print("Transaction failed")
    print("Insufficient balance")
    

# 18. Calculate tax based on salary slabs  
salary = float(input("enter salary:"))
if salary <= 100000:
    print("0 tax")
elif salary >= 200000:
    print("tax=",salary*5/100)
elif salary > 300000:
    print("tax=",salary*10/100)
else:
    print("tax=",salary*20/100)
    
    
# 19. Check whether a number is a 3-digit number
num = int(input("Enter number:"))
if num >= 100 and num <= 1000:
    print(num,"is a 3-digit number")
else:
    print(num,"is not a 3-digit number")
    
    
# 20. Check whether a character is an alphabet (without built-in functions)  
char = input("Enter the character:")
Alphabet = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
if char in Alphabet:
    print("yes")
    print(f"'{char}' is an Alphabet")
else:
    print("No")
    print(f"'{char}' is not an Alphabet")
    
    
# 21. Find the largest of three numbers using nested if  
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
if num1 > num2:
    if num1 > num3:
        print(num1,"is largest number")
    else:
        print(num1,"is not largest number")
else:
    if num2 > num3:
        print(num2,"is largest number")
    else:
        print(num3,"is largest number")
        
        
# 22. Create a login system (username & password check)
username = input("Username:")  
password = input("Password:")
if username == 'sandeep10k' and password == '@sandeep':
    print("Welcome Back Sandeep!")
else:
    print("Invalid Username or Password")
    
    
# 23. Check whether a number is positive → then check even/odd 
num = int(input("enter number:")) 
if num>0:
    if num%2==0:
        print("even")
    else:
        print("odd")
else:
    print("enter positive number?")


# 24. ATM system with conditions (balance + withdrawal limit)  
balance = 20000
withdrawl = int(input("Enter amount:"))
withdrawl_limit = 10000
if withdrawl <= balance and withdrawl <= withdrawl_limit:
    print("Transaction Sucessful")
else:
    print("Transaction Failed")
    print("withdrawl limit exceeded")
    print(f"You cannot withdrawl {withdrawl} in a single transaction")
    
    
# 25. Student result system:  
# • Pass (≥35)  
# • Distinction (≥75)  
# • First Class (≥60)  
marks = int(input("enter marks:"))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

# # 1. Check whether a number is positive, negative, or zero 
# num = int(input('enter number:'))
# if num>0:
#     print(num,"positive")
# elif num<0:
#     print(num,"negative")
# else:
#     print(num,"zero")


# # 2. Check whether a number is even or odd  
# num = int(input('enter number:'))
# if num%2==0:
#     print("even")
# else:
#     print("odd")


# # 3. Find the largest of two numbers 
# num1 =int(input('enter first number:'))
# num2 =int(input('enter second number:'))
# if num1>num2:
#     print(num1,"largest")
# else:
#     print(num2,"largest") 


# # 4. Find the largest of three numbers  
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter last number:"))
# if a>b and a>c:
#     print(a,"largest number")
# elif b>c and c<a:
#     print(b,"largest number")
# else:
#     print(c,"largest number")


# # 5. Check whether a person is eligible to vote (age ≥ 18)  
# age = int(input('enter age:'))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

    
# # 6. Assign grades based on marks (A, B, C, Fail)
# marks = 80
# if marks>=75:
#     print("grade A")
# elif marks>=55:
#     print("grade B")
# elif marks>=35:
#     print("grade C")
# else:
#     print("fail") 
    
    
# # 7. Check whether a character is vowel or consonant 
# ch = input("enter char:")
# if ch in 'aeiouAEIOU':
#     print("vowel")
# else:
#     print("consonant")
    
    
# # 8. Check whether a number is divisible by both 3 and 5 
# num = int(input('enter number:'))
# if num%3==0 and num%5==0:
#     print(num,"divisible by both 3 and 5")
# else:
#      print(num,"not divisible by both 3 and 5")
     
     
# # 9. Check whether a character is uppercase, lowercase, digit, or special symbol  

# # 10. Check whether a number is divisible by 7  
# # 11. Check whether a person is a senior citizen (age ≥ 60)  
# age = int(input("enter your age:"))
# if age >= 60:
#     print("senior citizen")
# else:
#     print("not senior citizen")
    
    
# # 12. Check whether a year is a leap year  
# year = int(input('enter year:'))
# if year%4==0:
#     print(year,"leap year")
# else:
#     print(year,"not leap year")
    
    
# # 13. Build a *simple calculator (+, -, , /)  
# # 14. Check whether a number is in range (1 to 100)  
# num = int(input('enter number:'))
# if num in range(1,100):
#     print("True")
# else:
#     print("False")
    
    
# # 15. Input marks of 3 subjects and check pass/fail (≥35 each)  
# Dsa = 40
# sppm = 36
# cc = 30
# if Dsa>=35 and sppm>=35 and cc>=35:
#     print("pass")
# else:
#     print("Fail")
    
    
# # 16. Check whether a number is a multiple of 3 and 5 (separately)  
# num = int(input("number:"))
# if num%3==0 and num%5==0:
#     print("satisfy")
# else:
#     print("Not satisfy")
    
    
# # 17. Simulate ATM withdrawal (check sufficient balance)  
withdrawl_amount = int(input("enter the amount:"))
balance = 20000
if withdrawl_amount < balance:
    print("Transaction sucessful")
else:
    print("Transaction failed")
    print("Insufficient balance")
    

# # 18. Calculate tax based on salary slabs  
# # 19. Check whether a number is a 3-digit number  
# # 20. Check whether a character is an alphabet (without built-in functions)  
# # 21. Find the largest of three numbers using nested if  
# # 22. Create a login system (username & password check)
# username = input("Username:")  
# password = input("Password:")
# if username == 'sandeep10k' and password == '@sandeep':
#     print("Welcome Back Sandeep!")
# else:
#     print("Invalid Username or Password")
    
    
# # 23. Check whether a number is positive → then check even/odd 
# num = int(input("enter number:")) 
# if num>0:
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("enter positive number?")


# # 24. ATM system with conditions (balance + withdrawal limit)  
# # 25. Student result system:  
# # • Pass (≥35)  
# # • Distinction (≥75)  
# # • First Class (≥60)  

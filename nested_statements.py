# Easy Level
# Write a program to check whether a person is eligible to vote.
# If the person's age is 18 or above, check whether they have a voter ID.
# Print the appropriate message.
age = int(input("Enter your age:"))
voter_id = input("(yes/no):")
if age >= 18:
    if voter_id == "yes":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote because you dont have an voter ID")
else:
    print("You are not eligible to vote because you are under 18")
    
    
# Write a program to check whether a student has passed.
# If the student scores 35 or more, check if the marks are 75 or above.
# Display "Distinction" or "Pass" accordingly.
marks = int(input("Enter marks:"))
if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")
    
    
# Write a program to check whether a user can log in.
# If the username is correct, check whether the password is correct.
username = input("Username:")
password = input("Password:")
if username == 'sandeep.dv':
    if password == '@made2006':
        print("login")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
    
    
# Write a program to check whether a person can drive.
# If the age is 18 or above, check whether they have a valid driving license.
age = int(input("Enter age:"))
driving_license = input("(yes/no):")
if age >= 18:
    if driving_license == "yes":
        print("Can Drive")
    else:
        print("can't Drive because you dont have a driving license")
else:
    print("Can't drive because you are under 18")
    
    
# Write a program to check ATM withdrawal.
# If the account balance is greater than or equal to the withdrawal amount, check whether the withdrawal amount is within the daily limit.
balance = 20000
withdrawl = int(input("Enter Withdrawl Amount:"))
withdrawl_limit = 10000
if balance >= withdrawl:
    if withdrawl < withdrawl_limit:
        print("Transaction Sucessful")
    else:
        print("Transaction Fail , withdrawl limit exceeds")
else:
    print("Insufficient balance")


# Medium Level
# Write a program to determine an employee's bonus.
# If the employee has worked for at least 5 years, check if the performance rating is "Excellent".
# Give a higher bonus for excellent performance; otherwise, give a standard bonus.
worked = int(input("enter working experience in (years):")) 
performance = 'Excellent'
if  worked >= 5:
    if performance == 'Excellent':
        print("Higher bonus")
    else:
        print("Standard bonus")
else:
    print("you should work atleast 5 years, to get higher bonus")    
    
    
# Write a program to determine whether a student is eligible for a scholarship.
# If the student's attendance is at least 75%, check whether the marks are 90 or above.
attendance = float(input("enter your attendance in '%':"))
marks = float(input("enter marks:"))
if attendance >= 75:
    if marks >= 90:
        print("eligible for scholarship")
    else:
        print("not eligible for scholarship")
else:
    print("you are not eligible for scholarship due to less attendance")


# Write a program to check admission eligibility.
# If the candidate has passed the entrance exam, check whether their age is between 17 and 25.
passed = input("(Pass/Fail):")
age = int(input("enter age:"))
if passed == 'Pass':
    if age >= 17 and age <= 25:
        print("eligible for adimission")
    else:
        print("not eligible for admission")
else:
    print("Fail")


# Write a program to determine whether an online order qualifies for free delivery.
# If the purchase amount is at least ₹1000, check whether the customer is a premium member.
amount = int(input("enter purchase amount:"))
premium_member = input("(yes/no):")
if amount >= 1000:
    if premium_member == 'yes':
        print("free delivery")
    else:
        print("no free delivery")
else:
    print("amount should be atleast 1000 to avail free delivery")

# Write a program to check if a bank loan can be approved.
# If the applicant's salary is at least ₹30,000, check whether their credit score is 750 or above.
salary = float(input("Enter salary:"))
credit_score = int(input("Enter credit score:"))
if salary >= 30000:
    if credit_score >= 750:
        print("Bank loan approved")
    else:
        print("Bank loan failed due to less credit score")
else:
    print("Bank loan failed due to less salary")
    
    
# Write a program to determine a movie ticket price.
# If the person is a student, check whether they are under 18 to provide an additional discount.
person = input("Are you a student (yes/no):")
age = int(input("Enter age: "))
if person == 'yes':
    if age < 18:
        print("student discount, under 18")
    else:
        print("no student discount")
else:
    if age < 18:
        print("under 18 discount")
    else:
        print("regular price")


# Write a program to determine hostel eligibility.
# If the student belongs to another city, check whether hostel rooms are available.
student = input("Do you belongs to another city (yes/no):")
hostel_rooms = True
if student == 'yes':
    if hostel_rooms == True:
        print("rooms are available")
    else:
        print("rooms are not available")
else:
    print("not eligible for hostel")
    
    
# Write a program to determine promotion eligibility.
# If an employee has completed at least 3 years of service, check whether the performance rating is at least 4.
# Program to determine promotion eligibility
service = int(input("Enter years of service:"))
rating = float(input("Enter performance rating (1-5):"))
if service >= 3:
    if rating >= 4:
        print("Eligible for promotion")
    else:
        print("Not eligible for promotion due to low performance rating")
else:
    print("Not eligible for promotion due to insufficient years of service")


# Write a program to check exam eligibility.
# If attendance is at least 75, check whether the assignment marks are at least 40.
# Program to check exam eligibility
attendance = float(input("Enter attendance percentage:"))
assignment_marks = int(input("Enter assignment marks:"))
if attendance >= 75:
    if assignment_marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible due to low assignment marks")
else:
    print("Not eligible due to low attendance")




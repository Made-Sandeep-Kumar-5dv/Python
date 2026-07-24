"""Comparison Operators (==, !=, >, <, >=, <=)"""

"""Rahul scored 78 marks. The passing mark is 35.
 Write a Python expression to check whether Rahul passed."""
marks = 78
pass_marks = 35
print(marks > pass_marks) # True

"""A movie ticket is allowed only for people aged 18 or above.
 A person's age is 16.
 Write an expression to check if they are eligible."""
person_age = 16
ticket_age = 18
print(person_age >= ticket_age) # False

"""A laptop costs ₹55,000.
 Your budget is ₹60,000.
 Check whether the laptop is within your budget."""
laptop_cost = 55000
my_budget  = 60000
print(my_budget > laptop_cost) # True

"""There are 25 students in Class A and 25 students in Class B.
 Write an expression to check whether both classes have the same number of students."""
A_students = 25
B_students = 25
print(A_students == B_students) # True

"""The temperature today is 42°C.
 Check whether the temperature is greater than 40°C."""
temp = 42
print(temp > 40) # True

"""A customer entered the correct OTP 5678.
 The entered OTP is 6789.
 Write an expression to check whether the OTP is incorrect."""
correct_otp = 5678
entered_otp = 6789
print(correct_otp != entered_otp) # True

"""The speed limit is 80 km/h.
 A car is moving at 80 km/h.
 Check whether the car is following the speed limit."""
speed_limit_kmh = 80
car_speed_kmh = 80
print(speed_limit_kmh == car_speed_kmh) # True

"""A train has 150 seats.
 Currently, 145 seats are booked.
 Check whether all seats are filled."""
total_seats = 150
booked_seats = 145
print(total_seats == booked_seats) # False

"""The minimum balance required in a bank account is ₹1000.
 Current balance is ₹850.
 Check whether the balance is less than the required amount."""
min_balance = 1000
current_balance = 850
print(current_balance < min_balance) # True

"""A student needs at least 75% attendance.
 Current attendance is 75%.
 Check whether the student is eligible for the exam."""
required_attendance = 75
current_attendance = 75
print(required_attendance == current_attendance) # True

"""Logical Operators (and, or, not)
A student can attend the placement drive only if:
CGPA is 7.5 or above
Attendance is 75% or above
Current CGPA = 8.1
 Attendance = 82%"""
cgpa = 8.1
attendance = 82
print(cgpa >= 7.5 and attendance >= 75) # True

"""A customer gets free delivery if:
Purchase amount is above ₹500
Customer is a Prime member
Purchase = ₹650
 Prime Member = True
Write the condition."""
purchase = 650
prime_member = True
print(purchase > 500 and prime_member ==True) # True

"""A website allows login if:
Username is correct OR
Email is correct
Username Correct = False
 Email Correct = True
Write the condition."""
username = False
email = True
print(username == True or email == True) # True 

"""A cricket player is selected if:
Runs > 500
Wickets > 20
Runs = 620
 Wickets = 18
Write the condition."""
runs = 620
wickets = 18
print(runs > 500 and wickets > 20) # False

"""A student passes only if:
Theory marks ≥ 35
Practical marks ≥ 35
Theory = 40
 Practical = 30
Write the condition."""
theory_marks = 40
practical_marks = 30
print(theory_marks >= 35 and practical_marks >= 35) # False

"""A shop offers a discount if:
Customer is a member
OR total purchase exceeds ₹2000
Member = False
 Purchase = ₹2500
Write the condition."""
member = False
purchase = 2500
print(member == False or purchase > 2000) #True

"""A person can vote if:
Age is 18 or above
AND is an Indian citizen
Age = 20
 Citizen = True
Write the condition."""
age = 20
citizen = True
print(age >= 18 and citizen == True) # True

"""A student is not absent.
 Absent = False
Write a Python expression using the not operator to check whether the student is present."""
absent = False
print(not(absent)) # True

"""A system grants admin access only if:
Username is "admin"
Password is correct
Username = "admin"
 Password Correct = True
Write the condition."""
username = 'admin'
password = True
print(username == 'admin' and password == True) #True

"""A person can enter a swimming pool if:
They have a membership
OR they pay the entry fee
Membership = False
 Paid Fee = False
Write the condition."""
membership = False
fee_paid = False
print(not(membership == True or fee_paid == True)) # True

# Mixed Comparison + Logical Operators
"""A student gets Grade A if:
Marks are between 90 and 100 (inclusive).
Marks = 95
Write the condition."""
marks = 95
print(marks >= 90 and marks <= 100) #True

"""A customer is eligible for cashback if:
Purchase ≥ ₹1000
AND purchase ≤ ₹5000
Purchase = ₹3200
Write the condition."""
purchase = 3200
print(purchase >= 1000 and purchase <= 5000) #True

"""A user can reset their password if:
OTP is correct
AND account is active
OTP Correct = True
 Account Active = True
Write the condition."""
correct_otp = True
ac_active = True
print(correct_otp == True and ac_active == True) # True

"""A player qualifies if:
Age is between 18 and 25 (inclusive).
Age = 23
Write the condition."""
age = 23
print(age >= 18 and age <= 25) #True

"""A vehicle is fined if:
Speed > 80 km/h
OR signal is broken
Speed = 75
 Signal Broken = True
Write the condition."""
speed = 75
signal_broken = True
print(speed > 80 or signal_broken == True) #True

# Challenge Questions
"""Write a condition to check whether a number is between 10 and 50 (inclusive)."""
num = int(input())
print(num >= 10 and num <= 50) #True

"""Write a condition to check whether a person is either a student or a teacher."""
person = input("student or teacher:")
print(person == "student" or person == "teacher") # student True , teacher True

"""Write a condition to check whether a password length is at least 8 characters and contains at least one digit."""
ch = "Sandy"
print(len(ch) >= 8 and len(ch) >= 1) # False

"""Write a condition to check whether a person's age is not less than 18."""
age = 24
print(age > 18) # True

"""A customer gets a gift only if:
Purchase amount is greater than ₹5000
AND customer is a premium member
AND today is their birthday
Write the condition using logical operation"""
amount = int(input())
member = bool(input())
birthday = bool(input())
gift = bool(amount > 5000 and member and birthday)
print(gift) # True
"""Interview-Style Questions Based on Conditional Statements"""

# 1. Check Even or Odd
# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number
num = 6
if num%2==0:
    print("even number")
else:
    print("odd number")


# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
num = 25
if num%5==0 and num%10!=0:
    print("Satisfy")
else:
    print("not satisfy")
    
    
# 3. Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
a=4
b=7
if a>b:
    print("biggest is:",a)
else:
    print("biggest is:",b) 
    
    
# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4
a=4
b=7
if a<b:
    print("smallest is:",a)
else:
    print("smallest is:",b) 
    
    
# 5. Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy
num = 18
if num%6==0:
    if num%2==0 and num%3==0:
        print("Satisfy")
else:
    print("not satisfy")
    
    
# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
age = 19
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


# 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail
Maths = 40
Physics = 36
Chemistry = 30
if Maths>=35 and Physics>=35 and Chemistry>=35:
    print("pass")
else:
    print("Fail")
    
    
# 8. Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass
Maths = 20
Physics = 38
Chemistry = 25
if Maths>=35 or Physics>=35 or Chemistry>=35:
    print("Pass")
else:
    print("Fail")
    
    
# 9. Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass
Maths = 40
Physics = 20
Chemistry = 36
if Maths>=35 and Physics>=35 or Maths>35 and Chemistry>=35:
    print("Pass")
else:
    print("Fail")
    
    
# 10. Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9
A = 7
B = 4
C = 9
if A>B and A>C:
    print("Biggest is",A)
elif B>C and C<A:
    print("Biggest is",B)
else:
    print("Biggest is",C)
    
    
# 11. Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
A = 7
B = 4
C = 9
if A<B and A>C:
    print("Smallest is",A)
elif B<C and C>A:
    print("Smallest is",B)
else:
    print("Smallest is",C)
    
    
# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square
Number = 49
if Number%7==0:
    print("Perfect square")
else:
    print("not perfect square")
    
    
# 13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
members = 17
cars = members / 5
print(cars)
# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18
A = 10
B = 25
C = 18
if A>B and A>C:
    print("Second Biggest is",A)
elif B>C and B<A:
    print("Second Biggest is",B)
else:
    print("Second Biggest is",C)
    
    
# 15. Leap Year or Not
# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
Year = 2024
if Year%4==0:
    print("Leap year")
else:
    print("Not leap year")

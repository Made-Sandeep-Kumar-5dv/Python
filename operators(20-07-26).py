# Interview-Style Programming Questions: Basic Math and Logic

# 1. Area of Square
# Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25
side = 5
result = side * side
print("Area of Square is:",result)


# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24
l = 6
b = 4
result = l*b
print("Area of Rectangle is:",result)


# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0
base = 8
height = 5
result = (1/2) * base * height
print("Area of Triangle is:",result)


# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - Side = 6 - Output: - Perimeter of square is: 24
side = 6
result = 4 * side
print("Perimeter of Square is:",result)


# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16
l = 5
b = 3
result = 2 * (l + b)
print("Perimeter of Rectangle is:",result)


# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
side1 = 5
side2 = 6
side3 = 7
result = side1+side2+side3
print("Perimeter of Triangle is:",result)


# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200
Amount = 3700
thousands = Amount // 1000
Amount = Amount % 1000
fivehundreds = Amount // 500
Amount = Amount % 500
Remaining = Amount
print(f"1000s: {thousands} - 500s: {fivehundreds} - Remaining: {Remaining}")

# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
Totalseconds = 3672
Hrs = Totalseconds // 3600
mins = Totalseconds // 3600
secs = Totalseconds % 60
print(f"Hours: {Hrs} - Minutes: {mins} - Seconds: {secs}")


# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
Maths  = 85
Physics = 90
Chemistry = 88
result = Maths + Physics + Chemistry
print("Total Marks:",result)


# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
Maths  = 85
Physics = 90
Chemistry = 88
result = (Maths + Physics + Chemistry) / 3
print("Average Marks:",result)
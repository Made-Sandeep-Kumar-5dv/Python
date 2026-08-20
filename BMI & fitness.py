def get_details():
    height = int(input("Enter Height:"))
    weight = float(input("Enter Weight:"))
    return height,weight

def calculate_bmi(height,weight):
    bmi = weight / (height * height)
    return bmi

def find_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def display_result(weight,height):
    # height,weight = get_details()
    bmi = calculate_bmi(height,weight)
    Category = find_category(bmi)
    
    print(f"Enter Weight: {weight}") 
    print(f"Enter height: {height}")
    print(f"BMI: {bmi}")
    print(f"Category: {Category}")  
display_result(175.5,75)
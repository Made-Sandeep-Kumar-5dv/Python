def get_marks():
    name = input("Enter Student Name:")
    python = float(input("Enter Python Marks:"))
    Java = float(input("Enter Java Marks:"))
    Sql = float(input("Enter SQL Marks:"))
    return name,python,Java,Sql

def calculate_total(sub1,sub2,sub3):
    return sub1+sub2+sub3

def calculate_average(total_marks,subjects=3):
    return total_marks/subjects

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
    
def display_result(name,total_marks,average,grade):
    print(f'Student Name: {name}')
    print(f'Total Marks: {total_marks}')
    print(f'Average: {average:.2f}')
    print(f'Grade: {grade}')
    
def main():
    name,python,Java,Sql = get_marks()
    total_marks = calculate_total(python,Java,Sql)
    average = calculate_average(total_marks)
    grade = calculate_grade(average)
    display_result(name,total_marks,average,grade)
main()
def show_cab_types():
    print("=== Cab Type ===")
    print("1. Mini")
    print("2. Sedan")
    print("3. SUV")
    
    choice = int(input("Enter Cab Type (1-3): "))
    return choice

def get_distance():
    distance = float(input("Enter Distance (in km): "))
    return distance

def calculate_fare(choice, distance):
    basic_fare = 100
    rate_per_km = 12
    
    if choice == 1:  
        distance_fare = rate_per_km * distance
    elif choice == 2:  
        distance_fare = (rate_per_km * 2) * distance
    elif choice == 3:  
        distance_fare = (rate_per_km * 3) * distance
    else:
        distance_fare = 0
    
    total_fare = basic_fare + distance_fare
    return basic_fare, distance_fare, total_fare

def calculate_discount(fare):
    discount = 10  
    return fare - discount

def generate_bill():
    choice = show_cab_types()
    distance = get_distance()
    base_fare, distance_fare, total_fare = calculate_fare(choice, distance)
    final_fare = calculate_discount(total_fare)
    
    print("=== Bill ===")
    print(f"Cab Type: {choice}")
    print(f"Distance: {distance} km")
    print(f"Base Fare: ₹{base_fare}")
    print(f"Distance Fare: ₹{distance_fare}")
    print(f"Total Fare: ₹{total_fare}")
    print(f"Final Fare: ₹{final_fare}")
    
generate_bill()

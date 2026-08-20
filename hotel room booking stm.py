def show_rooms():
    print("---- ROOM TYPE ----")
    print("1. Single Room $1500/day")
    print("2. Double Room $2500/day")
    print("3. Deluxe Room $4000/day")

def select_room():  
    choice = int(input("Enter Room Type (1-3):"))
    days = int(input("Enter Number of Days:"))
    return choice, days

def calculate_room_cost(choice, days):
    if choice == 1:
        room_cost = 1500 * days
    elif choice == 2:
        room_cost = 2500 * days
    elif choice == 3:
        room_cost = 4000 * days
    else:
        room_cost = 0
    return room_cost

def calculate_service_charge():
    return 500

def calculate_discount():
    return 1000

def generate_bill(choice, days):
    room_cost = calculate_room_cost(choice, days)
    service_charge = calculate_service_charge()
    discount = calculate_discount()
    final_amount = room_cost + service_charge - discount
    return f"Final Amount: ${final_amount}"
show_rooms()
choice, days = select_room()
print(generate_bill(choice, days))

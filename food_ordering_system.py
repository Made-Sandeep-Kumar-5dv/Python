def display_menu():
    print("---- MENU ----")
    print("1. Pizza ₹250")
    print("2. Burger ₹150")
    print("3. Pasta ₹200")
    print("4. Sandwich ₹120")
    
def select_food(choice,quantity):
    choice = int(input("Enter choice (1-4):"))
    quantity = int(input("Enter Quantity:"))
    return choice,quantity

def calculate_price(choice,quantity):
    if choice == 1:
        price = 250 * quantity
    elif choice == 2:
        price = 150 * quantity
    elif choice == 3:
        price = 200 * quantity
    elif choice == 4:
        price = 120 * quantity
    else:
        price = 0
    return price

def calculate_discount():
    return 50

def generate_bill():
    display_menu()
    choice, quantity = select_food(None, None)
    price = calculate_price(choice, quantity)
    discount = calculate_discount()
    final_amount = price - discount
    
    print("\n---- BILL ----")
    print(f"Item: {choice}")
    print(f"Quantity: {quantity}")
    print(f"Total: ₹{price}")
    print(f"Discount: ₹{discount}")
    print(f"Final Bill: ₹{final_amount}")
    
generate_bill()

    
    
def show_movies():
    print("--- MOVIES ---")
    print("1. Varanasi")
    print("2. Paradise")
    print("3. DC")
    print("4. Vishwanath & Sons")
    print("5. Lenin")

def select_movie(choice,tickets):
    choice = int(input("Enter Movie (1-5):"))
    tickets = int(input("Enter Number of Tickets:"))
    return choice,tickets

def calculate_ticket_price(choice,tickets,price=200):
    if 1 <= choice <= 5:
        ticket_price = price * tickets
    else:
        ticket_price = 0
    return ticket_price

def calculate_discount(ticket_price):
    return ticket_price * 20/100

def display_bill():
    while True:
        show_movies()
        choice,tickets = select_movie(None,None)
        ticket_price = calculate_ticket_price(choice,tickets)
        discount = calculate_discount(ticket_price)
        final_amount = ticket_price - discount
        
        print(f"Enter Movie: {choice}")
        print(f"Enter Number of Tickets: {tickets}")
        print(f"Ticket Price: 200")
        print(f"Total: {ticket_price}")
        print(f"Discount: {discount}")
        print(f"Final Amount: {final_amount}")
display_bill()
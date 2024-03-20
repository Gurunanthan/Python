menu = {
    "Idly": 2.50,
    "Dosa": 3.50,
    "Poori": 4.00,
    "Pongal": 3.00,
    "sandhagaii": 5.00,
    "ravai": 3.00,
    "Chapathi": 2.00,
    "Parotta": 2.50,
    "Uthappamm": 3.00
}

def print_menu():
    i = 1
    for item, price in menu.items():
        print(i, "", item, "- $", price)
        i += 1

def calculate_bill(order):
    total_cost = 0
    for item, qty in order.items():
        total_cost += menu[item] * qty
    return total_cost

def main():
    order = {}
    while True:
        print("\nMenu:")
        print_menu()
        
        try:
            choice = int(input("Enter the Item number from the menu (0 to finish): "))
            if choice == 0:
                break
            elif choice < 1 or choice > len(menu):
                print("Invalid choice. Please choose a valid item number.")
                continue
            
            amount = int(input("Enter quantity: "))
            if amount < 1:
                print("Quantity should be a positive integer.")
                continue
            
            item_index = choice - 1
            item_name = list(menu.keys())[item_index]
            
            if item_name in order:
                order[item_name] += amount
            else:
                order[item_name] = amount
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    total_bill = calculate_bill(order)
    print("\nYour order:")
    for item, qty in order.items():
        print(item, "x", qty)
    print("Total bill: $", total_bill)
    print(order)

if __name__ == "__main__":
    main()

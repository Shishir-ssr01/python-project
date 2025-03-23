import qrcode
import time
from datetime import datetime

# Menu with prices
menu = {
    'pizza': 160,
    'pasta': 90,
    'tea': 50,
    'ice cream': 90,
    'sandwich': 120,
    'hot coffee': 80,
    'cold coffee': 80,
    'litti chokha': 150,
}

# Display current time and date
current_time = datetime.now().strftime("%H:%M:%S")
date = datetime.now().strftime("%y-%m-%d")

print("Welcome to our SAH cafe")
print(f"{current_time}")
print(f"{date}")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}")

# Initialize total order amount
order_total = 0

# Function to process an order item
def process_order(item_name):
    global order_total
    if item_name in menu:
        print(f"Your item {item_name} is in the order list!")
        try:
            quantity = int(input(f"How many {item_name}s would you like? "))
            if quantity > 0:
                order_total += menu[item_name] * quantity
                print(f"{quantity} '{item_name}' has been added to your order!")
            else:
                print("Sorry, quantity must be greater than 0.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Sorry, your item {item_name} is not available here.")

# Process first item
item_1 = input('Enter the name of the item: ').lower()
process_order(item_1)

# Process additional items
while True:
    another_order = input('Would you like another item? (yes/no): ').lower()
    if another_order == "yes":
        item_2 = input('Enter the name of another item: ').lower()
        process_order(item_2)
    else:
        break

# Calculate total with GST and service charge
order_total += order_total * 0.18 + order_total * 0.02
print(f"Total amount of order you placed: ₹{order_total:.2f}")
print("THANK YOU FOR VISITING! Have a nice day!")

# Generate UPI payment QR code
upi_id = "xxxxxxxxxxxxxxxxxxxx"  # Replace with actual UPI ID
recipient_name = "xxxxxxxxxxx"   #merchant name
google_pay = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={order_total:.2f}&cu=INR"
g_pay_qr = qrcode.make(google_pay)
g_pay_qr.save('g_pay_qr.png')
g_pay_qr.show()

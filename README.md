# SAH Cafe Ordering System

This is a Python-based terminal application for ordering food at SAH Cafe. The program allows users to place an order from a predefined menu, calculates the total cost including GST and service charge, and generates a UPI payment QR code for easy payment.

## Features
- 🕒 Displays the current date and time.
- 📜 Provides a menu with predefined prices.
- 🍽️ Allows customers to select multiple items and specify quantities.
- 💰 Computes the total bill including:
  - 🏷️ GST (18%)
  - 🏷️ Service charge (2%)
- 📲 Generates a QR code for UPI payment via Google Pay.

## Requirements
- 🐍 Python 3.x
- 📦 `qrcode` library (install using `pip install qrcode[pil]`)

## Usage
1. ▶️ Run the script using:
   ```bash
   python cafe_order.py
   ```
2. 📋 Follow the prompts to place an order.
3. 🏷️ Once all items are added, the total amount is displayed.
4. 📷 A QR code is generated for UPI payment. Scan it using any UPI-enabled payment app.

## Example Menu
```
🍕 pizza: ₹160
🍝 pasta: ₹90
🍵 tea: ₹50
🍨 ice cream: ₹90
🥪 sandwich: ₹120
☕ hot coffee: ₹80
🥤 cold coffee: ₹80
🥘 litti chokha: ₹150
```

## Notes
- ⚠️ The UPI ID and recipient name should be updated with actual merchant details before use.
- 🖼️ The QR code is saved as `g_pay_qr.png` and displayed for payment.

## License
📜 This project is open-source and can be modified as needed.



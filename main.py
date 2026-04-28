from jinja2 import Template
from datetime import date
import webbrowser

cart = []
total_sum = 0

client_name = input("Client name: ")
invoice_number = input("Invoice number: ")

while True:
    add = input("Add item (q to quit): ")
    if add == "q":
        break

    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    total = price * quantity
    total_sum += total

    cart.append([add, quantity, price, total])

# Load template
with open("invoice_template.html", "r", encoding="utf-8") as file:
    template = Template(file.read())

# Render HTML
html_output = template.render(
    client_name=client_name,
    invoice_no=invoice_number,
    date=date.today(),
    items=cart,
    grand_total=total_sum
)

# Save output
with open("invoice.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("Invoice created: invoice.html")

webbrowser.open("invoice.html")

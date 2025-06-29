#cafe order management system


menu = {
    "pizza": 150,
    "burger": 50,
    "coffee":60,
    "pasta": 100,
    "coke": 40,
    "biryani": 160,
    "saled":40
 }

order = {}
total = 0

while True:
    print("\nWelcome to PG Cafe!")
    print("\nMenu:\nburger:rs 50\npizza:rs 120\ncoffee:rs 60\npasta:rs 100\nbiryani rs:160\nsaled:rs 40'",)
    item = input("Enter item to order (or 'exit' to finish): ")
    
    if item.lower() == 'exit':
        break
    elif item in menu:
        qty = int(input("Enter quantity: "))
        order[item] = order.get(item, 0) + qty
        total += menu[item] * qty
    else:
        print("Item not available!")

print("\n🧾 Your Order Summary:")
for item, qty in order.items():
    print(f"{item} x {qty} = ₹{menu[item]*qty}")
print("Total Bill: ₹", total)






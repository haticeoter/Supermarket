from supermarket import *
print("""***********************************

Welcome to the Supermarket Program.

Operations;

1. Show the Products

2. Look for a Product

3. Sell a Product

4. Add a Product

Type "E" to exit.
***********************************""")

product = Supermarket()

while True:
    operation = input("Which operation would you like to do:")

    if operation == "E":
        print("Program is terminated.....")
        break

    elif operation == "1":
        product.show_products()

    elif operation == "2":
        demand = input("What type of product are you looking for? : ")
        product.find_product(demand)

    elif operation == "3":
        sold_product = input("Which product was sold? : ")
        product.sell_product(sold_product)

    elif operation == "4":
        print("Please type the demanding informations:")
        name = input("Name of the Product:")
        pro_type = input("Type of the product:")
        expiration_date = input("Expiration Date of the Product:")
        price = input("Price of the Product:")
        new_product = Products(name, pro_type, expiration_date, price)
        product.add_product(new_product)
        print("New product added.")

    else:
        print("Invalid Operation...")








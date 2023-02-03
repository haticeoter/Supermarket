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
        pass
    elif operation == "2":
        pass
    elif operation == "3":
        pass
    elif operation == "4":
        pass
    else:
        print("Invalid Operation...")








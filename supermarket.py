import sqlite3

class Products():
    def __init__(self, name, pro_type, expiration_date, price):
        self.name = name
        self.pro_type = pro_type
        self.expiration_date = expiration_date
        self.price = price

    def __str__(self):
        return "Product Name: {}\nProduct Type: {}\nExpiration Date of the Product: {}\nPrice: {}"\
            .format(self.name, self.pro_type, self.expiration_date, self.price)

class Supermarket():
    safe = 0
    def __init__(self):
        self.get_connect()

    def get_connect(self):
        self.connect = sqlite3.connect("supermarket.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS supermarket (Name TEXT, Type TEXT, Expiration_Date TEXT, Price INT)")
        self.connect.commit()

    def add_product(self, product):
        self.cursor.execute("INSERT INTO supermarket VALUES(?,?,?,?)",
                            (product.name, product.pro_type, product.expiration_date, product.price))
        self.connect.commit()

    def find_product(self, type):
        self.cursor.execute("Select * From supermarket where type = ?", (type,))
        products = self.cursor.fetchall()

        if (len(products) == 0):
            print("There is no product of this type")
        else:
            for product in products:
                stuff = Products(product[0], product[1], product[2], product[3])
                print(stuff)

    def sell_product(self, name):
        self.cursor.execute("SELECT * FROM supermarket WHERE name = ?", (name,))
        product = self.cursor.fetchone()
        if product:
            self.cursor.execute("DELETE FROM supermarket WHERE name = ?", (name,))
            Supermarket.safe += int(product[3])
            print("Safe: {}".format(Supermarket.safe))
            self.connect.commit()
            print("Product was sold.")
        else:
            print("There is no such a product")

    def show_products(self):
        self.cursor.execute("Select * From supermarket")
        products = self.cursor.fetchall()
        if len(products) == 0:
            print("There is no product yet.")
        else:
            for i in products:
                product = Products(i[0], i[1], i[2], i[3])
                print(product)




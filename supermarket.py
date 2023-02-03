import sqlite3

class Products():
    def __init__(self, name, type, expiration_date, price):
        self.name = name
        self.type = type
        self.expiration_date = expiration_date
        self.price = price

    def __str__(self):
        return "Product Name: {}\nProduct_Type: {}\nExpiration Date of the Product: {}\nPrice: {}"\
            .format(self.name, self.type, self.expiration_date, self.price)

class Supermarket():
    def __init__(self):
        self.get_connect()

    def get_connect(self):
        self.connect = sqlite3.connect("supermarket.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS supermarket (Name TEXT, Type TEXT, Expiration_Date TEXT, Price INT)")
        self.connect.commit()

    def add_product(self, product):
        self.cursor.execute("INSERT INTO supermarket VALUES(?,?,?,?)",
                            (product.name, product.type, product.expiration_date, product.price))
        self.connect.commit()

    def find_product(self):
        self.cursor.execute("Select * From supermarket where type = ?", (type,))
        product = self.cursor.fetchall()

        if (len(product) == 0):
            print("There is no product of this type")
        else:
            stuff = Products(product[0][0], product[0][1], product[0][2], product[0][3])
            print(stuff)

    def sell_product(self, name):
        self.cursor.execute("Delete From supermarket where name = ?", (name,))
        self.connect.commit()
        product = self.cursor.fetchall()
        safe = 0
        for i in name:
            safe += product[0][3]


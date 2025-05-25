class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

        # getting for the price attribute
    @property
    def price(self):
        return self._price

    # setting for the price attribute
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value


            #deleer to dlete price attribut
    @price.deleter
    def price(self):   
        print(f"Deleting price of {self.name}")
        del self._price

    # creating a product object
product = Product("Laptop", 1000)


#accessing the price using @property
print(product.price) 

# updating the price using @price.setter
product.price = 1200
print(product.price)

# trying to set a negative price
product.price = -500  # This will trigger the setter validation     

# deleting the price using @price.deleter
del product.price  # This will trigger the deleter method
























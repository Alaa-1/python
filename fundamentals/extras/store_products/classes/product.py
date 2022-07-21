from uuid import uuid4

# Creating a product class
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        # giving a unique id to every instance overkill for this example
        self.uid = uuid4().hex

    def update_price(self, percent_change, is_increased):

        change_value = (self.price / 100) * percent_change
        if is_increased:
            self.price += change_value
        else:
            self.price -= change_value
        return self

    def print_info(self):
        print(
            f"UID: {self.uid} ** Product name: {self.name}, category: {self.category}, price: {self.price:.2f}$"
        )
        return self

# Creating a Store class
class Store:
    # products_list = []

    def __init__(self, name):
        self.name = name
        self.products_list = list()

    # takes a product and adds it to the store
    def add_product(self, new_product):
        self.products_list.append(new_product)
        return self

    # remove the product from the store's list of products given the id
    def sell_product(self, id):
        if id < len(self.products_list):
            self.products_list.pop(id)
        return self

    # increases the price of each product by the percent_increase given
    # (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for item in self.products_list:
            item.update_price(percent_increase, is_increased=True)
        return self

    # updates all the products matching the given category by
    # reducing the price by the percent_discount given
    def set_clearance(self, category, percent_discount):
        pass


# Creating a product class
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):

        change_value = (self.price / 100) * percent_change
        if is_increased:
            self.price += change_value
        else:
            self.price -= change_value
        return self

    def print_info(self):
        print(
            f"Product name: {self.name}, category: {self.category}, price: {self.price}$"
        )
        return self


earbuds = Product("AirPods pro", 250, "Accessories")
smartphone = Product("iPhone 13", 999, "iPhone")
laptop = Product("MacBook Air", 1199, "Mac")
my_store = Store("Nothing Store")
# testing classes
# earbuds.print_info()
# smartphone.update_price(10, True).print_info()

my_store.add_product(earbuds).add_product(smartphone).add_product(laptop)

print("product prices")
for prod in my_store.products_list:
    prod.print_info()

my_store.inflation(0.5)
print("product prices after after inflation")

for prod in my_store.products_list:
    prod.print_info()


# TODO:
# ?NINJA BONUS: Modularize your code into 3 separate files
# ??NINJA BONUS: Modularize your code into 3 separate files
# ???SENSEI BONUS: Update the product class to give each product a unique id.
# ??? Update the sell_product method to accept the unique id.

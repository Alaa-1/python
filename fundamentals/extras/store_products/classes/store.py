from . import product

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
        for item in self.products_list:
            print(f"given id: {id} ***** product id: {item.uid}")
            if item.uid == id:
                print("Found !!!")
                self.products_list.remove(item)
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
        for product in self.products_list:
            if product.category == category:
                product.update_price(percent_discount, is_increased=False)
        return self

from classes.store import Store
from classes.product import Product

if __name__ == "__main__":

    # testing classes
    earbuds_1 = Product("AirPods pro", 250, "Accessories")
    earbuds_2 = Product("Bose", 380, "Accessories")
    smartphone = Product("iPhone 13", 999, "iPhone")
    laptop = Product("MacBook Air", 1199, "Mac")
    my_store = Store("Nothing Store")
    # earbuds.print_info()
    # smartphone.update_price(10, True).print_info()

    my_store.add_product(earbuds_1).add_product(earbuds_2).add_product(
        smartphone
    ).add_product(laptop)

    # print("-- product prices --")
    # for prod in my_store.products_list:
    #     prod.print_info()

    # my_store.inflation(0.5)
    # print("---- product prices after after inflation ----")

    # for prod in my_store.products_list:
    #     prod.print_info()

    # my_store.set_clearance("Mac", 25)
    # print("------ product prices after after clearance ------")

    # for prod in my_store.products_list:
    #     prod.print_info()
    # print("*" * 20)

    earbuds_id = my_store.products_list[0].uid

    my_store.sell_product(earbuds_id)

    for prod in my_store.products_list:
        prod.print_info()

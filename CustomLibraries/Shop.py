from robot.api.deco import library, keyword
from SeleniumLibrary import SeleniumLibrary



@library
class Shop:

    def __init__(self):
        self.selLib = SeleniumLibrary()

    @keyword
    def hello_Buddies(self):
        print("Congratulation!!! You created Class, Method, Custom Keyword")

    @keyword
    def add_items_into_cart_checkout(self,product_list):
        i=1
        product_tittles=self.selLib.get_webelements("xpath: //h4[@class='card-title']")
        for product_tittle in product_tittles:
            if product_tittle.text in product_list:
                self.selLib.click_button("xpath: (//button[@class='btn btn-info'])[i]")

            i=i+1


from robot.libraries.BuiltIn import BuiltIn

class ProductPage:
    def __init__(self):
        # Attach to the SeleniumLibrary instance already loaded in Robot
        self.selib = BuiltIn().get_library_instance('SeleniumLibrary')

    def get_product_price_by_name(self, product_name):
        locator = f"xpath://div[text()='{product_name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
        price_text = self.selib.get_text(locator)
        return float(price_text.replace("$", ""))

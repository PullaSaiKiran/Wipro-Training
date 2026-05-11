from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.cart_page import CartPage
def test_navigate_to_laptops(driver):
    driver.get("https://www.demoblaze.com/index.html")
    home = HomePage(driver)

    assert home.click_laptops().verify_laptop_list_presence()

def test_phones_category(driver):
    driver.get("https://www.demoblaze.com/index.html")
    home = HomePage(driver)

    product_names = home.click_phones().get_all_product_names()

    assert "Samsung galaxy s6" in product_names, "Samsung galaxy s6 not found in Phones category!"

def test_add_sony_vaio_i5_to_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    home = HomePage(driver)

    product_page = home.click_sony_vaio_i5()
    assert product_page.add_product_to_cart()


def test_checkout_flow(driver):
    driver.get("https://www.demoblaze.com/index.html")
    home = HomePage(driver)

    # Navigate to Cart
    driver.find_element(By.ID, "cartur").click()
    cart = CartPage(driver)

    # Place Order → Fill Modal
    modal = cart.click_place_order()
    data = {
        "name": "Sai Kiran",
        "country": "India",
        "city": "Hyderabad",
        "card": "1234567890123456",
        "month": "05",
        "year": "2026"
    }
    modal.fill_purchase_form(data)

    assert modal.verify_success_message()

def test_login_wrong_password(driver):
    driver.get("https://www.demoblaze.com/index.html")
    home = HomePage(driver)

    modal = home.open_login_modal()
    alert_text = modal.login("testuser", "wrongpassword")

    # Intentionally failing assertion
    assert alert_text == "Success", f"Expected 'Success' but got '{alert_text}'"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

def before_scenario(context, scenario):
    print("before_scenario")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    ).send_keys("Admin")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"{scenario.name}_{timestamp}.png")
        context.driver.save_screenshot(screenshot_path)
    context.driver.quit()

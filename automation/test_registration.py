import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_user_registration(driver):
    url = "https://skillshikshya.com/register"
    driver.get(url)

    # Fill registration form
    driver.find_element(By.NAME, "name").send_keys("Pramod Test")
    driver.find_element(By.NAME, "email").send_keys("pramodqa@example.com")
    driver.find_element(By.NAME, "password").send_keys("Test@123")
    driver.find_element(By.NAME, "confirm_password").send_keys("Test@123")

    # Click register (if the button text is Register, change if different)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    # Validate success or error message
    assert "registered" in driver.page_source.lower() or "verify" in driver.page_source.lower()

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


def test_user_login(driver):
    url = "https://skillshikshya.com/login"
    driver.get(url)

    # Login form
    driver.find_element(By.NAME, "email").send_keys("pramodqa@example.com")
    driver.find_element(By.NAME, "password").send_keys("Test@123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(3)

    # Validate login success by checking user dashboard/menu
    assert "dashboard" in driver.page_source.lower() or "logout" in driver.page_source.lower()

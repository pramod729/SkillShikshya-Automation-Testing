import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_enroll_form_valid_submission(driver):
    driver.get("https://skillshikshya.com/enroll-form")

    # Fill email
    driver.find_element(By.NAME, "email").send_keys("pramod.qa@gmail.com")

    # Select "Interested Course"
    select_course = Select(driver.find_element(By.NAME, "interested_course"))
    select_course.select_by_index(1)

    # Enter name
    driver.find_element(By.NAME, "name").send_keys("Pramod Tester")

    # Phone
    driver.find_element(By.NAME, "phone").send_keys("9812345678")

    # Address
    driver.find_element(By.NAME, "address").send_keys("Kathmandu, Nepal")

    # Mode of training (radio or select)
    try:
        driver.find_element(By.XPATH, "//label[text()='Online']").click()
    except:
        Select(driver.find_element(By.NAME, "training_mode")).select_by_visible_text("Online")

    # Preferred shift
    Select(driver.find_element(By.NAME, "preferred_shift")).select_by_visible_text("Day")

    # Timing info
    driver.find_element(By.NAME, "timing").send_keys("10:00 AM - 4:00 PM")

    # Laptop ownership
    driver.find_element(By.XPATH, "//label[text()='Yes']").click()

    # College / Institution
    driver.find_element(By.NAME, "college").send_keys("Kathmandu University")

    # Grade
    Select(driver.find_element(By.NAME, "grade")).select_by_index(1)

    # Parent phone
    driver.find_element(By.NAME, "parent_phone").send_keys("9800001111")

    # Referred by
    driver.find_element(By.NAME, "referral_email").send_keys("friend@example.com")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(3)

    # Verify success (message or URL change)
    page_text = driver.page_source.lower()
    assert "thank" in page_text or "success" in page_text

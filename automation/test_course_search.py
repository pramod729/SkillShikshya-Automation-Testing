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


def test_course_search(driver):
    url = "https://skillshikshya.com/"
    driver.get(url)

    # Search course
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("QA")
    search_box.submit()

    time.sleep(3)

    # Validate results
    assert "qa" in driver.page_source.lower() or "quality" in driver.page_source.lower()

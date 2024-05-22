import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 60)
    driver.get('https://www.yatra.com/')
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()
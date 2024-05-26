import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='function')
def setup(request):
    driver = webdriver.Edge()
    driver.get('https://www.yatra.com/')
    driver.maximize_window()
    request.cls.driver = driver

    yield

    driver.quit()
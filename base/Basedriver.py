import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def visibility_of_element(self, xpath):
        wait = WebDriverWait(self.driver, 60)
        try:
            return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            print(f"Unable to find element - {e}")
    
    def visibility_of_all_elements(self, xpath):
        wait = WebDriverWait(self.driver, 60)
        try:
            return wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        except Exception as e:
            print(f"Unable to find elements - {e}")
        
    def click_on_element(self, elm):
        try:
            elm.click()
            time.sleep(1)
        except Exception as e:
            print(f"Unable to click element - {e}")

    def send_keys(self, elm, key_inp):
        try:
            elm.send_keys(key_inp)
            time.sleep(1)
        except Exception as e:
            print(f"Unable to send keys - {e}")
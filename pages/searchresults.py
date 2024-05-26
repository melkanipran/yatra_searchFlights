import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.xpaths import *
from base.Basedriver import BaseDriver

class SearchResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_stops(self, total_stop):
        stop_btn = self.visibility_of_element(STOPS_BTN.format(total_stop))
        self.click_on_element(stop_btn)

    # def scroll_down(self):
        # for i in range(10):
        #     self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #     time.sleep(3)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//*[contains(@class,'copyright ')]"))

    def assert_stops(self):
        self.visibility_of_element(STOP_DETAILS)
        stop_list = self.visibility_of_all_elements(STOP_DETAILS)
        print("Total Stops : " + str(len(stop_list)))
        for stop in stop_list:
            print(stop.text)
            assert "1 Stop" in stop.text
            print("Assert pass")
       
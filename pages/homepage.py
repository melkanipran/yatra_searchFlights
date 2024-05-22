from base.xpaths import *
from base.Basedriver import BaseDriver

class Homepage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def close_iframe(self):
        iframe = self.visibility_of_element(IFRAME)
        self.driver.switch_to.frame(iframe)
        close_btn = self.visibility_of_element(DENY_BTN)
        self.click_on_element(close_btn)
        self.driver.switch_to.default_content()

    def fill_from_field(self, origin_city):
        from_loc_field = self.visibility_of_element(FROM_LOC_FIELD)
        self.click_on_element(from_loc_field)
        self.send_keys(from_loc_field, origin_city)
        from_city = self.visibility_of_element(REQUIRED_ORIGIN_CITY.format(origin_city))
        self.click_on_element(from_city)

    def fill_to_field(self, dest_city):
        to_loc_field = self.visibility_of_element(TO_LOC_FIELD)
        self.click_on_element(to_loc_field)
        self.send_keys(to_loc_field, dest_city)
        to_city = self.visibility_of_element(REQUIRED_DEST_CITY.format(dest_city))
        self.click_on_element(to_city)

    def select_departure_date(self, travel_date):
        date_field = self.visibility_of_element(DEPARTURE_DATE_FIELD)
        self.click_on_element(date_field)
        date_list = self.visibility_of_all_elements(DATE_LIST)
        for dt in date_list:
            print(dt.get_attribute('id'))
            if dt.get_attribute('id') == travel_date:
                self.click_on_element(dt)
                break

    def click_search_flights_btn(self):
        search_btn = self.visibility_of_element(SEARCH_FLIGHTS_BTN)
        self.click_on_element(search_btn)
    
    def search_flights(self, origin, destination, travelDate):
        self.fill_from_field(origin)
        self.fill_to_field(destination)
        self.close_iframe()
        self.select_departure_date(travelDate)
        self.click_search_flights_btn()
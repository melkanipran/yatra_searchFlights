from base.xpaths import *
from base.Basedriver import BaseDriver

class Homepage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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


    def click_buses_icon(self):
        bus_icon = self.visibility_of_element(BUSES_ICON)
        self.click_on_element(bus_icon)

    def fill_depart_from_field(self, from_city):
        from_field = self.visibility_of_element(BUS_ORIGIN_FIELD)
        self.send_keys(from_field, from_city)
        origin_city = self.visibility_of_element(BUS_REQ_FROM_TO_CITY.format(from_city))
        self.click_on_element(origin_city)

    def fill_depart_to_field(self, to_city):
        to_field = self.visibility_of_element(BUS_DEST_FIELD)
        self.send_keys(to_field, to_city)
        dest_city = self.visibility_of_element(BUS_REQ_FROM_TO_CITY.format(to_city))
        self.click_on_element(dest_city)

    def select_bus_departure_date(self, travel_date):
        date_field = self.visibility_of_element(BUS_DATE_FIELD)
        date_field.click()
        date_list = self.visibility_of_all_elements(DATE_LIST)
        for dt in date_list:
            print(dt.get_attribute('id'))
            if dt.get_attribute('id') == travel_date:
                self.click_on_element(dt)
                break

    def click_search_buses_btn(self):
        search_bus_btn = self.visibility_of_element(SEARCH_BUSES_BTN)
        self.click_on_element(search_bus_btn)

    def search_buses(self, origin, destination, travelDate):
        self.click_buses_icon()
        self.fill_depart_from_field(origin)
        self.fill_depart_to_field(destination)
        self.select_bus_departure_date(travelDate)
        self.click_search_buses_btn()
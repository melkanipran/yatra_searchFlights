from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, pytest
from pages.homepage import Homepage
from pages.searchresults import SearchResult


@pytest.mark.usefixtures("setup")
class TestCheckFlights:
    def test_check_flight_stops(self):

        hp = Homepage(self.driver, self.wait)
        hp.search_flights("JFK", "BOM", "10/06/2024")
        
        sr = SearchResult(self.driver, self.wait)
        sr.select_stops("1")
        # sr.scroll_down()
        sr.assert_stops()



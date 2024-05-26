import time, pytest
from pages.homepage import Homepage
from pages.searchresults import SearchResult


@pytest.mark.usefixtures("setup")
class TestCheckFlightStops:
    @pytest.mark.skip()
    def test_check_flight_stops(self):

        hp = Homepage(self.driver)
        hp.search_flights("JFK", "BOM", "10/06/2024")
        
        sr = SearchResult(self.driver)
        sr.select_stops("1")
        # sr.scroll_down()
        sr.assert_stops()



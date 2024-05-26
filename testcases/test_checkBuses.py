import pytest, time
from pages.homepage import Homepage


@pytest.mark.usefixtures("setup")
class TestCheckBusStops:

    @pytest.mark.parametrize("origin, destination, travelDate", 
                             [("Sarai kale khan", "Haldwani", "05/07/2024"), ("Sarai kale khan", "Jaipur", "05/07/2024")])
    def test_check_bus_ticketprice(self, origin, destination, travelDate):

        hp = Homepage(self.driver)
        hp.search_buses(origin, destination, travelDate)
        self.driver.back()

        time.sleep(5)


        
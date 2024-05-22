# HOME PAGE
IFRAME = "//*[@id='webpush-onsite']"
DENY_BTN = "//*[@id='deny']"
FROM_LOC_FIELD = "//*[@id='BE_flight_origin_city']"
REQUIRED_ORIGIN_CITY = "//*[@class='ac_results origin_ac']//*[contains(text(),'{}')]"
TO_LOC_FIELD = "//*[@id='BE_flight_arrival_city']"
REQUIRED_DEST_CITY = "//*[@class='ac_results dest_ac']//*[contains(text(),'{}')]"
DEPARTURE_DATE_FIELD = "//*[@id='BE_flight_origin_date']"
DATE_LIST = "//*[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"
REQUIRED_DATE = "//*[@id='monthWrapper']//tbody//td[@id='{}']"
SEARCH_FLIGHTS_BTN = "//*[@value='Search Flights']"


# SEARCH RESULT PAGE
STOPS_BTN = "//*[contains(@class,'filter-stops')]//p[text()='{}']"
STOP_DETAILS = "//*[contains(@class,'stop-cont')]//span"
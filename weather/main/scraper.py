from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def weather_scrape(location):
    try:
        #open the web driver and open the url
        driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
        url = 'https://worldweather.wmo.int/en/home.html'
        driver.get(url)
        
        #find the city
        search_bar = driver.find_element_by_id('q_search')
        search_bar.send_keys(location)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(10) 
        driver.refresh()

        #get the forecast data
        current_weather = []
        current_temperature = driver.find_element_by_class_name('present_temp_value')
        current_weather.append(current_temperature.text)
        current_humidity = driver.find_element_by_class_name('present_rh_value')
        current_weather.append(current_humidity.text)
        current_wind = driver.find_element_by_class_name('present_wind_value')
        current_weather.append(current_wind.text)
        forecast_sparse_data = driver.find_elements_by_class_name('city_forecast_day_object')
        forecast_formatted_data = []

        for day in forecast_sparse_data:
            d = []
            l = day.text.split('\n')
            d.append(l[0])
            d.append(l[2])
            d.append(l[3])
            forecast_formatted_data.append(d)

        return current_weather, forecast_formatted_data
    except:
        return False, False   

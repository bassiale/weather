from bs4 import BeautifulSoup     
from selenium import webdriver

def weather_scrape(location):
    try:

        driver=webdriver.Chrome()
             
        driver.get(f"https://www.google.com/search?q={location}+weather")
        soup=BeautifulSoup(driver.page_source,"lxml")

        place=soup.find('div',id="wob_loc").text
        when=soup.find('div',id="wob_dts").text
        nature=soup.find('span',id="wob_dc").text


        current=soup.find('span',class_="wob_t").text
        precip=soup.find('span',id="wob_pp").text
        humid=soup.find('span',id="wob_hm").text
        wind=soup.find('span',id="wob_ws").text

        print(f"{place}\n{when}\n{nature}\n{current}\n{precip}\n{humid}\n{wind}")
        return place,when,nature,current,precip,humid,wind

    except:
        return False, False
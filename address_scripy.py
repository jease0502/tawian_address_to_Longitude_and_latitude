from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


class Address_scripy(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

    def get_address(self, addr: str):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("http://www.map.com.tw/")
        search = self.browser.find_element_by_id("searchWord")
        search.clear()
        search.send_keys(addr)
        self.browser.find_element_by_xpath(
            "/html/body/form/div[10]/div[2]/img[2]").click()
        # /html/body/form/div[4]/table/tbody/tr[3]/td/table/tbody/tr/td[2]
        time.sleep(2)
        iframe = self.browser.find_elements_by_tag_name("iframe")[1]
        self.browser.switch_to.frame(iframe)
        time.sleep(3)
        coor_btn = self.browser.find_element_by_xpath(
            "/html/body/form/div[4]/table/tbody/tr[3]/td/table/tbody/tr/td[2]")
        coor_btn.click()
        coor = self.browser.find_element_by_xpath(
            "/html/body/form/div[5]/table/tbody/tr[2]/td")
        coor = coor.text.strip().split(" ")
        lat = coor[-1].split("：")[-1]
        log = coor[0].split("：")[-1]
        return lat, log

    def quiz_browser(self) -> None:
        self.browser.quit()

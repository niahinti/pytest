from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from pages.LayoutPage import LayoutPage


class AcademyPage(LayoutPage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "subtitle": (By.CSS_SELECTOR, '.sub-title')
    }

    def getSubtitleText(self):
        self.waitUntilElementIsVisible(self.locators["subtitle"])
        return self.driver.find_element(*self.locators["subtitle"]).text

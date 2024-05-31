from selenium.webdriver.common.by import By
from UI.pages.LayoutPage import LayoutPage


class AcademyPage(LayoutPage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "subtitle": (By.CSS_SELECTOR, '.sub-title')
    }

    def getSubtitleText(self):
        self.waitUntilElementIsVisible(self.locators["subtitle"])
        return self.driver.find_element(*self.locators["subtitle"]).text

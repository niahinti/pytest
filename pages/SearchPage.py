from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from pages.LayoutPage import LayoutPage


class SearchPage(LayoutPage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "searchResults": (By.CSS_SELECTOR, '.search-page__list')
    }

    def inputSearch(self, text):
        self.waitUntilElementIsVisible(LayoutPage.locators["searchInput"])
        self.driver.find_element(*LayoutPage.locators["searchInput"]).send_keys(text)
        self.driver.find_element(*LayoutPage.locators["searchInput"]).send_keys(Keys.ENTER)

    def clickSearchResult(self, text):
        time.sleep(3)
        self.waitUntilElementIsVisible(self.locators["searchResults"])
        searchResults = self.driver.find_elements(By.XPATH, '//div[@class="search-page__list"]//h3')
        for result in searchResults:
            if result.text == text:
                result.click()
                break

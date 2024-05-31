from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class LayoutPage():
    def __init__(self, driver):
        self.driver = driver

    def getPageTitle(self):
        return self.driver.title

    def waitUntilElementIsVisible(self: object, locator: tuple):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def clickSearchBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, '.menu__search-image').click()
        self.waitUntilElementIsVisible((By.CSS_SELECTOR, '.form-input__text'))

    def switch_to_new_tab(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])

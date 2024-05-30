import pytest
from pytest_bdd import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


##########################################
## POMs
##########################################

class LayoutPage():
    def __init__(self, driver):
        self.driver = driver

    def getPageTitle(self):
        return self.title

    def waitUntilElementIsVisible(self: object, locator: tuple):
        return WebDriverWait(self, 10).until(EC.visibility_of_element_located(locator))

    def clickSearchBtn(self):
        self.find_element(By.CSS_SELECTOR, '.menu__search-image').click()


class HomePage(LayoutPage):
    def __init__(self, driver):
        super().__init__(driver)


class SearchPage(LayoutPage):
    def __init__(self, driver):
        super().__init__(driver)

    def waitUntilPageLoads(self):
        self.waitUntilElementIsVisible((By.CSS_SELECTOR, '.form-input__text'))

    def inputSearch(self, text):
        self.find_element(By.CSS_SELECTOR, '.form-input__text').send_keys(text)
        self.find_element(By.CSS_SELECTOR, '.form-input__text').send_keys(Keys.ENTER)


##########################################
## Step definitions
##########################################


@pytest.fixture
def browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    driver.get("https://www.softserveinc.com/")
    yield driver
    driver.quit()


@scenario("../features/SoftServeSearch.feature", "Search for Academy Page")
def test_setUp(browser):
    pass


@given("Im on SoftSearch main page with title 'SoftServe | Software Development & Digital Services Company'")
def main_page_title(browser):
    param = 'SoftServe | Software Development & Digital Services Company'
    print(f"Im on SoftSearch main page with title '{param}'")
    assert HomePage.getPageTitle(browser) == 'SoftServe | Software Development & Digital Services Company'


@when("I click on the search icon")
def click_search_icon(browser):
    print("I click on the search icon")
    HomePage.clickSearchBtn(browser)
    SearchPage.waitUntilElementIsVisible(browser, (By.CSS_SELECTOR, '.form-input__text'))
    assert SearchPage.getPageTitle(browser) == 'Search | SoftServe'


@when("I type 'Academy' in the search box in Search Page")
def type_search_term(browser):
    param = 'Academy'  # param would be received from cucumber step but it's failing to recognize step definition
    print(f"I type '{param}' in the search box in Search Page")
    SearchPage.inputSearch(browser, param)


@when("I click on 'IT Academy' search result in Search Page")
def click_search_result(browser):
    param = 'IT Academy'
    print(f"I click on '{param}' search result in Search Page")


@then("I should see 'SoftServe Academy' page title")
def check_page_title(browser):
    param = 'SoftServe Academy'
    print(f"I should see '{param}' page title")


@then("I should see 'Empowering learning solutions to start your career in IT.' subtitle on SoftServe Academy page")
def check_page_subtitle(browser):
    param = 'Empowering learning solutions to start your career in IT.'
    print(
        f"I should see '{param}' subtitle on SoftServe Academy page")

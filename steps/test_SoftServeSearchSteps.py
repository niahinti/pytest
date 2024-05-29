import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pytest_bdd import scenario, given, when, then

@pytest.mark.usefixtures("web_driver")

@pytest.fixture(scope="class")
def web_driver(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    driver.get("https://www.softserveinc.com/")
    yield
    driver.close()

@scenario("SoftServeSearch.feature", "Search for Academy Page")
def test_setUp(web_driver, capsys):
    pass

@given("I'm on SoftSearch main page")
def launchBrowser(web_driver, capsys):
    # driver = web_driver
    # title = driver.title
    # with capsys.disabled():
    # print(title)
    # SoftServe | Software Development & Digital Services Company
    with capsys.disabled():
        print("I'm on SoftSearch main page")

@when('I click on the search icon')
def click_search_icon(capsys):
    with capsys.disabled():
      print("I click on the search icon")

@when('I type "Academy" in the search box in Search Page')
def type_search_term(capsys):
    with capsys.disabled():
        print(f"I type 'Academy' in the search box in Search Page")

@when('I click on "IT Academy" search result in Search Page')
def click_search_result(capsys):
    with capsys.disabled():
        print(f'I click on "IT Academy" search result in Search Page')

@then('I should see "SoftServe Academy" page title')
def check_page_title(capsys):
    with capsys.disabled():
        print(f'I should see "SoftServe Academy" page title')

@then('I should see "Empowering learning solutions to start your career in IT." subtitle on SoftServe Academy page')
def check_page_subtitle(capsys):
    with capsys.disabled():
        print(f'I should see "Empowering learning solutions to start your career in IT." subtitle on SoftServe Academy page')

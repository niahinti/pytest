import pytest
from pytest_bdd import *
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    driver.get("https://www.softserveinc.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def global_state():
    return {}

@pytest.fixture
def response():
    return {}
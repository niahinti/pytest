from pytest_bdd import *
from pytest_bdd import parsers
from UI.pages.HomePage import HomePage
from UI.pages.SearchPage import SearchPage
from UI.pages.AcademyPage import AcademyPage
from conftest import browser


@scenario("../features/SoftServeSearch.feature", "Search for Academy Page")
def test_setUp(browser):
    pass


@given(parsers.parse("Im on SoftSearch main page with title \"{title}\""))
def main_page_title(browser, title):
    print(f"Im on SoftSearch main page with title '{title}'")
    assert HomePage(browser).getPageTitle() == title


@when(parsers.parse("I click on the search icon"))
def click_search_icon(browser):
    print("I click on the search icon")
    HomePage(browser).clickSearchBtn()
    assert SearchPage(browser).getPageTitle() == 'Search | SoftServe'


@when(parsers.parse("I type \"{searchTerm}\" in the search box in Search Page"))
def type_search_term(browser, searchTerm):
    print(f"I type '{searchTerm}' in the search box in Search Page")
    SearchPage(browser).inputSearch(searchTerm)


@when(parsers.parse("I click on \"{result}\" search result in Search Page"))
def click_search_result(browser, result):
    print(f"I click on '{result}' search result in Search Page")
    SearchPage(browser).clickSearchResult(result)


@then(parsers.parse("I should see \"{title}\" page title"))
def check_page_title(browser, title):
    param = 'SoftServe Academy'
    print(f"I should see '{title}' page title")
    SearchPage(browser).switch_to_new_tab()
    assert AcademyPage(browser).getPageTitle() == title


@then(parsers.parse("I should see \"{subtitle}\" subtitle on SoftServe Academy page"))
def check_page_subtitle(browser, subtitle):
    print(f"I should see '{subtitle}' subtitle on SoftServe Academy page")
    actual_subtitle = AcademyPage(browser).getSubtitleText()
    assert actual_subtitle == subtitle
    print(f"Subtitle displayed: {actual_subtitle}")

from behave import given, when, then
from selenium.webdriver.common.by import By

search_field = (By.CSS_SELECTOR, "input#searchval")
search_button = (By.CSS_SELECTOR, "button.banner-search-btn")
links = (By.CSS_SELECTOR, "a.description")
buyButton = (By.CSS_SELECTOR, "input#buyButton")
cart_icon = (By.CSS_SELECTOR, "span.btn-primary span.menu-btn-text")
empty_cart = (By.CSS_SELECTOR, "span.btn-primary span.menu-btn-text")


@given('Open web page')
def web_site(context):
    context.driver.get('https://www.webstaurantstore.com/')


@when('Search for {search_word}')
def search_for(context, search_word):
    field = context.driver.find_element(*search_field)
    field.clear()
    field.send_keys(search_word)
    search = context.driver.find_element(*search_button)
    search.click()


@then('Check the search result ensuring every product item has the word Table its title')
def check_result(context):
    all_links = context.driver.find_elements(*links)
    for i in all_links:
        #print(i.text)
        assert 'Table' in i.text, f'Expected Table in {i.text}'


@then('Add the last of found items to Cart.')
def add_cart(context):
    all_links = context.driver.find_elements(*links)
    all_links[-1].click()
    button = context.driver.find_element(*buyButton).click()


@then('Empty Cart.')
def empty_card(context):
    cart = context.driver.find_element(*cart_icon).click()
    empty = context.driver.find_element(*empty_cart).click()
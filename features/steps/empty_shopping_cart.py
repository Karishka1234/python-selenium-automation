from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

cart_icon=(By.CSS_SELECTOR, "span#nav-cart-count")
empty_cart=(By.CSS_SELECTOR, "h1.sc-empty-cart-header")

@given ('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('User clicks on cart icon')
def click_on_cart(context):
    context.driver.find_element(*cart_icon).click()
    sleep(1)

@then ('Verify that page contains {search_word}')
def is_empty(context, search_word):
    result = context.driver.find_element(*empty_cart).text
    assert search_word in result, "Expected word '{}' in message, but got '{}'".format(search_word, result)


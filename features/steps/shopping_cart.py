from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

search_box = (By.CSS_SELECTOR, "input#twotabsearchtextbox")
click_button1 = (By.CSS_SELECTOR, "input.nav-input")
products_needed = (By.CSS_SELECTOR, "span.a-price-whole")
subtotal = (By.XPATH, "//span[contains(text(), '2 items')]")
cart_icon = (By.CSS_SELECTOR, "a#nav-cart")
to_cart = (By.CSS_SELECTOR, "input#add-to-cart-button")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {product} in to search field')
def product_search(context, product):
    search = context.driver.find_element(*search_box)
    search.clear()
    search.send_keys(product)
    sleep(4)


@when('Click on search button')
def click_button(context):
    context.driver.find_element(*click_button1).click()
    sleep(1)


@when('Find toys')
def find_product(context):
    context.driver.find_element(*products_needed).click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "span.a-button-text").click()
    context.driver.find_element(By.CSS_SELECTOR, "a#quantity_1").click()
    sleep(1)


@then('Add {product} to a shopping cart')
def add_to_cart(context, product):
    context.driver.find_element(*to_cart).click()
    sleep(4)


@then('Close side window')
def close_window(context):
    window = context.driver.find_elements(By.ID, "attach-close_sideSheet-link")
    if len(window) == 1:
        window[0].click()
        sleep(2)


@then('Click to shopping cart')
def click_on_cart(context):
    context.driver.find_element(*cart_icon).click()
    sleep(1)


@then('Verify that {word} are there')
def is_there(context, word):
    search_word = context.driver.find_element(*subtotal).text
    assert word in search_word, "Expected '{}' in message, but got '{}'".format(word, search_word)



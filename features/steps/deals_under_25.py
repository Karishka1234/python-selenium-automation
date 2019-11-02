from behave import given, when, then
from selenium.webdriver.common.by import By


deals = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
today_deals = (By.CSS_SELECTOR, "div.gbh1-bold")
product = (By.CSS_SELECTOR, "a#dealTitle span.a-declarative")
add_to_cart_button = (By.CSS_SELECTOR, "input#add-to-cart-button")


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles


@when('Click to open Deals under 25')
def deals_under_25(context):
    context.driver.find_element(*deals).click()


@when('Switch to the newly opened window')
def switch_window(context):
    current_windows = context.driver.window_handles
    new_window = current_windows
    for w in context.old_windows:
        new_window.remove(w)
        context.driver.switch_to_window(new_window[0])


@when('{expected_header} is shown')
def deals_are_shown(context, expected_header):
    actual_header = context.driver.find_element(*today_deals).text
    assert actual_header == expected_header, f"Expected {expected_header}, but got {actual_header}"


@then('Add any product into a cart')
def add_to_cart(context):
    context.driver.find_element(*product).click()
    context.driver.find_element(*add_to_cart_button).click()
    no_thanks_button = context.driver.find_elements(By.CSS_SELECTOR, "button#attachSiNoCoverage-announce")
    close_button = context.driver.find_elements(By.CSS_SELECTOR, "a.close-button")
    if len(no_thanks_button) == 1:
        no_thanks_button[0].click()
    if len(close_button) == 1:
        close_button[0].click()


@then('User can close new window and switch back to original')
def close_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)


@then('Refresh the page')
def refresh(context):
    context.driver.refresh()


@then('Verify cart has {1} item')
def cart_item(context, item):
    items = context.driver.find_element(By.CSS_SELECTOR, "span#nav-cart-count").text
    print(items)
    assert item in items, f'Expected {item} item in shopping cart, but got {items}'
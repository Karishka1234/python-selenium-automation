from behave import given, when, then
from selenium.webdriver.common.by import By

orders_link_icon = (By.CSS_SELECTOR, "a#nav-orders")
sign_in = (By.CSS_SELECTOR, "div h1.a-spacing-small")


@when('Click Amazon Orders link')
def orders_link(context):
    # context.driver.find_element(*orders_link_icon).click()
    context.app.main_page.order_link()


@then('Verify {text} page is opened')
def sign_in_open(context, text):
    # actual = context.driver.find_element(*sign_in).text
    # assert text == actual, f'Expected text {text}, but got {actual}'
    context.app.sign_in_page.check_text(text)

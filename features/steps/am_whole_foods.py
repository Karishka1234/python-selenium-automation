from behave import given, when, then
from selenium.webdriver.common.by import By


items_on_sale = (By.CSS_SELECTOR, "ul.s-col-3 li")


@given('Open Amazon Whole Food page')
def open_url(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@when('Click on items on sale')
def sale_item(context):
    items = context.driver.find_elements(*items_on_sale)
    for i in items:
        i.click()


@then('Verify that every item has regular price')
def regular_text(context):
    context.driver.find_element()

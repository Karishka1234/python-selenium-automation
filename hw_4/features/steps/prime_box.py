from selenium.webdriver.common.by import By
from behave import given,when,then

boxes = (By.CSS_SELECTOR, "div.card-clickable")


@given('open amazon prime')
def prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('verify there are {number} boxes')
def boxes_num(context, number):
    box = context.driver.find_elements(*boxes)
    assert len(box) == 5

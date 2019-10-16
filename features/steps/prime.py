from behave import given, when, then
from selenium.webdriver.common.by import By


prime = (By.CSS_SELECTOR, "a.nav-sprite")
get_started = (By.CSS_SELECTOR, "a.nav-npt-a")
box = (By.CSS_SELECTOR, "div.benefit-container div.a-span6")


@given('Open Amazon web site')
def open_amazon(context):
   context.driver.get('https://www.amazon.com/')


@when('Click on TryPrime icon')
def click_prime(context):
    context.driver.find_element(*prime).click()
    context.driver.find_element(*get_started).click()


@then('Verify that page has {number} boxes')
def boxes(context, number):
    assert len(context.driver.find_elements(*box)) == 8
    #box_count = len(context.driver.find_elements(*box))
    #assert number == box_count, "Expected amount of boxes {number}, but i got {box_count}".format(number, box_count)






"""from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('cancel order')


sleep(4)

driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()
"""

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.XPATH, "//input[@id='helpsearch']")
SEARCH_SUBMIT = (By.CSS_SELECTOR, "input.a-button-input")
RESULTS_FOUND_MESSAGE = (By.CSS_SELECTOR, "div.help-content h1")
RESULTS = (By.CSS_SELECTOR, "div.help-content h1")


@given('Open help page on amazon web site')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into go field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on go icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('Results contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)

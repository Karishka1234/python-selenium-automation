from behave import given, when, then
from selenium.webdriver.common.by import By

actual_colors = (By.CSS_SELECTOR, "span div.tooltip")
available_colors = (By.CSS_SELECTOR, "div span.selection")


@given('Open product page')
def open_url(context):
    context.driver.get('https://www.amazon.com/dp/B07BKF1PT3/ref=twister_B07BKD8JCQ')


@then('Verify that user can choose colors')
def colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    colors = context.driver.find_elements(*actual_colors)
    for color in colors:
        color.click()
        available = context.driver.find_element(*available_colors).text
        assert expected_colors[colors.index(color)] == available

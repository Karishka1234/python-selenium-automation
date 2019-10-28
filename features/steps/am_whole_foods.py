from behave import given, when, then
from selenium.webdriver.common.by import By


items_on_sale = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")
product_name = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


@given('Open Amazon Whole Food page')
def open_url(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that every item has product name and regular price')
def sale_item(context):
    items = context.driver.find_elements(*items_on_sale)
    for i in items:
        product = i.find_elements(*product_name).text
        print(product)
        assert product != " ", f'Expected product name to be in text'
        assert 'Regular' in i.text, f'Expected Regular in {i.text}'


from behave import given, when, then
from selenium.webdriver.common.by import By

best_link = (By.XPATH, "//a[contains(text(), 'Best Sellers')]")
#header = (By.CSS_SELECTOR, "div#zg_banner_text_wrapper")


@when('User clicks on Best Seller link')
def best_seller(context):
    context.driver.find_element(*best_link).click()


@then('Click on each top link and verify that text updates')
def top_link_click(context):
    top_links = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs ul li")
    text = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
    for i in range(len(top_links)):
        top_link = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs ul li")
        top_link[i].click()
        top_link = context.driver.find_elements(By.CSS_SELECTOR, "div#zg_tabs ul li")
        for j in text:
            header_text = context.driver.find_element(By.CSS_SELECTOR, "div#zg_banner_text_wrapper").text
            assert text[i] in header_text, 'Expected {}, but got {}'.format(text[i], header_text)

from selenium.webdriver.common.by import By
from behave import given, when, then


address_bar = (By.ID, 'twotabsearchtextbox')
search = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
title = (By.CSS_SELECTOR, "span.a-size-medium")
badges = (By.CSS_SELECTOR, "span.a-badge-text")


@when('Send {book}')
def search_book(context, book):
    bar = context.driver.find_element(*address_bar)
    bar.send_keys(book)
    context.driver.find_element(*search).click()


@when('Count how many books would be shown in result list')
def count_book(context):
    count = context.driver.find_elements(*title)
    print(len(count))


@then('If last book has {label} label, will add it in the cart')
def has_label(context, label):
    badge = context.driver.find_elements(*badges)
    text = "Best Seller"
    if text in badge[-1].text:
        count = context.driver.find_elements(*title)
        count[-1].click()
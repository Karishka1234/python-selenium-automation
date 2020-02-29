from behave import given, when, then
from selenium.webdriver.common.by import By

hmenu_icon = (By.CSS_SELECTOR, "i.hm-icon")
am_music = (By.XPATH, "//a[@data-menu-id='3']//div[contains(text(),'Amazon Music')]")
actual_items = (By.CSS_SELECTOR, "ul.hmenu-visible li a:not(.hmenu-back-button")


@given('Open Amazon page')
def open_url(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_page()


@when('Click on hamburger menu')
def hamburger_menu(context):
    # menu = context.driver.find_element(*hmenu_icon)
    # menu.click()
    context.app.main_page.hmenu_click()


@when('Click on Amazon Music menu item')
def music_menu(context):
    # music = context.driver.find_element(*am_music)
    # music.click()
    context.app.main_page.am_music_click()


@then('{amount} menu items are present')
def items_present(context, amount):
    # items = context.driver.find_elements(*actual_items)
    # assert len(items) == int(expected_amount)
    context.app.main_page.items_amount(amount)

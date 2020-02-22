from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    orders_link_icon = (By.CSS_SELECTOR, "a#nav-orders")
    cart_icon = (By.CSS_SELECTOR, "span#nav-cart-count")
    hmenu_icon = (By.CSS_SELECTOR, "i.hm-icon")
    am_music = (By.XPATH, "//a[@data-menu-id='3']//div[contains(text(),'Amazon Music')]")
    actual_items = (By.CSS_SELECTOR, "ul.hmenu-visible li a:not(.hmenu-back-button")

    def order_link(self):
        self.click(*self.orders_link_icon)

    def cart_click(self):
        self.click(*self.cart_icon)

    def hmenu_click(self):
        self.click(*self.hmenu_icon)

    def am_music_click(self):
        self.click(*self.am_music)

    def open(self, url):
        self.open_page(url)

    def items_amount(self, amount):
        self.item_amount(amount, *self.actual_items)





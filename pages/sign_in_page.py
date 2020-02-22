from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):
    sign_in = (By.CSS_SELECTOR, "div h1.a-spacing-small")
    empty_cart = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")

    def check_text(self, expected_text):
        self.verify_text(expected_text, *self.sign_in)


    def check_text1(self, expected_text):
        self.verify_text(expected_text, *self.empty_cart)
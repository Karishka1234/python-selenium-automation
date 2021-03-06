from pages.main_page import MainPage
from pages.sign_in_page import SignIn


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignIn(self.driver)


from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    EMAIL = (By.CSS_SELECTOR, "#normal_login_username")
    PASSWORD = (By.CSS_SELECTOR, "#normal_login_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    SIGNUP_LINK = (By.CSS_SELECTOR, "button > span")

    """Конструктор класса страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    """Действия на странице входа"""

    """это используется для получения заголовка страницы"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """это используется для входа в аккаунт"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)


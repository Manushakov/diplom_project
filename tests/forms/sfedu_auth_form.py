from forms.base_form import CheckForm
from elements.text_field_element import TextField
from elements.button import Button
from selenium.webdriver.common.by import By
from utils.checklogger import CheckLogger


class SfeduAuthForm(CheckForm):
    SFEDU_AUTH_PAGE_LOCATOR = (By.XPATH, "//div[@class='main']")
    LOGIN_LOCATOR_TEXT_FIELD = (By.XPATH, "//*[@id='loginoauth']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='signoauthin_b']")

    def __init__(self, name="sfeduAuthorisationForm", element=SFEDU_AUTH_PAGE_LOCATOR):
        super().__init__(element, name)

    def send_login(self, login):
        CheckLogger.info("Отправляем логин в поле ввода")
        TextField(self.LOGIN_LOCATOR_TEXT_FIELD, "textFieldLogin").send_keys(login)

    def click_login_button(self):
        CheckLogger.info("Нажимаем на кнопку авторизации")
        Button(self.LOGIN_BUTTON, "loginButton").click()

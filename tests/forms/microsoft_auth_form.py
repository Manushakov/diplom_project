from forms.base_form import CheckForm
from elements.text_field_element import TextField
from elements.button import Button
from selenium.webdriver.common.by import By
from utils.checklogger import CheckLogger


class MicrosoftAuthForm(CheckForm):
    MICROSOFT_AUTH_PAGE_LOCATOR = (By.XPATH, "//div[@class='win-scroll']")
    PASSWORD_LOCATOR_TEXT_FIELD = (By.XPATH, "//*[@name='passwd']")
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//*[@id='idBtn_Back']")

    def __init__(self, name="microsoftAuthorisationForm", element=MICROSOFT_AUTH_PAGE_LOCATOR):
        super().__init__(element, name)

    def send_password(self, password):
        CheckLogger.info("Отправляем пароль в поле ввода")
        TextField(self.PASSWORD_LOCATOR_TEXT_FIELD, "textFieldPassword").send_keys(password)

    def click_login_button(self):
        CheckLogger.info("Нажимаем на кнопку авторизации")
        Button(self.LOGIN_BUTTON, "loginButton").click()

    def click_submit_login_button(self):
        CheckLogger.info("Нажимаем на кнопку подтверждения авторизации")
        Button(self.SUBMIT_LOGIN_BUTTON, "submitLoginButton").click()

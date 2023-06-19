from waits import Waits
from browser.check_browser import CheckBrowser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BaseElement:

    def __init__(self, locator, name, condition=By.XPATH):
        self.locator = locator
        self.name = name
        self.condition = condition

    def isDisplayed(self):
        return self.find_element().is_displayed()

    def getName(self):
        return self.name

    def click(self):
        self._wait_for_exists().click()

    def getAttribute(self, name):
        return self._wait_for_exists().get_attribute(name)

    def find_element(self):
        return CheckBrowser.get_driver().find_element(self.condition, self.locator)

    def find_elements(self):
        return CheckBrowser.get_driver().find_elements(self.condition, self.locator)

    def _wait_for_exists(self):
        return Waits.element_presence_wait(CheckBrowser.get_driver(), self.locator)

    def get_text(self):
        return self._wait_for_exists().text

    def move_cursor(self):
        action = ActionChains(CheckBrowser.get_driver())
        action.move_to_element(self._wait_for_exists()).perform()

    def send_keys(self, value):
        self._wait_for_exists().send_keys(value)

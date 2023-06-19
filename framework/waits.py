from utils.checklogger import CheckLogger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Waits:
    @staticmethod
    def alert_wait(browser):
        try:
            WebDriverWait(browser, 5).until(EC.alert_is_present())
        except TimeoutException:
            CheckLogger.info("no alert")

    @staticmethod
    def element_presence_wait(browser, locator):
        try:
            element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            CheckLogger.info(f"element with locator: {locator} not found on page")

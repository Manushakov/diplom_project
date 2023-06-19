from waits import Waits
from utils.checklogger import CheckLogger
from singleton import Singleton
from browser.check_browser_factory import CheckBrowserFactory
from selenium.common.exceptions import NoAlertPresentException


class CheckBrowser(metaclass=Singleton):
    __driver = None

    def __init__(self, name=None, locale=None):
        self.browser_name = name
        CheckBrowser.__driver = CheckBrowserFactory().get_driver(name, locale)

    @staticmethod
    def get_page(url, login=None, password=None):
        CheckLogger.info(f"opening {url} page")
        if login is None and password is None:
            CheckBrowser.__driver.get(url)

        elif login is not None and password is not None:
            CheckBrowser.__driver.get(url.replace("//", f"//{login}:{password}@"))
        else:
            raise ValueError("Incorrect values for authorisation")

    @staticmethod
    def get_driver():
        return CheckBrowser.__driver

    @staticmethod
    def quit():
        CheckBrowser.__driver.quit()
        CheckBrowser._instances = {}

    @staticmethod
    def get_alert_text(name):
        CheckLogger.info("get alert text and compare", name)
        Waits.alert_wait(CheckBrowser.get_driver())
        return CheckBrowser.__driver.switch_to.alert.text

    @staticmethod
    def accept_alert(name):
        CheckLogger.info("accept alert", name)
        Waits.alert_wait(CheckBrowser.get_driver())
        CheckBrowser.__driver.switch_to.alert.accept()

    @staticmethod
    def send_text_alert(text, name):
        CheckLogger.info("send text to prompt", name)
        Waits.alert_wait(CheckBrowser.get_driver())
        CheckBrowser.__driver.switch_to.alert.send_keys(text)

    @staticmethod
    def is_alert_close(name):
        CheckLogger.info("check closed alert", name)
        try:
            CheckBrowser.__driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True

    @staticmethod
    def get_url():
        return CheckBrowser.__driver.current_url

    @staticmethod
    def back(name):
        CheckLogger.info("open previous page", name)
        CheckBrowser.__driver.back()


    @staticmethod
    def reload():
        CheckLogger.info("open previous page")
        CheckBrowser.__driver.reload()

    @staticmethod
    def switch_to_frame(frame_id, name):
        CheckLogger.info("switch to iFrame", name)
        CheckBrowser.__driver.switch_to.frame(frame_id)

    @staticmethod
    def switch_to_default_content(name):
        CheckLogger.info("switch to default page", name)
        CheckBrowser.__driver.switch_to.default_content()

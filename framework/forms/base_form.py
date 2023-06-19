from waits import Waits
from utils.checklogger import CheckLogger
from browser.check_browser import CheckBrowser


class CheckForm:

    def __init__(self, element, name):
        self.element = element
        self.name = name

    def isDisplayed(self):
        return self.element.isDisplayed()

    def waitForOpen(self):
        CheckLogger().info("Проверка загрузки страницы", self.name)
        return Waits.element_presence_wait(CheckBrowser.get_driver(), self.element)

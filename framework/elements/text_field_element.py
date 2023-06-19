from elements.base_element import BaseElement
from browser.check_browser import CheckBrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TextField(BaseElement):
    def select_half_letters(self, amount):
        action = ActionChains(CheckBrowser.get_driver())
        action.move_to_element_with_offset(self._wait_for_exists(), 0, 0).click().perform()
        action.key_down(Keys.SHIFT).perform()
        action.send_keys(Keys.ARROW_RIGHT * (amount//2)).perform()

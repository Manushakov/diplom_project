from .base_element import BaseElement
from selenium.webdriver.common.keys import Keys


class Slider(BaseElement):
    def move_slider_indicator(self, amount):
        self._wait_for_exists().send_keys(Keys.ARROW_RIGHT*amount)

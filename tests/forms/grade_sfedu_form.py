from forms.base_form import CheckForm
from elements.label import Label
from elements.button import Button
from selenium.webdriver.common.by import By


class GradeSfeduForm(CheckForm):
    GRADE_SFEDU_PAGE_LOCATOR = (By.XPATH, "//div[@class='win-scroll']")
    DISCIPLINE_LABEL_FIELD = "//tr[@class='disciplineRow']"
    DISCIPLINE_BUTTON_LOCATOR = "//a[contains(text(), 'Дисциплины')]"
    HISTORY_BUTTON_LOCATOR = "//a[contains(text(), 'История событий')]"

    def __init__(self, name="gradeSfeduForm", element=GRADE_SFEDU_PAGE_LOCATOR):
        super().__init__(element, name)

    def get_disciplines_amount(self):
        return len(Label(self.DISCIPLINE_LABEL_FIELD, "disciplineLabelField").find_elements())

    def is_disciplines_button_present(self):
        return Button(self.DISCIPLINE_BUTTON_LOCATOR, "disciplineButton").isDisplayed()

    def is_history_button_present(self):
        return Button(self.HISTORY_BUTTON_LOCATOR, "historyButton").isDisplayed()

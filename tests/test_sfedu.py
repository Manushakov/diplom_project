import allure
from browser.check_browser import CheckBrowser
from tests.forms.sfedu_auth_form import SfeduAuthForm
from tests.forms.microsoft_auth_form import MicrosoftAuthForm
from tests.forms.grade_sfedu_form import GradeSfeduForm
from tests.config.urls import Urls
from utils.checklogger import CheckLogger


class TestGradeSfedu:
    @allure.title("Тест БРС")
    @allure.description("Проверка наличия элементов управления на главной странице БРС")
    @allure.link(Urls.BASE_URL, name="Site Url")
    def test_auth_page(self, create_browser):
        with allure.step("Авторизация БРС"):
            CheckLogger.info("Авторизация в системе БРС")
            CheckBrowser.get_page(Urls.BASE_URL)  # получение браузером исходной страницы
            sfedu_auth_page = SfeduAuthForm()  # инициализация страницы авторизации ЮФУ
            sfedu_auth_page.waitForOpen()  # ожидание открытия страницы
            sfedu_auth_page.send_login(create_browser[0])  # ввод Логина пользователя
            sfedu_auth_page.click_login_button()  # нажатие на кнопку авторизации
        with allure.step("Авторизация Microsoft"):
            microsoft_auth_page = MicrosoftAuthForm()  # инициализация страницы авторизации Microsoft
            microsoft_auth_page.waitForOpen()  # ожидание открытия страницы
            microsoft_auth_page.send_password(create_browser[1])  # ввод Пароля пользователя
            microsoft_auth_page.click_login_button()  # нажатие на кнопку авторизации
            microsoft_auth_page.click_submit_login_button()  # нажимаем на кнопку подтверждения
        with allure.step("Проверка функционала  БРС"):
            grade_sfedu_form = GradeSfeduForm() # инициализация страницы БРС
            CheckLogger.info("Проверка на наличие дисциплин на странице БРС")
            assert grade_sfedu_form.get_disciplines_amount() > 0, "Дисциплины не отображаются"
            CheckLogger.info("Проверка наличия кнопки 'Дисциплины' на странице БРС")
            assert grade_sfedu_form.is_disciplines_button_present(), "кнопка 'Дисциплины' не отображается"
            CheckLogger.info("Проверка наличия кнопки 'История событий' на странице БРС")
            assert grade_sfedu_form.is_history_button_present(), "кнопка 'История событий' не отображается"

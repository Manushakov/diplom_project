class BrowserConfig(object):
    # Настройки браузера
    # Поддерживаемые браузеры: "chrome", "firefox"
    BROWSER = "chrome"
    LOCALE = "ru"
    CHROME_VERSION = "75.0"
    FIREFOX_VERSION = "66.0"

    # Блок ожиданий
    # Настройка ожиданий браузера
    IMPLICITLY_WAIT_SEC = 0
    EXPLICITLY_WAIT_SEC = 10
    PAGE_LOAD_TIMEOUT_SEC = 10

from selenium.webdriver.common.by import By


class CommonLocators:

    HEADER_YANDEX_BUTTON = By.XPATH, '//div/a[contains(@class, "Header_LogoYandex")]'
    HEADER_SCOOTER_BUTTON = By.XPATH, '//div/a[contains(@class, "Header_LogoScooter")]'
    HEADER_ORDER_BUTTON = By.XPATH, '//div[2]/button[1][ text()="Заказать" ]'

    COOKIE_BUTTON = By.XPATH, '//button[contains(@class, "CookieButton")]'

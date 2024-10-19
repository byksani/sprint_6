from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Найти элемент с ожиданием: {locator}")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
            locator))
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_using_js(self, locator):
        element = self.find_element_with_wait(locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Добавить текст '{text}' в элемент: {locator}")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получить текст из элемента: {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Прокрутить до элемента: {locator}")
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Форматировать локаторы: {locator_1} с числом {num}")
    def format_locators(self, locator_1, num):
        method, locator = locator_1 # '//*[@class="my-question-locator-{}"]'
        locator = locator.format(num) # '//*[@class="my-question-locator-1"]'
        # f'{num}'
        return method, locator

    @allure.step("Проверить текущую страницу: {expected_url}")
    def verify_current_page(self, expected_url):
        current_url = self.get_current_url()
        return current_url == expected_url, f"Ожидался URL {expected_url}, но был {current_url}"

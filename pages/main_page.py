from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.common_locators import CommonLocators
from data import Urls
import allure


class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    @allure.step("Скрыть плашку про куки")
    def hide_the_cookie_bar(self):
        self.click_to_element(CommonLocators.COOKIE_BUTTON)

    @allure.step("Прокрутка в самый низ страницы")
    def scroll_down_the_page(self):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)

    @allure.step("Клик по вопросу: {locator_q_formatted}")
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.click_to_element(locator_q_formatted)

    @allure.step("Получение текста ответа для локатора: {locator_a_formatted}")
    def get_answer_text_1(self, locator_a_formatted):
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Получение текста ответа для вопроса номер {num}")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_down_the_page()
        self.hide_the_cookie_bar()
        self.click_to_element(locator_q_formatted)
        return self.get_answer_text_1(locator_a_formatted)

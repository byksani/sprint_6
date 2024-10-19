from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.common_locators import CommonLocators
import allure
import data


class OrderPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(data.MAIN_PAGE_URL)

    @allure.step("Открыть страницу заказа")
    def open_order_page(self):
        self.open_page(data.ORDER_PAGE_URL)

    @allure.step("Скрыть плашку про куки")
    def hide_the_cookie_bar(self):
        self.click_to_element(CommonLocators.COOKIE_BUTTON)

    @allure.step("Клик по кнопке заказа")
    def click_to_the_order_button(self, button):
        self.scroll_to_element(button)
        self.click_to_element(button)

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, random_user_data):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, random_user_data['first_name'])
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, random_user_data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, random_user_data['address'])
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, random_user_data['phone'])
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_to_element(OrderPageLocators.FIRST_METRO_STATION)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.TWO_DAYS)
        self.add_text_to_element(OrderPageLocators.DATEPICKER, random_user_data['tomorrow'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.OK_BUTTON)
        self.find_element_with_wait(OrderPageLocators.ORDER_STATUS)
        return self.get_text_from_element(OrderPageLocators.ORDER_STATUS)

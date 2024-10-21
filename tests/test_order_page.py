from data import Urls
import pytest
import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.common_locators import CommonLocators


class TestMainPage:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Переходим на страницу заказа, заполняем форму, подтверждаем заказ и проверяем, что статус успешный')
    @pytest.mark.parametrize('order_button', [
        CommonLocators.HEADER_ORDER_BUTTON,
        OrderPageLocators.DOWN_ORDER_BUTTON
    ])
    def test_success_order_creation(self, driver, random_user_data, order_button):
        order_page = OrderPage(driver)
        order_page.open_main_page()
        order_page.click_to_the_order_button(order_button)
        order_page.hide_the_cookie_bar()

        order_page.fill_first_page(random_user_data)
        order_page.fill_second_page(random_user_data)

        order_status = order_page.get_order_status()
        assert 'Заказ оформлен' in order_status, f"Ожидалось сообщение 'Заказ оформлен', но получено '{order_status}'"

    @allure.title('Проверка переходов по клику на кнопки в хедере')
    @allure.description('Открыть страницу заказа, кликнуть на кнопку {header_button} в хедере и проверить конечный URL')
    @pytest.mark.parametrize('header_button,expected_url', [
        [CommonLocators.HEADER_SCOOTER_BUTTON, Urls.MAIN_PAGE_URL],
        [CommonLocators.HEADER_YANDEX_BUTTON, Urls.DZEN_PAGE]
    ])
    def test_return_to_the_main_page(self, driver, header_button, expected_url):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_to_element(header_button)
        assert order_page.verify_current_page(expected_url)

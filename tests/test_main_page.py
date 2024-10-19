import pytest
import allure
from data import ANSWER_NUM_AND_TEXTS
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка ответов на вопросы')
    @allure.description('Скроллим до секции с вопросами, открываем вопрос и проверяем ответ на него')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_NUM_AND_TEXTS.get(0)),
            (1, ANSWER_NUM_AND_TEXTS.get(1)),
            (2, ANSWER_NUM_AND_TEXTS.get(2)),
            (3, ANSWER_NUM_AND_TEXTS.get(3)),
            (4, ANSWER_NUM_AND_TEXTS.get(4)),
            (5, ANSWER_NUM_AND_TEXTS.get(5)),
            (6, ANSWER_NUM_AND_TEXTS.get(6)),
            (7, ANSWER_NUM_AND_TEXTS.get(7))
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.get_answer_text(num) == result


import pytest
import allure
from data import AnswerTexts
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка ответов на вопросы')
    @allure.description('Скроллим до секции с вопросами, открываем вопрос и проверяем ответ на него')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(0)),
            (1, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(1)),
            (2, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(2)),
            (3, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(3)),
            (4, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(4)),
            (5, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(5)),
            (6, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(6)),
            (7, AnswerTexts.ANSWER_NUM_AND_TEXTS.get(7))
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.get_answer_text(num) == result


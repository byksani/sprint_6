from selenium.webdriver.common.by import By


class OrderPageLocators:

    DOWN_ORDER_BUTTON = By.XPATH, '//div[5]/button[ text()="Заказать" ]'

    NAME_FIELD = By.XPATH, '//input[ @placeholder="* Имя" ]'
    SURNAME_INPUT = By.XPATH, '//input[ @placeholder = "* Фамилия" ]'
    ADDRESS_INPUT = By.XPATH, '//input[ @placeholder = "* Адрес: куда привезти заказ" ]'
    METRO_STATION_INPUT = By.XPATH, '//input[ @placeholder = "* Станция метро" ]'
    FIRST_METRO_STATION = By.XPATH, "//button[ @value='1' ]"
    PHONE_INPUT = By.XPATH, '//input[ @placeholder = "* Телефон: на него позвонит курьер" ]'
    NEXT_BUTTON = By.XPATH, '//button[ text()="Далее" ]'

    DATEPICKER = By.XPATH, '//input[ @placeholder = "* Когда привезти самокат" ]'
    RENTAL_PERIOD = By.XPATH, '//div[ text()="* Срок аренды" ]'
    TWO_DAYS = By.XPATH, '//div[ text()="двое суток" ]'
    ORDER_BUTTON = By.XPATH, '//div[3]/button[2][ text()="Заказать" ]'
    OK_BUTTON = By.XPATH, '//button[2][ text()="Да" ]'

    ORDER_STATUS = By.XPATH, '//div[contains(@class, "Order_ModalHeader")]'
    VIEW_STATUS_BUTTON = By.XPATH, '//button[2][ text()="Посмотреть статус" ]'

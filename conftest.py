import pytest
import random
from selenium import webdriver
from datetime import datetime, timedelta

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def random_user_data():
    names = ['Валерия', 'Марта', 'Ася', 'Шарлотта']
    streets = ['Мира', 'Каширская', 'Рубинштейна']
    today = datetime.now()
    tomorrow = (today + timedelta(days=1)).strftime("%d.%m.%Y")
    random_name = random.choice(names)
    random_surname = random.choice(names) + 'нова'
    random_address = f"ул. {random.choice(streets)}, д. {random.randint(1, 100)}"
    random_phone = f"+7{random.randint(9000000000, 9999999999)}"

    return {
        'first_name': random_name,
        'last_name': random_surname,
        'address': random_address,
        'phone': random_phone,
        'tomorrow': tomorrow
    }

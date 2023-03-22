import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_present(my_pets):
   """Проверка наличия всех питомцев на странице со списком питомцев пользователя"""

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # Вывод элементов карточек питомцев в переменную pets

    statistics = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    # Вывод элементов карточек питомцев в переменную statistics

    number_of_pets = len(pets)
    # Вывод количества карточек питомцев пользователя

    number = statistics[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # Вывод количества карточек питомцев пользователя из данных статистики

    assert number == number_of_pets
    # Проверка совпадения количества питомцев из статистики с количеством карточек питомцев


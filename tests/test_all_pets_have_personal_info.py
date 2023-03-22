import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_pets_have_name_age_gender(my_pets):
   """Поверка наличия у всех питомцев информации (имя, возраст, порода) на странице со списком моих питомцев"""
    wait = WebDriverWait(pytest.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # Сохранение элементов с данными о питомца в переменную pet_data

    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3
"""В pet_data из полученных данных оставили имя, возраст и породу, вместо остальных данных пустая строку и отделяем через пробел.
В полученном результате находим количество элементов и сравниваем с ожидаемым результатом"""


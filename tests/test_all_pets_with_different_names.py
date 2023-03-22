import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_with_different_names(my_pets):
    """Поверка отсутствия у питомцев в списке пользователя одинаковых имен"""
    """Для получения положительного результата на странице пользователя должны быть загружены питомцы с разными 
   идентифицирующими данными, в данном случае разными именами"""
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # Сохранение элементов карточек питомцев в переменную pets

    # Из pet_data выбираются имена и добавляются в список pet_name
    pet_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pet_name.append(split_data_pet[0])

    # Проверка полученных имен. При каждом совпадении счетчик увеличивается на единицу
    # Если совпадений нет, то similar(счетчик) будет равен нулю.
    similar = 0
    for i in range(len(pet_name)):
        if pet_name.count(pet_name[i]) > 1:
            similar += 1
    assert similar == 0

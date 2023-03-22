import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(my_pets):
    '''Проверка отсутствия в списке пользователя повторяющихся питомцев'''

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # Сохранение элементы с данными о питомцав в переменную pet_data

    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)
    # Из данных в pet_data остается имя, возраст, порода. Остальное заменяется на пустую строку
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '
    # Объединиение полученных данных имени, возраста, породы
    # Полученный результат добавляется в строку с пробелом

    list_line = line.split(' ')
    set_list_line = set(list_line)
    a = len(list_line)
    b = len(set_list_line)
    # Из строки line выводится список, переводится в множество и находится количество элементов в списке и в множестве
    result = a - b
    assert result == 0
    # Поиск различий в количестве элементов списка с количеством элементов множества
    # Если разница между элементами 0, то повторяющихся питомцев у пользователя нет

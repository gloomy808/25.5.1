import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_show_my_pets():
   """Проверка перехода на страницу Мои питомцы"""
    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    #  Ввод email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    # Нажатие на кнопку входа
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    # Нажатие на кнопку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    # Проверка, что произошел переход на страницу "Мои питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'


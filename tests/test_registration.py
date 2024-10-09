import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    #Тестируем успешную регистрацию
    def test_registration_with_valid_data_registration_confirmed(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Находим поле "Имя" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys('Test User29494895811343433')

        # Находим поле "Email" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys('test15699@ya.ru')

        # Находим поле "Пароль" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(3) > div > div > input').send_keys('gerternord29')

        # Находим кнопку "Регистрация" и кликаем
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        driver.implicitly_wait(5)

        # Проверяем, что сообщения об ошибке регистрации на странице нет
        error_message = driver.find_elements(By.CLASS_NAME, 'input__error text_type_main-default')

        assert len(error_message) == 0

        driver.quit()

    # Тестируем вывод шибки для некорректного пароля
    def test_registration_with_not_valid_password_registration_not_confirmed(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Находим поле "Имя" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys('Test User23434234')

        # Находим поле "Email" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys('test2785561@ya.ru')

        # Находим поле "Пароль" и заполняем его
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(3) > div > div > input').send_keys('gerte')

        # Находим кнопку "Регистрация" и кликаем
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        # Проверяем, что сообщение о некорректном пароле отображается (с ожиданием)
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')))

        driver.quit()

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestJumpFromPersonalAccount:
    #Тестируем переход в кноструктор по кнопке из личного кабинета
    def test_jump_to_constructor_by_clicking_constructor_button_jump_completed(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        # Находим кнопку "Войти в аккаунт" на главной странице и кликаем
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button').click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys(
            '45697833@ya.ru')

        # Находим поле "Пароль" и заполняем его данными
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys(
            'hertond4545')

        # Находим кнопку "Войти" и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        # Находим и кликаем на кнопку "Личный кабинет"
        driver.find_element(By.XPATH, '//*/div/header/nav/a/p').click()

        # Находим кнопку "Конструктор" и кликаем
        driver.find_element(By.XPATH, '//*/div/header/nav/ul/li/a/p[text()="Конструктор"]').click()

        # Проверяем, что переход выполнен, через поиск кнопки "Оформить заказ"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*/div/main/section/div/button[text()="Оформить заказ"]')))

        driver.quit()

    # Тестируем переход в кноструктор по клику на лого
    def test_jump_to_constructor_by_clicking_logo_jump_completed(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        # Находим кнопку "Войти в аккаунт" на главной странице и кликаем
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button').click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys(
            '45697833@ya.ru')

        # Находим поле "Пароль" и заполняем его данными
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys(
            'hertond4545')

        # Находим кнопку "Войти" и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        # Находим и кликаем на кнопку "Личный кабинет"
        driver.find_element(By.XPATH, '//*/div/header/nav/a/p').click()

        # Находим и кликаем на лого
        driver.find_element(By.XPATH, '//*/div/header/nav/div/a').click()

        # Проверяем, что переход выполнен, через поиск кнопки "Оформить заказ"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*/div/main/section/div/button[text()="Оформить заказ"]')))

        driver.quit()

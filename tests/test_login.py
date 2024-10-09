from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    #Тестируем вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_login_confirmed(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site")

        # Находим кнопку "Войти в аккаунт" на главной странице и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button').click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys('45697833@ya.ru')

        # Находим поле "Пароль" и заполняем его данными
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys('hertond4545')

        # Находим кнопку "Войти" и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        # Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ", которая заменяет кнопку "Войти в аккаунт"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button')))

        driver.quit()

    # вход через кнопку «Личный кабинет»
    def test_login_through_personal_account_button_login_confirmed(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site")

        # Находим кнопку "Личный Кабинет" в шапке и кликаем
        driver.find_element(By.XPATH, '//*/div/header/nav/a/p').click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys('45697833@ya.ru')

        # Находим поле "Пароль" и заполняем его данными
        driver.find_element(By.CSS_SELECTOR,  '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys('hertond4545')

        # Находим кнопку "Войти" и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        # Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ", которая заменяет кнопку "Войти в аккаунт"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button')))

        driver.quit()

    #Тестируем вход через кнопку в форме регистрации
    def test_login_through_button_in_the_registration_form_login_confirmed(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/register")

        #Находим кнопку "Войти" на странице регистрации и кликаем
        driver.find_element(By.XPATH, '//*/div/main/div/div/p/a[text()="Войти"]').click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys('45697833@ya.ru')

        # Находим поле "Пароль" и заполняем его данными
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys('hertond4545')

        # Находим кнопку "Войти" и кликаем
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        # Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ", которая заменяет кнопку "Войти в аккаунт"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button')))

        driver.quit()

    #Тестируем вход через кнопку в форме восстановления пароля
    def test_login_through_button_in_the_password_recovery_form(self):
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # Находим кнопку "Войти" на странице регистрации и кликаем
        driver.find_element(By.XPATH, '//*/div/main/div/div/p/a[text()="Войти"]').click()

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

        # Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ", которая заменяет кнопку "Войти в аккаунт"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button')))

        driver.quit()

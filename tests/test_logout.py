from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    #Тестируем выход из личного кабинет
    def test_logout_through_personal_account_logout_completed(self):
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

        # Переходим в личный кабинет
        driver.find_element(By.XPATH, '//*/div/header/nav/a/p').click()

        # Ждем, пока прогрузится страница ЛК и жмем кнопку выхода
        driver.implicitly_wait(3)
        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > nav > ul > li:nth-child(3) > button').click()

        # Проверяем результат через поиск "Вход"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*/div/main/div/h2[text()="Вход"]')))

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestJumpToPersonalAccount:
    #Тестируем вход в личный кабинет с предварительной авторизацией
    def test_jump_to_personal_account_fron_main_page_jump_is_completed(self):
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

        # Проверяем, что переход в ЛК выполнен через поиск на странице кнопки "История заказов"
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*/div/main/div/nav/ul/li/a[text()="История заказов"]')))

        driver.quit()

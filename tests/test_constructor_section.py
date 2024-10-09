from selenium.webdriver.common.by import By
from selenium import webdriver


class TestConstructorSection:
    #Тестируем скрол к секции булок (сначала скролим до начинки, потом возвращаемся)
    def test_constructor_jump_to_buns_section(self):
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

        # Прокручиваем до начинки
        element1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')
        driver.execute_script("arguments[0].scrollIntoView();", element1)

        # Возвращаемся к булкам
        element2 = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')
        driver.execute_script("arguments[0].scrollIntoView();", element2)

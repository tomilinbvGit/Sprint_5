from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import Locators
from conftest import driver
from data import URLS, DATA


class TestJumpFromPersonalAccount:
    # Тестируем переход в кноструктор по кнопке из личного кабинета
    def test_jump_to_constructor_by_clicking_constructor_link_jump_completed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Находим кнопку "Войти в аккаунт" на главной странице и кликаем
        driver.find_element(*Locators.GO_TO_LOGIN_PAGE).click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(DATA.pre_registered_email)

        # Находим поле "Пароль" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.pre_registered_password)

        # Находим кнопку "Войти" и кликаем
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        """Находим и кликаем на кнопку "Личный кабинет" 
        (с ожиданием, т.к. при прогоне автотестов возникает ошибка "element click intercepted")"""
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Находим ссылку "Конструктор" и кликаем
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        # Проверяем, что переход выполнен, через поиск кнопки "Оформить заказ"
        order_button_on_main_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

    # Тестируем переход в кноструктор по клику на лого
    def test_jump_to_constructor_by_clicking_logo_jump_completed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Находим кнопку "Войти в аккаунт" на главной странице и кликаем
        driver.find_element(*Locators.GO_TO_LOGIN_PAGE).click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(DATA.pre_registered_email)

        # Находим поле "Пароль" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.pre_registered_password)

        # Находим кнопку "Войти" и кликаем
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        """Находим и кликаем на кнопку "Личный кабинет" 
        (с ожиданием, т.к. при прогоне автотестов возникает ошибка "element click intercepted")"""
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Находим и кликаем на ссылку-лого
        driver.find_element(*Locators.LOGO_LINK).click()

        # Проверяем, что переход выполнен, через поиск кнопки "Оформить заказ"
        order_button_on_main_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

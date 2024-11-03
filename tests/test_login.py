from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import Locators
from conftest import driver
from data import URLS, DATA


class TestLogin:
    # Тестируем вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_login_confirmed(self, driver):
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

        """Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ",
        которая заменяет кнопку "Войти в аккаунт"""
        order_button_on_main_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

    # Тестируем вход через кнопку «Личный кабинет»
    def test_login_through_personal_account_link_login_confirmed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Находим кнопку "Личный Кабинет" в шапке и кликаем
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(DATA.pre_registered_email)

        # Находим поле "Пароль" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.pre_registered_password)

        # Находим кнопку "Войти" и кликаем
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        """Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ",
        которая заменяет кнопку "Войти в аккаунт"""
        order_button_on_main_page = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

    # Тестируем вход через кнопку в форме регистрации
    def test_login_through_button_in_the_registration_form_login_confirmed(self, driver):
        # Открываем страницу регистрации
        driver.get(URLS.registration_page)

        # Находим кнопку "Войти" на странице регистрации и кликаем на нее, когда будет возможность
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.LOGINING_BUTTON)).click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(DATA.pre_registered_email)

        # Находим поле "Пароль" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.pre_registered_password)

        # Находим кнопку "Войти" и кликаем
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        """Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ",
        которая заменяет кнопку "Войти в аккаунт"""
        order_button_on_main_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

    # Тестируем вход через кнопку в форме восстановления пароля
    def test_login_through_button_in_the_password_recovery_form(self, driver):
        # Открываем страницу формы восстановления
        driver.get(URLS.recovery_form_page)

        # Нажимаем кнопку на "Войти"
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        # Находим поле "Email" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(DATA.pre_registered_email)

        # Находим поле "Пароль" и заполняем его данными заранее зарегистрированного пользователя
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.pre_registered_password)

        # Находим кнопку "Войти" и кликаем
        driver.find_element(*Locators.LOGINING_BUTTON).click()

        """Проверяем, что вход выполнен, через переадресовку на главную страницу и поиска кнопки "Оформить заказ",
        которая заменяет кнопку "Войти в аккаунт"""
        order_button_on_main_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        assert order_button_on_main_page is not None

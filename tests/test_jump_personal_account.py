from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import Locators
from conftest import driver
from data import URLS, DATA


class TestJumpToPersonalAccount:
    # Тестируем вход в личный кабинет пользователя (с предварительной авторизацией)
    def test_jump_to_personal_account_fron_main_page_jump_is_completed(self, driver):
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

        # Находим и кликаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Проверяем, что переход в ЛК выполнен через поиск на странице ссылки "История заказов"
        history_link_on_page = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.ORDER_HISTORY))

        assert history_link_on_page is not None

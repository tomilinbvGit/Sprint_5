from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import Locators
from conftest import driver
from data import URLS, DATA


class TestLogout:
    # Тестируем выход из личного кабинет
    def test_logout_through_personal_account_logout_completed(self, driver):
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

        # Переходим в личный кабинет (с ожиданием кликабельности ссылки ЛК)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Ждем, пока прогрузится страница ЛК и жмем кнопку выхода
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        # Проверяем результат через поиск кнопки "Войти" на странице авторизации
        assert WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(Locators.LOGINING_BUTTON)
        )

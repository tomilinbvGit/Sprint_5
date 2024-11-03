from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from TestLocators import Locators
from helpers import email_generator, password_generator
from data import URLS, DATA


class TestRegistration:
    # Тестируем успешную регистрацию

    def test_registration_with_valid_data_registration_confirmed(self, driver):
        # Создаем переменную с уникальной почтой для теста
        unique_email = email_generator()

        # Создаем переменную с уникальным паролем для теста
        unique_password = password_generator()

        # Открываем страницу регистрации
        driver.get(URLS.registration_page)

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.NAME_INPUT).send_keys('TomilinBV1')

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(unique_email)

        # Находим поле "Пароль" и заполняем его
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(unique_password)

        # Находим кнопку "Регистрация" и кликаем
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        """Проверяем, что регистрация пройдена через поиск текста "Вы — новый пользователь?"
        который будет появляться при успешно регистраци и переводе на страницу входа ('.../login')"""
        question_on_login_page = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.QUESTION_ABOUT_REGISTRATION))

        assert question_on_login_page is not None

    # Тестируем вывод шибки для некорректного пароля
    def test_registration_with_not_valid_password_registration_not_confirmed(self, driver):

        # Создаем переменную с уникальной почтой для теста
        unique_email = email_generator()

        # Открываем страницу регистрации
        driver.get(URLS.registration_page)

        # Находим поле "Имя" и заполняем его
        driver.find_element(*Locators.NAME_INPUT).send_keys('TomilinBV2')

        # Находим поле "Email" и заполняем его
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(unique_email)

        # Находим поле "Пароль" и заполняем его невалидным паролем
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(DATA.not_valid_password)

        # Находим кнопку "Регистрация" и кликаем
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Поиск сообщения о невалидном пароле ищем через ожиданием
        error_message_is_presence = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(Locators.NOT_VALID_PASSWORD_ERROR_MESSAGE))

        assert error_message_is_presence is not None

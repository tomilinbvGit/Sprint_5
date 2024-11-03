from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestLocators import Locators
from conftest import driver
from data import URLS


class TestConstructorSection:
    """Тест перехода в раздел 'Булки'. Чтобы проверить переход по кнопке раздела 'Булки',
    сначала необходимо выполнить переход в другой раздел конструктора, т.к. раздел 'Булки' открыт по умолчанию
    и кнопка перехода в его раздел изначально неактивна"""
    def test_constructor_jump_to_buns_section_jump_is_completed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Проверяем, что кнопка переходжа в раздел 'Соусы' кликабельна и кликаем на нее
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()

        # Проверяем, что кнопка переходжа в раздел кликабельна и кликаем на нее
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.BUNS_BUTTON)).click()

        # Проверяем через видимость загаловка раздела "Булки" на странице
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.HEADING_OF_THE_BUNS_SECTION)
        )

    # Тест перехода в раздел 'Соусы'
    def test_constructor_jump_to_sauces_section_jump_is_completed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Проверяем, что кнопка переходжа в раздел кликабельна и кликаем на нее
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.SAUCES_BUTTON)).click()

        # Проверяем через видимость загаловка раздела "Соусы" на странице
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.HEADING_OF_THE_SAUCES_SECTION)
        )

    # Тест перехода в раздел 'Начинки'
    def test_constructor_jump_to_fillings_section_jump_is_completed(self, driver):
        # Открываем главную страницу
        driver.get(URLS.main_page)

        # Проверяем, что кнопка переходжа в раздел кликабельна и кликаем на нее
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.FILLINGS_BUTTON)).click()

        # Проверяем через видимость загаловка раздела "Соусы" на странице
        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.HEADING_OF_THE_FILLINGS_SECTION)
        )

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    # Фикстура для загрузки драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

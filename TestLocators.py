from selenium.webdriver.common.by import By


class Locators:
    # Локатор поля "Имя"
    NAME_INPUT = [By.XPATH, ".//label[text()='Имя']/following-sibling::input"]
    # Локатор поля "Email"
    EMAIL_INPUT = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]
    # Локатор поля "Пароль"
    PASSWORD_INPUT = [By.XPATH, ".//label[text()='Пароль']/following-sibling::input"]
    # Локатор кнопки "Зарегистрироваться"
    REGISTRATION_BUTTON = [By.XPATH, ".//button[text()='Зарегистрироваться']"]
    # Локатор абзаца "Вы — новый пользователь?", который появляется после регистрации и переводе на страницу входа
    QUESTION_ABOUT_REGISTRATION = [By.XPATH, " //p[starts-with(text(), 'Вы')]"]
    # Локатор сообщения при попытке регистрации с невалидным паролем
    NOT_VALID_PASSWORD_ERROR_MESSAGE = [By.XPATH, "//p[text()='Некорректный пароль']"]
    # Локатор кнопки "Войти в аккаунт" на главной странице
    GO_TO_LOGIN_PAGE = [By.XPATH, ".//button[text()='Войти в аккаунт']"]
    # Локатор кнопки "Войти" страницы Входа
    LOGINING_BUTTON = [By.XPATH, ".//*[text()='Войти']"]
    # Локатор кнопки "Оформить заказ" на главной странице (повяляется после входа)
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]
    # Локатор для ссылки на страницу личного кабинета пользователя
    PERSONAL_ACCOUNT_LINK = [By.XPATH, ".//a[contains(@href, '/account')]"]
    # Локатор для ссылки истории заказов в личном кабинете пользователя
    ORDER_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
    # Локатор для ссылки на страницу конструктора
    CONSTRUCTOR_LINK = [By.XPATH, ".//a[@href='/']/p[text()='Конструктор']"]
    # Локатор для лого-ссылки
    LOGO_LINK = [By.XPATH, ".//a[@href='/']/*[local-name()='svg' and @fill='none']"]
    # Локатор для кнопки выхода из личного кабинета пользователя
    LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]
    # Локатор кнопки перехода на раздел "Булки"
    BUNS_BUTTON = [By.XPATH, ".//span[text()='Булки']/parent::div"]
    # Локатор для заголовка раздела "Булки"
    HEADING_OF_THE_BUNS_SECTION = [By.XPATH, ".//h2[text()='Булки']"]
    # Локатор кнопки перехода на раздел "Соусы"
    SAUCES_BUTTON = [By.XPATH, ".//span[text()='Соусы']/parent::div"]
    # Локатор для заголовка раздела "Соусы"
    HEADING_OF_THE_SAUCES_SECTION = [By.XPATH, ".//h2[text()='Соусы']"]
    # Локатор кнопки перехода на раздел "Начинки"
    FILLINGS_BUTTON = [By.XPATH, ".//span[text()='Начинки']/parent::div"]
    # Локатор для заголовка раздела "Начинки"
    HEADING_OF_THE_FILLINGS_SECTION = [By.XPATH, ".//h2[text()='Начинки']"]

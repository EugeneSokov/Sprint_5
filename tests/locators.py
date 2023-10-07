from selenium.webdriver.common.by import By

class Locators:
    PERS_AREA = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # Кнопка "Личный кабинет" на главной странице
    REG_NAME = (By.XPATH,"//label[contains(text(),'Имя')]") # Подпись к полю для ввода имени при регистрации
    REG_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # Активная ссылка "Зарегистрироваться"
    REG_EMAIL = (By.XPATH,"//label[contains(text(),'Email')]") # Подпись к полю для ввода email на странице регистрации
    ACTIVE_REG_POLE = (By.XPATH,"//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_active']/input") # Активное поле на странице регистрации
    EMAIL_AUTOR = (By.XPATH, "//input[@type = 'text']") # Поле ввода email на странице авторизации
    REG_PASS = (By.XPATH,"//input[@type = 'password']") # Поле ввода пароля на странице регистрации
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # Кнопка "Зарегистрироваться"
    PASS_AUTOR = (By.XPATH, "//input[@type = 'password']") # Поле ввода пароля на странице авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка "Войти" на странице авторизации
    REG_CARD_NAME = (By.XPATH, "//h2[contains(text(),'Регистрация')]") # Наименование карточки регистрации
    LOG_CARD_NAME = (By.XPATH, "//h2[contains(text(),'Вход')]") # Наименование карточки входа
    UNCORRECT_PASS = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # Подсказка ввода некорректного пароля
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка "Оформить заказ"
    PROFILE_TEXT = (By.XPATH, "//a[contains(text(),'Профиль')]") # Текст "Профиль" на странице Личного кабинета
    LINK_LOGIN = (By.XPATH, "//a[contains(text(), 'Войти')]") # Активная ссылка "Войти" на странице регистрации
    LINK_RECOVER_PASS = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Активная ссылка для восстановления пароля
    BUTTON_RECOV = (By.XPATH, "//button[contains(text(),'Восстановить')]") # Кнопка восстановления пароля
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка выхода из аккаунта
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка "Конструктор"
    BUTTON_LOGO = (By.XPATH, "//header/nav[1]/div[1]")# Кнопка логотипа Stellar Burgers
    ELEM_SAUCE = (By.XPATH,"//span[contains(text(),'Соусы')]") # Раздел "Соусы"
    ELEM_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]") # Раздел "Булки"
    ELEM_TOPPINGS = (By.XPATH,"//span[contains(text(),'Начинки')]") # Раздел "Начинки"
    ACTIVE_ELEM = (By.XPATH,"//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']") # Активный раздел

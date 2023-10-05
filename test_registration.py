from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators

faker = Faker()
class TestBurgersRegistration:
    def test_registration_registered(self, driver):
        email = faker.email()
        password = faker.password()
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.REG_CARD_NAME)))
        driver.find_element(*Locators.REG_NAME).send_keys('Ivan')
        driver.find_element(*Locators.EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.PASS_REG).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        text = driver.find_element(*Locators.LOG_CARD_NAME).text
        assert text == 'Вход'

    def test_registration_registration_error(self, driver):
        email = faker.email()
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.REG_CARD_NAME)))
        driver.find_element(*Locators.REG_NAME).send_keys('Ivan')
        driver.find_element(*Locators.EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.PASS_REG).send_keys('@12$&')
        driver.find_element(*Locators.REG_BUTTON).click()
        #WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))
        text = driver.find_element(*Locators.UNCORRECT_PASS).text
        assert text == 'Некорректный пароль'

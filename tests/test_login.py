from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.tests.locators import Locators


class TestBurgersLogin:
    def test_login_from_login_to_account(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys('cynthia18@example.org')
        driver.find_element(*Locators.PASS_AUTOR).send_keys('qwerty123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))

    def test_login_from_personal_area(self, driver):
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys('cynthia18@example.org')
        driver.find_element(*Locators.PASS_AUTOR).send_keys('qwerty123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))

    def test_login_from_registration_page(self, driver):
            driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
            driver.find_element(*Locators.REG_LINK).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((Locators.REG_BUTTON)))
            driver.find_element(*Locators.LINK_LOGIN).click()
            driver.find_element(*Locators.EMAIL_AUTOR).send_keys('cynthia18@example.org')
            driver.find_element(*Locators.PASS_AUTOR).send_keys('qwerty123456')
            driver.find_element(*Locators.BUTTON_LOGIN).click()
            assert WebDriverWait(driver, 3).until(
                expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))

    def test_login_from_password_recovery(self, driver):
            driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
            driver.find_element(*Locators.LINK_RECOVER_PASS).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((Locators.BUTTON_RECOV)))
            driver.find_element(*Locators.LINK_LOGIN).click()
            driver.find_element(*Locators.EMAIL_AUTOR).send_keys('cynthia18@example.org')
            driver.find_element(*Locators.PASS_AUTOR).send_keys('qwerty123456')
            driver.find_element(*Locators.BUTTON_LOGIN).click()
            assert WebDriverWait(driver, 3).until(
                expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))

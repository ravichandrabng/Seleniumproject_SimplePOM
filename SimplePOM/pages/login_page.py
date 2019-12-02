from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        driver.set_page_load_timeout(15)

    __username_tb = (By.ID, "username")
    __password_tb = (By.NAME, "pwd")
    __login_button_tb = (By.ID, "loginButton")

    def set_user_name(self, username):
        self.driver.find_element(*self.__username_tb).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.__password_tb).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.__login_button_tb).click()



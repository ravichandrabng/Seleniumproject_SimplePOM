from selenium import webdriver
from SimplePOM.pages.home_page import HomePage
from SimplePOM.pages.login_page import LoginPage
from time import sleep


#driver = webdriver.Chrome()
driver = webdriver.Firefox(executable_path="E:\geckodriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://demo.actitime.com")


login = LoginPage(driver)
login.set_user_name("admin")
login.set_password("manager")
login.click_login_button()

#doubt on executing
home = HomePage(driver)
sleep(6)
home.click_on_logout_link()
sleep(6)
driver.quit()


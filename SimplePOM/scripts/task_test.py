from selenium import webdriver

from SimplePOM.pages.home_page import HomePage
from SimplePOM.pages.login_page import LoginPage
from SimplePOM.pages.task_page import TaskPage
from time import sleep

# driver = webdriver.Chrome()
driver=webdriver.Firefox(executable_path="E:\geckodriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://demo.actitime.com")

login = LoginPage(driver)
login.set_user_name("admin")
login.set_password("manager")
login.click_login_button()

home = HomePage(driver)
sleep(6)
home.click_on_task_tab()

task = TaskPage(driver)
task.click_on_add_new_button()
sleep(6)
task.click_on_new_task()
sleep(6)
task.close_pop_up()
sleep(6)
home.click_on_logout_link()

driver.quit()

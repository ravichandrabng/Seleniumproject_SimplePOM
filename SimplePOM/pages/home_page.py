from selenium.webdriver.common.by import By


class HomePage:

    __logout_link = (By.ID, "logoutLink")
   # __task_tab = (By.XPATH, "//div[text()='TASKS']")
    __task_tab = (By.XPATH, "// div[@id ='container_tasks']")

    def __init__(self, driver):
        self.driver = driver
        driver.set_page_load_timeout(15)
#doubt

    def click_on_logout_link(self):
        self.driver.find_element(*self.__logout_link).click()

        #Note:*self is  used because find_element takes 2 arguments ,if we give self it gives error
        #on giving *self since it takes  arbitrary value as input

    def click_on_task_tab(self):
        self.driver.find_element(*self.__task_tab).click()

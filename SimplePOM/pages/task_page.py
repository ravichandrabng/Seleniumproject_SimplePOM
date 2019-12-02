from selenium.webdriver.common.by import By


class TaskPage:

    __add_new_button = (By.XPATH, "//div[contains(@class,'title ellipsis')]")
    __new_task_button = (By.XPATH, "//div[contains(@class,'item createNewTasks')]")
    __close_button = (By.XPATH, "//div[@id='closeCreateTasksPopupButton']")

    def __init__(self, driver):
        self.driver = driver
        driver.set_page_load_timeout(15)

    def click_on_add_new_button(self):
        self.driver.find_element(*self.__add_new_button).click()

    def click_on_new_task(self):
        self.driver.find_element(*self.__new_task_button).click()

    def close_pop_up(self):
        self.driver.find_element(*self.__close_button).click()


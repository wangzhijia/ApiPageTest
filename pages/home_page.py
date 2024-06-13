from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_click_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_presence_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_user(self):
        return self.wait_presence_element((By.XPATH, "//a[@href='/Member/index.html']"))


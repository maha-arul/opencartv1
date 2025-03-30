from selenium.webdriver.common.by import By

class HomePage():
    lnk_register_linktext = "Register"
    lnk_login_css = "input[value='Log In']"

    def __init__(self, driver):
        self.driver = driver

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.lnk_login_css).click()

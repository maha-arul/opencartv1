from selenium.webdriver.common.by import By

class MyAccountPage():

    link_logout_css = "a[href='logout.htm']"

    def __init__(self,driver):
        self.driver = driver

    def clicklogout(self):
        self.driver.find_element(By.CSS_SELECTOR,self.link_logout_css).click()

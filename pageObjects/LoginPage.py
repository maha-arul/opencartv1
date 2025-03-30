from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.customLogger import LogGen


class LoginPage():
    txt_username_name ="username"
    txt_password_name="password"
    btn_login_css = "input[value='Log In']"
    txt_login_cnfm_css=".smallText"

    def __init__(self,driver):
        self.driver=driver
        self.logger = LogGen.loggen()


    def setUserName(self,user):
        self.driver.find_element(By.NAME,self.txt_username_name).send_keys(user)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login_css).click()

    def getLogincnfmmsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element= wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,self.txt_login_cnfm_css)))
            return element.is_displayed()
        except Exception as e:
            self.logger.error(f"⚠️ Error while getting confirmation message: {str(e)}")  # Log error
            return None
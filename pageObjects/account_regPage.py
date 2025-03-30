from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen


class account_regPage():
    txt_firstname_css = "input[id='customer.firstName']"
    txt_lastname_css = "input[id='customer.lastName']"
    txt_address_css = "input[id='customer.address.street']"
    txt_city_css = "input[id='customer.address.city']"
    txt_state_css = "input[id='customer.address.state']"
    txt_zipcode_css = "input[id='customer.address.zipCode']"
    txt_phone_css="input[id='customer.phoneNumber']"
    txt_ssn_css="input[id='customer.ssn']"
    txt_username_css="input[id='customer.username']"
    txt_password_css = "input[id='customer.password']"
    txt_confpassword_css = "#repeatedPassword"
    btn_reg_xpath="//input[@value='Register']"
    text_msg_conf_xpath="//p[contains(text(),'Your account was created successfully. You are now')]"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def setFirstName(self, fname):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_firstname_css).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_lastname_css).send_keys(lname)

    def setAddress(self,address):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_address_css).send_keys(address)

    def setCity(self,city):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_city_css).send_keys(city)

    def setState(self,state):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_state_css).send_keys(state)

    def setZipcode(self,zipcode):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_zipcode_css).send_keys(zipcode)

    def setPhonenumber(self,phone):
       self.driver.find_element(By.CSS_SELECTOR,self.txt_phone_css).send_keys(phone)

    def setSSN(self,ssn):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_ssn_css).send_keys(ssn)

    def setUsername(self,user):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_username_css).send_keys(user)

    def setPassword(self,pwd):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_password_css).send_keys(pwd)

    def setConfirmPassword(self,cnfpwd):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_confpassword_css).send_keys(cnfpwd)

    def clickReg(self):
        self.driver.find_element(By.XPATH,self.btn_reg_xpath).click()

    def getconfirmationmsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_msg_conf_xpath)))
            return  element.text
        except Exception  as e:
            self.logger.error(f"⚠️ Error while getting confirmation message: {str(e)}")  # Log error
            return None
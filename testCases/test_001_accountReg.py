import logging
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.account_regPage import account_regPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    def test_account_reg(self,setup):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickRegister()

        self.logger.info("Proving customer details for registration")
        self.regpage=account_regPage(self.driver)
        self.regpage.setFirstName("Arul")
        self.regpage.setLastName("Prakash")
        self.regpage.setAddress("lic colony")
        self.regpage.setCity("yeshwantpur")
        self.regpage.setState("bangalore")
        self.regpage.setZipcode("560023")
        self.regpage.setPhonenumber("9070809798")
        self.regpage.setSSN("123566")
        self.username= randomeString.random_string_generator()
        self.regpage.setUsername(self.username)
        self.regpage.setPassword("Asdf@123")
        self.regpage.setConfirmPassword("Asdf@123")

        self.regpage.clickReg()

        self.confmsg=self.regpage.getconfirmationmsg()
        if self.confmsg and ("Your account was created successfully") in self.confmsg:
            self.logger.info("Account registration is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_reg.png")
            self.logger.error("Account registration is failed.")
            self.driver.close()
            assert False

        self.logger.info("**** test_001_AccountRegistration finished *** ")





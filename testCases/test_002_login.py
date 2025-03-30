import logging
import os

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    user = ReadConfig.getUsername()
    pwd = ReadConfig.getPassword()

    def test_login(self,setup):
        self.logger.setLevel(logging.DEBUG)
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user)
        self.lp.setPassword(self.pwd)
        self.lp.clicklogin()

        if self.lp.getLogincnfmmsg() == True:
            self.logger.info("Account login is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_login.png")
            self.logger.error("Account login is failed.")
            self.driver.close()
            assert False


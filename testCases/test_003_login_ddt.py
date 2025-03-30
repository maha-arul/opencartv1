import logging
import os
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    path = os.path.abspath(os.curdir) + "\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Launching application")

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.logout = MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(3)
            self.targetpage=self.lp.getLogincnfmmsg()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.logout.clicklogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.logout.clicklogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")

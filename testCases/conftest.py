from datetime import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='edge':
        serv_obj = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge browser.........")
    elif browser=='firefox':
        serv_obj = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=serv_obj)
        print("Launching firefox browser.........")
    else:
        serv_obj = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching chrome browser.........")

    driver.delete_all_cookies()  # ✅ Clears all cookies before test execution

    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Maha'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

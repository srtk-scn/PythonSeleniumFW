from selenium import webdriver
import pytest
from .Config import *

@pytest.fixture()
def init(request):
    if Config.BROWSER_NAME.upper()=="CHROME":
        driver=webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    elif Config.BROWSER_NAME.upper()=="FIREFOX":
        driver=webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
    else:
        driver=webdriver.Ie(executable_path=Config.IE_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()



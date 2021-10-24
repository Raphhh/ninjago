from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumDriverFactory:

    def __init__(self, logger):
        self._logger = logger

    def create_selenium_driver(self) -> WebDriver:
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Chrome(desired_capabilities=capabilities)
        self._logger.debug('driver ready')
        return driver

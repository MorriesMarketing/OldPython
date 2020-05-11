from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumDrivers():
    CHROME = webdriver.Chrome(executable_path="C:/PythonCode/Drivers/chromedriver.exe")

    def __init__(self, website_driver):
        self.driver = website_driver

    def navigate_to(self, Domain, page):
        print(f'Navigate To: {Domain}{page}')
        return self.driver.get(f'{Domain}{page}')

    def teardown_method(self):
        self.driver.quit()
    
    @staticmethod
    def move_to_element(driver, element):
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

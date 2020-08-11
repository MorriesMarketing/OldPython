from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# Use [self.driver = Selenium()] to initialize Selenium object.
# All selenium functions are to be housed inside the Selenium object for ease of use.
# Headless functionality will be added at somepoint.
#
#
#
#
#
class Selenium():
    #CHROME = webdriver.Chrome(executable_path="C:/PythonCode/Drivers/chromedriver.exe")
    CHROME = webdriver.Chrome(executable_path="F:\DRIVERS/chromedriver.exe")
    def __init__(self, Driver=CHROME):
        self.driver = Driver

    def navigate_to(self, domain, page):
        print(f'Navigate To: {domain}{page}')
        self.driver.get(f'{domain}{page}')

    def teardown_method(self):
        self.driver.quit()
    
    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def find_xpath(self, path):
        print(f'Looking for element:{path}')
        self.driver.find_element_by_xpath(path)
        print(f'Found element:{path}')

    def click_xpath(self, path):
        print(f'Clicking element:{path}')
        self.driver.find_element_by_xpath(path).click()

    @staticmethod
    def fill_text_box(driver, text, element):
        special_symbols = ['"', '/', '<', '>', ';', ':', '=', '-', '\n', '\t','®']
        for x in special_symbols:
            text = text.replace(x,f'\{x}')
        driver.execute_script('arguments[0].value = "' + text + '";', element)
        print(text)
    
        
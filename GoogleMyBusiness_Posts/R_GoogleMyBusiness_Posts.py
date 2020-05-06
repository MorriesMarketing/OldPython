from O_Selenium import SeleniumDrivers
from O_Days import Today
from O_Login import Login

class GmbPosts(SeleniumDrivers, Today):

    def __init__(self):
        SeleniumDrivers.__init__(self)
        self.driver = self.CHROME


    def run(self):
        Login()
        
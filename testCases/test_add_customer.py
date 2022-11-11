import pytest, time, string, random
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
	baseURL = ReadConfig.getApplicationURL()
	email = ReadConfig.getUserEmail()
	password = ReadConfig.getPassword()
	logger = LogGen.loggen()

	def test_addCustomer(self, setup):
		self.logger.info("Test_003_AddCustomer")
		self.driver = setup
		self.driver.get(self.baseURL)
		self.driver.maximize_window()

		self.lp = LoginPage(self.driver)
		self.lp.setEmail(self.email)
		self.lp.setPassword(self.password)
		self.lp.clickLogin()
		self.logger.info("Login Successful")

		self.addcust = AddCustomer(self.driver)
		self.addcust.clickOnCustomerMenu()
		self.addcust.clickOnCustomerMenuItem()

		self.addcust.clickOnAddNew()

		self.logger("Providing Customer Info")





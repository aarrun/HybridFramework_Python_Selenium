import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
	baseURL = ReadConfig.getApplicationURL()
	Email = ReadConfig.getUserEmail()
	Password = ReadConfig.getPassword()
	logger = LogGen.loggen()

	@pytest.mark.regression
	def test_searchCustomerByName(self, setup):
		self.logger.info("SearchSearchCustomerByName_005")
		self.driver = setup
		self.driver.get(self.baseURL)
		self.driver.maximize_window()

		self.lp = LoginPage(self.driver)
		self.lp.setEmail(self.Email)
		self.lp.setPassword(self.Password)
		self.lp.clickLogin()
		self.logger.info("Login Successful")

		self.logger.info("Search Customer Test Started")

		self.addcust = AddCustomer(self.driver)
		self.addcust.clickOnCustomerMenu()
		self.addcust.clickOnCustomerMenuItem()

		self.logger.info(" searching customer by Name")
		searchcust = SearchCustomer(self.driver)
		searchcust.setFirstname("Victoria")
		searchcust.setLastname("Terces")
		searchcust.clickSearch()
		time.sleep(5)
		status = searchcust.searchCustomerByName("Victoria Terces")
		assert True == status
		self.logger.info("Test Finished")
		self.driver.close()

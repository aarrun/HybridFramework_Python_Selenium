import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
	baseURL = ReadConfig.getApplicationURL()
	email = ReadConfig.getUserEmail()
	password = ReadConfig.getPassword()

	logger = LogGen.loggen()

	@pytest.mark.sanity
	@pytest.mark.regression
	def test_homePageTitle(self, setup):
		self.logger.info("****Test_001_Login*****")
		self.logger.info("Verifying")
		self.driver = setup
		self.driver.get(self.baseURL)
		act_title = self.driver.title

		if act_title == "Your store. Login":
			assert True
			self.driver.close()

		else:
			self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
			self.driver.close()
			self.logger.error("****Test_001_Login*****")
			assert False

	@pytest.mark.sanity
	@pytest.mark.regression
	def test_login(self, setup):
		self.logger.info("Login Test")
		self.driver = setup
		self.driver.get(self.baseURL)
		self.lp = LoginPage(self.driver)
		self.driver.implicitly_wait(10)
		self.lp.setEmail(self.email)
		self.lp.setPassword(self.password)
		self.lp.clickLogin()
		act_title = self.driver.title
		if act_title == "Dashboard / nopCommerce administration":
			assert True
			self.driver.close()

		else:
			self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
			self.driver.close()
			assert False

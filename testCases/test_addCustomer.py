import pytest, time, string, random
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_003_AddCustomer:
	baseURL = ReadConfig.getApplicationURL()
	email = ReadConfig.getUserEmail()
	password = ReadConfig.getPassword()
	logger = LogGen.loggen()

	@pytest.mark.sanity
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

		self.logger.info("Providing Customer Info")

		def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
			return ''.join(random.choice(chars) for x in range(size))

		self.email = random_generator() + "@gmail.com"
		self.addcust.setEmail(self.email)
		self.addcust.setPassword("test123")
		self.addcust.setFirstName("Arun")
		self.addcust.setLastName("Poojary")
		self.addcust.setGender("Male")
		self.addcust.setDOB("02/25/1994")
		self.addcust.setCompanyName("Octrans")
		self.addcust.setVendor("Vendor 2")
		self.addcust.setAdminComment("Testing")
		self.addcust.setCustomerRoles("Guests")
		self.addcust.clickOnSave()

		self.logger.info(" Saving Customer Info")
		self.logger.info("Add customer validation started")

		self.msg = self.driver.find_element(By.TAG_NAME, "body").text

		if 'The new customer has been added successfully.' in self.msg:
			assert True == True
			self.logger.info("Test Passed")

		else:
			self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
			self.logger.error("Test Failed")
			assert True == False








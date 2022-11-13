from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import pytest


class Test_002_DDT_Login:
	baseURL = ReadConfig.getApplicationURL()
	path = ".//TestData//LoginData.xlsx"
	logger = LogGen.loggen()

	@pytest.mark.regression
	def test_login_ddt(self, setup):
		self.logger.info("Login Test")
		self.driver = setup
		self.driver.get(self.baseURL)
		self.lp = LoginPage(self.driver)

		self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

		lst_status = []

		for r in range(2, self.rows + 1):
			self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
			self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
			self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
			self.driver.implicitly_wait(10)
			self.lp.setEmail(self.email)
			self.lp.setPassword(self.password)
			self.lp.clickLogin()
			time.sleep(5)

			act_title = self.driver.title
			exp_title = "Dashboard / nopCommerce administration"

			if act_title == exp_title:
				if self.exp == "Pass":
					self.logger.info("Test Passed")
					self.lp.clickLogout()
					lst_status.append("Pass")

				elif self.exp == "Fail":
					self.logger("Test Failed")
					self.lp.clickLogout()
					lst_status.append("Fail")

			elif act_title != exp_title:
				if self.exp == 'Pass':
					self.logger.info("Failed")
					lst_status.append('Fail')

				elif self.exp == 'Fail':
					self.logger.info("Passed")
					lst_status.append('Pass')

		if 'Fail' not in lst_status:
			self.logger.info('Login DDT Test is passed')
			self.driver.close()
			assert True
		else:
			self.logger.info('Login DDT Test is failed')
			self.driver.close()
			assert False

		self.logger.info("End of DDT")
		self.logger.info("Completed TC_LoginDDT_OO2")

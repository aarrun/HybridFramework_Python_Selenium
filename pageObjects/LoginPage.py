from selenium.webdriver.common.by import By


class LoginPage:
	textbox_email_xpath = "//input[@id='Email']"
	textbox_password_id = "Password"
	button_login_xpath = "//button[@type='submit']"
	link_logout_linktext = "Logout"

	def __init__(self, driver):
		self.driver = driver

	def setEmail(self, email):
		self.driver.implicitly_wait(10)
		self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
		self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

	def setPassword(self, password):
		self.driver.find_element(By.ID, self.textbox_password_id).clear()
		self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

	def clickLogin(self):
		self.driver.find_element(By.XPATH, self.button_login_xpath).click()

	def clickLogout(self):
		self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()



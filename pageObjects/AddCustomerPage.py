import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
	lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
	lnkCustomers_menuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
	btnAddNew_xpath = "//a[@class='btn btn-primary']"
	txtEmail_xpath = "//input[@id='Email']"
	txtPassword_xpath = "// input[ @ id = 'Password']"
	txtFirstname_xpath = "//input[@id='FirstName']"
	txtLastname_xpath = "//input[@id='LastName']"
	rdMaleGender_xpath = "//input[@id='Gender_Male']"
	rdFemaleGender_xpath = "//input[@id='Gender_Female']"
	txtDOB_xpath = "//input[@id='DateOfBirth']"
	txtCompanyName_xpath = "//input[@id='Company']"
	chkboxTAX_xpath = "//input[@id='IsTaxExempt']"
	dropdownNewsletter_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down']//div[@role='listbox']"
	lstItemYourStore_xpath = "//li[normalize-space()='Your store name']"
	lstItemTS2_xpath = "//li[normalize-space()='Test store 2']"
	dropdownManager_xpath = "//select[@id='VendorId']"
	optNotVendor_xpath = "//option[@value='0']"
	optNotVendor1_xpath = "//option[@value='1']"
	optNotVendor2_xpath = "//option[@value='2']"
	chkboxActive_xpath = "//input[@id='Active']"
	txtAdminComment_xpath = "//textarea[@id='AdminComment']"
	txtboxCustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-focused k-state-hover k-state-border-down']//div[@role='listbox']"
	lstItemAdmins_xpath = "//li[normalize-space()='Administrators']"
	lstItemForumMods_xpath = "//li[normalize-space()='Forum Moderators']"
	lstItemGuests_xpath = "//li[normalize-space()='Guests']"
	lstItemRegistered_xpath = "//li[normalize-space()='Registered']"
	lstItemVendors_xpath = "//li[contains(text(),'Vendors')]"
	btnSave_xpath = "//button[@name='save']"

	def __init__(self, driver):
		self.driver = driver

	def clickOnCustomerMenu(self):
		self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

	def clickOnCustomerMenuItem(self):
		self.driver.find_element(By.XPATH, self.lnkCustomers_menuItem_xpath).click()

	def clickOnAddNew(self):
		self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

	def setEmail(self, email):
		self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

	def setPassword(self, password):
		self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

	def setFirstName(self, fname):
		self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(fname)

	def setLastName(self, lname):
		self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lname)

	def setDOB(self, dob):
		self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

	def setCompanyName(self, company):
		self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(company)

	def setVendor(self, value):
		drp = Select(self.driver.find_element(By.XPATH, self.dropdownManager_xpath))
		drp.select_by_visible_text(value)

	def setCustomerRoles(self, role):
		self.driver.find_element(By.XPATH, self.txtboxCustomerRoles_xpath).click()
		time.sleep(3)

		if role == 'Registered':
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)

		elif role == 'Guests':
			time.sleep(3)
			self.driver.find_element(By.XPATH, "//span[normalize-space()='Registered']").click()
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuests_xpath)

		elif role == 'Registered':
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)

		elif role == 'Administrators':
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemAdmins_xpath)

		elif role == 'Vendor':
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemVendors_xpath)

		elif role == 'ForumMods':
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemForumMods_xpath)

		else:
			self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuests_xpath)

		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.listitem)

	def setGender(self, gender):
		if gender == 'Male':
			self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

		elif gender == 'Female':
			self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()

		else:
			self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
	if browser == "chrome":
		driver = webdriver.Chrome()
		print("Launching Chrome Browser")

	elif browser == "firefox":
		driver = webdriver.Firefox()
		print("Launching Firefox Browser")

	else:
		driver = webdriver.Chrome()

	return driver


def pytest_addoption(parser):
	parser.addoption("--browser")


@pytest.fixture()
def browser(request):
	return request.config.getoption("--browser")


# Pytest HTML Report

def pytest_configure(config):
	config._metadata["Project Name"] = "nopcommerce"
	config._metadata["Module Name"] = "Customers"
	config._metadata["Tester"] = "Arun"

from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()




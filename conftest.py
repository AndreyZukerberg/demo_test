import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Users\Андрей\firefox.exe'
options.add_argument('--headless')

@pytest.fixture
def browser():
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
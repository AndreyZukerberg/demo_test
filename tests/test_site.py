import time
from pages.homepage import Home_page
from pages.product import ProductPage
import pytest


def test_open_s6(browser):

    home_page = Home_page(browser)
    home_page.open()
    home_page.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')



def test_two_monitors(browser):
    home_page = Home_page(browser)
    home_page.open()
    home_page.click_monitor()
    time.sleep(2)
    home_page.check_products_count(2)
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import pytest
import time
from tests.homepage_locators import Locators
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_home(self):
        driver_homepage = Locators(self.driver)

        driver_homepage.test_autoseggest()

        driver_homepage.test_radio_button()

        driver_homepage.test_dro_dow()
        time.sleep(2)

        driver_homepage.test_check_box()

        driver_homepage.test_win()

        driver_homepage.test_nw_windo("work")

        driver_homepage.test_alert()

        driver_homepage.test_table_amount()

        driver_homepage.test_mouse_hover()

        driver_homepage.test_ifrm()

        driver_homepage.test_practice()

    def test_newtab(self):
        driver_homepage = Locators(self.driver)

        # driver_homepage.test_new_tab()












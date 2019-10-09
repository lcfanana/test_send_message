import time
import pytest

from base.base_data import data_file
from base.get_driver import init_driver
from page.page import Page
import allure

class TestSend:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("args",data_file("send_message.yaml","test_add"))
    def test_send(self,args):
        self.page.message_frist.click_meassage_button()
        self.page.send_message.send_recipe_person(args["phone"])
        self.page.send_message.send_word(args["text"])
        self.page.send_message.click_send_button()

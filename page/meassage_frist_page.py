from selenium.webdriver.common.by import By
import allure
from base.action import BaseAction


class Message_Frist_Page(BaseAction):
    add_meassage_button=By.ID,"com.android.mms:id/action_compose_new"
    @allure.step(title="点击添加短信按钮")

    def click_meassage_button(self):
        self.click(self.add_meassage_button)

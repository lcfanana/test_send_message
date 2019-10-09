from selenium.webdriver.common.by import By
import allure
from base.action import BaseAction


class SendMessagePage(BaseAction):
    recipe_person=By.ID,"com.android.mms:id/recipients_editor"
    word=By.ID,"com.android.mms:id/embedded_text_editor"
    send_button=By.XPATH,"//*[@content-desc='发送']"
    @allure.step(title="输入接收人号码")
    def send_recipe_person(self,person):
        allure.attach("接收人号码",person,allure.attach_type.TEXT)
        self.input(self.recipe_person,person)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="输入短信内容")
    def send_word(self,word):
        allure.attach("短信内容",word, allure.attach_type.TEXT)
        self.input(self.word,word)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="点击发送短信按钮")
    def click_send_button(self):
        self.click(self.send_button)
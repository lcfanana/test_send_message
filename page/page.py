from page.meassage_frist_page import Message_Frist_Page
from page.send_message_page import SendMessagePage


class Page:
    def __init__(self,driver):
        self.driver=driver
    @property
    def message_frist(self):
        return Message_Frist_Page(self.driver)
    @property
    def send_message(self):
        return SendMessagePage(self.driver)



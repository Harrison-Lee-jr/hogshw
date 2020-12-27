from appium.webdriver.common.mobileby import MobileBy

from test_appium201227.PO_appium.page.base_page import BasePage
from test_appium201227.PO_appium.page.contact_add import ContactAdd


class MemberInviteMenuPage(BasePage):
    '''添加成员PO'''
    def add_member_menual(self):
        '''手动添加成员信息'''
        # todo 点击手动添加成员信息
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
        return ContactAdd(self.driver)
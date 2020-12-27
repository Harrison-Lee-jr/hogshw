from appium.webdriver.common.mobileby import MobileBy

from test_appium201227.PO_appium.page.address_list_page import AddressListPage
from test_appium201227.PO_appium.page.base_page import BasePage


class MainPage(BasePage):
    '''首页PO'''
    def goto_address(self):
        '''进入通讯录'''
        # 点击通讯录按钮
        print("点击通讯录按钮")
        self.find_and_click(MobileBy.XPATH,"//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")
        return AddressListPage(self.driver)

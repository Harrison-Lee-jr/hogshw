from appium.webdriver.common.mobileby import MobileBy
from test_appium201227.PO_appium.page.base_page import BasePage


class ContactAdd(BasePage):
    '''成员信息编辑'''
    def add_contact(self):
        '''添加信息'''
        # todo 姓名、性别、手机号填写
        self.find_and_send(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@text='必填']",'aaaaa')
        self.find_and_click(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']")
        # 加载慢时，有可能会找到下面那层的”男”，而不是弹框的男，所以可以加一个显式等待来避免
        self.wait_for(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_send(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//*[@text='手机号']",'13119191614')
        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")
        return True
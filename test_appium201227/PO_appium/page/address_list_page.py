from test_appium201227.PO_appium.page.base_page import BasePage
from test_appium201227.PO_appium.page.member_invite_menu_page import MemberInviteMenuPage

class AddressListPage(BasePage):
    '''通讯录PO'''
    def click_addmember(self):
        '''添加成员'''
        # todo 点击添加成员
        print('点击添加成员')
        self.scroll_find_click('添加成员')
        # self.swip_find_click(MobileBy.XPATH,"//*['添加成员']")
        return MemberInviteMenuPage(self.driver)

from time import sleep
from selenium.webdriver.common.by import By
from test_web_weixin_hw.page.add_depart import AddDepart
from test_web_weixin_hw.page.base_page import BasePage

class ContactPage(BasePage):
    _location_member_list=(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_addmember=(By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    _location_goto_adddepart_add=(By.CSS_SELECTOR,".js_create_dropdown")
    _location_goto_add_depart = (By.CSS_SELECTOR, ".js_create_party")
    _location_get_departname=(By.CSS_SELECTOR,".jstree-last .jstree-anchor:nth-last-child(1)")

    def goto_add_member_bycontact(self):
        '''添加成员操作'''
        from test_web_weixin_hw.page.add_member import AddMember
        # 在函数内导入，避免循环导入的问题
        # WebDriverWait(self.driver,9).until(
        #     expected_conditions.element_to_be_clickable(self._location_goto_addmember))
        #添加显式等待，保证按钮可以点击
        self.wait_click(self._location_goto_addmember)
        self.find(self._location_goto_addmember).click()
        return AddMember(self.driver)

    def get_member(self):
        sleep(1)
        '''获取成员列表，用来做断言'''
        # member_list=self.driver.find_elements(*self._location_member_list)
        member_list = self.finds(*self._location_member_list)
        # member_list_res=[i.text for i in member_list] #优化，下面3行等于本行
        member_list2=[]
        for i in member_list:
            member_list2.append(i.text)
        return member_list2

    def goto_add_depart(self):
        '''添加部门操作'''
        self.find(self._location_goto_adddepart_add).click()
        self.find(self._location_goto_add_depart).click()
        return AddDepart(self.driver)

    def get_depart_name(self):
        '''获取部门名字'''
        # depart_name=self.find(self._location_get_departname).text
        sleep(1)
        depart_list=self.finds(self._location_get_departname)
        depart_name_list=[]
        for i in depart_list:
            depart_name_list.append(i.text)
        print(depart_name_list)
        return depart_name_list

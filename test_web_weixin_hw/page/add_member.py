from time import sleep
from selenium.webdriver.common.by import By
from test_web_weixin_hw.page.base_page import BasePage
from test_web_weixin_hw.page.contact_page import ContactPage


class AddMember(BasePage):
    # 前面加_使之变成私有变量，因为在case文件无需知道这些元素，原则：不要暴露内部元素给外部
    _location_username=(By.ID,"username")
    _location_acctid=(By.ID,"memberAdd_acctid")
    _location_Add_phone=(By.ID,"memberAdd_phone")

    def add_member(self):
        '''添加成员操作'''
        # driver=webdriver.Chrome() #抽取到base_page 下方driver报红，解决：在类方法(继承base_page)
        self.driver.find_element(*self._location_username).send_keys('rong')
        self.driver.find_element(*self._location_acctid).send_keys('137')
        self.driver.find_element(*self._location_Add_phone).send_keys('13119191614')
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        return ContactPage(self.driver)
        # 传入self.driver，让它不用再打开一次网页

    def add_member_fail(self,acctid,phone):
        self.driver.find_element(*self._location_username).send_keys('rong')
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        # error_message=self.driver.find_element(By.CSS_SELECTOR,".member_edit_item.member_edit_item_Account .ww_inputWithTips_tips").text
        # #手机占有
        # error_phone=self.driver.find_element(By.CSS_SELECTOR,".ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list=[error_message,error_phone]
        sleep(1.5)
        res =self.finds(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        print(res)
        error_list=[i.text for i in res]
        print(error_list)
        return error_list

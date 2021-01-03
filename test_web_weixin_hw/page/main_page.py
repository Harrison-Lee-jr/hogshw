from time import sleep
from selenium.webdriver.common.by import By
from test_web_weixin_hw.page.add_member import AddMember
from test_web_weixin_hw.page.base_page import BasePage
from test_web_weixin_hw.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member=(By.CSS_SELECTOR,'.ww_indexImg_AddMember')
    def goto_add_member(self):
        '''跳转到添加成员'''
        # driver=webdriver.Chrome() #抽取到base_page,下方driver报红，解决：在类方法(继承base_page)
        self.driver.find_element(*self._location_goto_member).click()
        # 上面括号里加*是因为find_element需要传入两个值，但抽取元素到属性后变成了一个元组，*是解包，解成两个参数传入
        # self.find(*self._location_goto_member).click() # 结合封装的find方法
        return AddMember(self.driver)
        # 传入self.driver，让它不用再打开一次网页

    def goto_contact(self):
        '''跳转到通讯录页面'''
        self.find(By.ID,'menu_contacts').click()
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID,"menu_index").click()
        sleep(2)
        self.find(By.CSS_SELECTOR,"a[node-type='cancel'").click()
        sleep(2)
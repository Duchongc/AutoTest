# conding:utf-8
#from common.zendao_login import *
import time
import unittest
from selenium import webdriver
class TestLogin(unittest.TestCase):
    """登录测试用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
    def setUp(self):
        self.driver.get("http://47.98.214.128/zentao/index.php")
        time.sleep(3)
    def is_elart(self):
        time.sleep(3)
        try:
            a=self.driver.switch_to.alert
            text=a.text
            a.accept()
            return text
        except:
            return ""
    def is_get_login_username(self):
        try:
            self.element = self.driver.find_element_by_css_selector("span.user-name").text
            return self.element
        except:
            return ""
    def test_01(self):
        '''正确的账户和密码'''
        self.driver.find_element_by_css_selector("#account").send_keys("yingzi")
        self.driver.find_element_by_css_selector('[name="password"]').send_keys("admin123..")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        t=self.is_get_login_username()
        self.assertTrue(t=="英子")
    def test_02(self):
        '''错误的账户和正确密码'''
        self.driver.find_element_by_css_selector("#account").send_keys("yingzi11")
        self.driver.find_element_by_css_selector('[name="password"]').send_keys("admin123..")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        t=self.is_get_login_username()
        self.assertTrue(t=="")
    def test_03(self):
        '''正确的账户和错误的密码'''
        self.driver.find_element_by_css_selector("#account").send_keys("yingzi")
        self.driver.find_element_by_css_selector('[name="password"]').send_keys("admin123..11")
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        t=self.is_get_login_username()
        self.assertTrue(t=="")
    def tearDown(self):
        self.is_elart()
        self.driver.delete_all_cookies()
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()





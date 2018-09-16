from src.entity.jianyishuPage import jianyishuPage
from src.functions.LoginAction import *
from time import sleep
class jianyishuAction(object):
    @staticmethod
    def click_jianyishu(driver, name, datas):
            jianyishu = jianyishuPage(driver)
            sleep(5)
            jianyishu.clicks().click()    # 点击建议书
            sleep(5)
            jianyishu.adduser().click()    # 点击新增
            sleep(5)
            jianyishu.bbr_name().send_keys(name)   # 输入姓名
            sleep(1)
            jianyishu.bbr_sex_g().click()   # 性别
            sleep(1)
            jianyishu.bbr_from().send_keys(datas)   # 出生日期
            sleep(1)
            jianyishu.bbr_work().click()   # 职业
            sleep(1)
            jianyishu.bbr_work_one().click()  # 职业一级
            sleep(1)
            jianyishu.bbr_work_one_one().click()  # 职业二级
            sleep(1)
            jianyishu.bbr_work_one_one_one().click()   # 职业三级
            sleep(1)
            jianyishu.bbr_work_one_one_sure().click()   # 职业确定
            sleep(1)
            jianyishu.bbr_beibaoren().click()   #  选择被保险人关系
            sleep(1)
            jianyishu.bbr_beibaoren_guanxi().click()
            sleep(1)
            jianyishu.shejixianzhong().click()   # 点击下一步
            sleep(10)

if __name__== '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://tstmobile.gwcslife.com/NGLife/")
    LoginAction.login(driver,username="sh0000002",password="Aa111111")
    time.sleep(3)
    jianyishuAction.click_jianyishu(driver,'zhaolili','1990-10-10')
    time.sleep(10)





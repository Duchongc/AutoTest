from src.common.ObjectMap import *
from src.common.ParseConfigurationFile import ParseCofigFile

class jianyishuPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.homePage = self.parseCF.getItemsSection("changsheng_jianyishu")

    def clicks(self):  # 首页点击建议书
        try:
            locateType,locatorExperession = self.homePage["jianyishu.jianyishu".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def adduser(self):  # 点击新增
        try:
            locateType,locatorExperession = self.homePage["jianyishu.adduser".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_name(self):  # 点击输入姓名
        try:
            locateType,locatorExperession = self.homePage["beibaoren.name".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_sex_b(self):  # 选择姓名——男
        try:
            locateType,locatorExperession = self.homePage["beibaoren.insSexMImg".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_sex_g(self):   # 选择姓名--女
        try:
            locateType,locatorExperession = self.homePage["beibaoren.insSexFImg".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_from(self):   # 选择出生日期
        try:
            locateType,locatorExperession = self.homePage["beibaoren.from".lower()].split(">")
            js = 'document.getElementById("%s").removeAttribute("disabled");' %locatorExperession
            print('js是:'+js)
            self.driver.execute_script(js)
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_work(self): # 选择职业
        try:
            locateType,locatorExperession = self.homePage["beibaoren.work".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_work_one(self):
        try:
            locateType,locatorExperession = self.homePage["beibaoren.work.one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_work_one_one(self):
        try:
            locateType,locatorExperession = self.homePage["beibaoren.work.one.one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e

    def bbr_work_one_one_one(self):
        try:
            locateType, locatorExperession = self.homePage["beibaoren.work.one.one.one".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_work_one_one_sure(self):  # 选择职业点击确定
        try:
            locateType, locatorExperession = self.homePage["beibaoren.work.one.one.sure".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_beibaoren(self):  # 点击被保人
        try:
            locateType, locatorExperession = self.homePage["toubaoren.beibaoren".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_beibaoren_guanxi(self):  # 选择被保人关系
        try:
            locateType, locatorExperession = self.homePage["toubaoren.beibaoren.guanxi".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def shejixianzhong(self):
        try:
            locateType, locatorExperession = self.homePage["jianyishu.shejixianzhong".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e

from src.common.ObjectMap import *
from src.common.ParseConfigurationFile import ParseCofigFile

class zhunkehuPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.homePage = self.parseCF.getItemsSection("changsheng_zhunkehu")
    def clicks(self):  # 首页点击准客户管理
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.zhunkehu".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_button(self):  # 点击新增
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_button".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_Name(self):  # 输入姓名
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_name".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_Birthday(self):  # 点击出生日期
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_birthday".lower()].split(">")
            js = 'document.getElementById("%s").removeAttribute("disabled");' %locatorExperession
            self.driver.execute_script(js)
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_work(self):  # 职业代码
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_work".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_work_one(self):  # 职业代码一层
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_work_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_work_one_one(self):  #职业代码二层
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_work_one_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_work_one_one_one(self):  # 职业代码三层
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_work_one_one_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_work_one_one_sure(self):  # 职业代码点击确定
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_work_one_one_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_term_of_validity(self):  # 证件有效期
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_term_of_validity".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_HealthFlag(self):  # 医保标志
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_HealthFlag".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_HealthFlags(self):  # 医保标志选择
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_HealthFlags".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_saveCustom(self):  # 点击底部确定
        try:
            locateType,locatorExperession = self.homePage["zhunkehu.add_saveCustom".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_resultPanel(self):  # 点击修改
        try:
            locateType, locatorExperession = self.homePage["zhunkehu.add_resultPanel".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_tosug(self):  # 点击建议书
        try:
            locateType, locatorExperession = self.homePage["zhunkehu.add_tosug".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def addd_toefrom(self):  # 点击电子投保
        try:
            locateType, locatorExperession = self.homePage["zhunkehu.addd_toefrom".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExperession)
            return elementObj
        except Exception as e:
            raise e
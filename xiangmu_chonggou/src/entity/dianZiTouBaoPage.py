from src.common.ObjectMap import *
from src.common.ParseConfigurationFile import ParseCofigFile
from selenium.webdriver.common.action_chains import ActionChains
class dianZiTouBaoPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.homePage = self.parseCF.getItemsSection("changsheng_dianzitoubao")
    def clicks(self):  # 首页点击电子投保
        try:
            locateType,locatorExperession = self.homePage["dztb.dainzitoubao".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_button(self):  # 点击新增
        try:
            locateType,locatorExperession = self.homePage["dztb.add".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def add_and_sure(self):  # 点击同意
        try:
            locateType,locatorExperession = self.homePage["dztb.add_and_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_name(self):  # 姓名  homePage.add_beibaoren_name
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_name".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_male(self):  # 性别男  homePage.add_beibaoren_male
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_male".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_female(self):  # 性别女 homePage.add_beibaoren_female
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_female".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_idtype(self):  # 证件类型  add_beibaoren_idtype
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_idtype".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_idtypes(self):  # 选择证件类型  dztb.add_beibaoren_idtypes
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_idtypes".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_idnumber(self):  # 证件内容 dztb.add_beibaoren_idnumber
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_idnumber".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_idtime(self):  # 证件有效期  dztb.add_beibaoren_idtime
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_idtime".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_birthday(self):  # 出生日期  dztb.add_beibaoren_birthday
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_birthday".lower()].split(">")
            js = 'document.getElementById("%s").removeAttribute("disabled");' %locatorExperession
            self.driver.execute_script(js)
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_Marriage(self):  # 婚姻状况  dztb.add_beibaoren_Marriage
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_Marriage".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_Marriages(self):  # 选择婚姻状况 dztb.add_beibaoren_Marriages
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_Marriages".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HJSZD(self):  # 户籍所在地  dztb.add_beibaoren_HJSZD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HJSZD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HJSZDs(self):  # 选择户籍所在地  dztb.add_beibaoren_HJSZDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HJSZDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_YearSalary(self):  # 平均年收入  dztb.add_beibaoren_YearSalary
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_YearSalary".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_PROVNCD(self):  # 家庭住址，省  dztb.add_beibaoren_PROVNCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_PROVNCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_PROVNCDs(self):  # 家庭住址，选择省  dztb.add_beibaoren_PROVNCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_PROVNCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_CITYCD(self):  # 家庭住址，市  dztb.add_beibaoren_CITYCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_CITYCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_CITYCDs(self):  # 家庭住址，选择市  dztb.add_beibaoren_CITYCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_CITYCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_DSTRCTCD(self):  # 家庭住址，县（区）  dztb.add_beibaoren_DSTRCTCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_DSTRCTCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_DSTRCTCDs(self):  # 家庭住址，选择县（区）  dztb.add_beibaoren_DSTRCTCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_DSTRCTCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HomeDetailAddr(self):  # 输入详细地址  dztb.add_beibaoren_HomeDetailAddr
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HomeDetailAddr".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HomeZipCode(self):  # 家庭住址邮编  dztb.add_beibaoren_HomeZipCode
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HomeZipCode".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GrpName(self):  # 单位name  dztb.add_beibaoren_GrpName
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GrpName".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPPROVNCD(self):  # 单位住址，省  dztb.add_beibaoren_GRPPROVNCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPPROVNCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPPROVNCDs(self):  # 单位住址，选择省  dztb.add_beibaoren_GRPPROVNCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPPROVNCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPCITYCD(self):  # 单位住址，市  dztb.add_beibaoren_GRPCITYCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPCITYCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPCITYCDs(self):  # 单位住址，选择市  dztb.add_beibaoren_GRPCITYCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPCITYCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPDSTRCTCD(self):  # 单位住址，县（区） dztb.add_beibaoren_GRPDSTRCTCD
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPDSTRCTCD".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GRPDSTRCTCDs(self):  # 单位住址，选择县（区）  dztb.add_beibaoren_GRPDSTRCTCDs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GRPDSTRCTCDs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GrpDetailAddr(self):  # 单位地址  dztb.add_beibaoren_GrpDetailAddr
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GrpDetailAddr".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_GrpZipCode(self):  # 单位邮编  dztb.add_beibaoren_GrpZipCode
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_GrpZipCode".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HealthFlag(self):  # 单位医保 dztb.add_beibaoren_HealthFlag
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HealthFlag".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_HealthFlags(self):  # 选择单位医保 dztb.add_beibaoren_HealthFlags
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_HealthFlags".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_detailWork(self):  # 点击职业代码  dztb.add_beibaoren_detailWork
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_detailWork".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_detailWork_one(self):  # 点击职业代码一级 dztb.add_beibaoren_detailWork_one
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_detailWork_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_detailWork_one_one(self):  # 点击职业代码二级
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_detailWork_one_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_detailWork_one_one_one(self):  # 点击职业代码三级  dztb.add_beibaoren_detailWork_one_one_one
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_detailWork_one_one_one".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_detailWork_one_one_sure(self):  # 职业代码 确定按钮  dztb.add_beibaoren_detailWork_one_one_sure
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_detailWork_one_one_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def bbr_Mobile(self):  # 移动电话  dztb.add_beibaoren_Mobile
        try:
            locateType,locatorExperession = self.homePage["dztb.add_beibaoren_Mobile".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbr_action(self):  # 点击投保人 dztb.add_toubaoren_action
        try:
            locateType,locatorExperession = self.homePage["dztb.add_toubaoren_action".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbr_Appntrela(self):  # 投保人和被保人关系  dztb.add_toubaoren_Appntrela
        try:
            locateType,locatorExperession = self.homePage["dztb.add_toubaoren_Appntrela".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbr_Appntrelas(self):  #   dztb.add_toubaoren_Appntrelas
        try:
            locateType,locatorExperession = self.homePage["dztb.add_toubaoren_Appntrelas".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def syr_action(self):  # 点击受益人 dztb.add_shouyiren_action
        try:
            locateType,locatorExperession = self.homePage["dztb.add_shouyiren_action".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_action(self):  #  tbjh_action
        try:
            locateType,locatorExperession = self.homePage["dztb.add_toubaojihua_action".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e

    def target(self):     # 元素聚焦   dztb.add_addRiskMain
        try:
            locateType, locatorExperession = self.homePage["dztb.add_addRiskMain".lower()].split(">")
            target = getElement(self.driver, locateType, locatorExperession)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            print(target)
            return target
        except Exception as e:
            print(e)
    def tbjh_addRiskMain(self):  # 点击添加主险 dztb.add_addRiskMain
        try:
            locateType,locatorExperession = self.homePage["dztb.add_addRiskMain".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_add_zhuxian(self):  # 点击选择主险 dztb.add_zhuxian
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_add_zhuxian_sure(self):  # 点击主险确认 dztb.add_zhuxian_sure
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_PayIntv(self):  # 点击缴费方式 dztb.add_zhuxian_PayIntv
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_PayIntv".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_PayIntvs(self):  # 选择缴费方式 dztb.add_zhuxian_PayIntvs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_PayIntvs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_Amnt(self):  # 保额 dztb.add_zhuxian_Amnt
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_Amnt".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_Prem(self):  # 保费 dztb.add_zhuxian_Prem
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_Prem".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_sureAddBtn(self):  # 主险确定 dztb.add_zhuxian_sureAddBtn
        try:
            locateType,locatorExperession = self.homePage["dztb.add_zhuxian_sureAddBtn".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_saveSubRisks(self):  # 点击附加险 dztb.add_fujiaxian_saveSubRisks
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_saveSubRisks".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_add_fujiaxian(self):  # 选择附加险 dztb.add_fujiaxian
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_affirmSubRisks(self):  # 选择附加险 确认 dztb.add_fujiaxian_affirmSubRisks
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_affirmSubRisks".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_fjx_PayIntv(self):  # 附加险选择缴费方式 dztb.add_fujiaxian_PayIntv
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_PayIntv".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_fjx_PayIntvs(self):  #  dztb.add_fujiaxian_PayIntvs
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_PayIntvs".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_fjx_Amnt(self):  # 保额 dztb.add_fujiaxian_Amnt
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_Amnt".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_fjx_Prem(self):  # 保费 dztb.add_fujiaxian_Prem
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_Prem".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def tbjh_fjx_sureAddBtn(self):  # 附加险确定 dztb.add_fujiaxian_sureAddBtn
        try:
            locateType,locatorExperession = self.homePage["dztb.add_fujiaxian_sureAddBtn".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_action(self):  # 点击相关告知 dztb.add_gaozhi_action
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_action".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_ybgz_allfalse(self):  # 一般告知 一键全否 dztb.add_gaozhi_f_allFalse_f
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_f_allFalse_f".lower()].split(">")
            target = getElement(self.driver,locateType,locatorExperession)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return target
        except Exception as e:
            raise e
    def xggz_ybgz_sure(self):  # 一般告知 一键全否确认 dztb.add_gaozhi_sure
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_sure".lower()].split(">")
            target = getElement(self.driver,locateType,locatorExperession)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            return target
        except Exception as e:
            raise e
    def xggz_ybgz_finish(self):  # 一般告知 完成 dztb.add_gaozhi_finish_f
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_finish_f".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_jkgz_one(self):  # 健康告知 第一个填空 dztb.add_gaozhi_h_height
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_h_height".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_jkgz_two(self):  # 健康告知 第二个填空  dztb.add_gaozhi_h_weight
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_h_weight".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_jkgz_allfalse(self):  # 健康告知 一键全否 dztb.add_gaozhi_h_allFalse_h
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_h_allFalse_h".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_jkgz_sure(self):  # 健康告知 确定 dztb.add_gaozhi_h_sure
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_h_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_jkgz_finish(self):  # 健康告知 完成 dztb.add_gaozhi_h_finish_h
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_h_finish_h".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_one(self):  # 营销员告知 第一个填空 dztb.add_gaozhi_a_Acquaintance
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_Acquaintance".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_two(self):  # 营销员告知 陌生拜访  dztb.add_gaozhi_a_renshi
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_renshi".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_three(self):  # 营销员告知 家庭保障 dztb.add_gaozhi_a_mudi
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_mudi".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_four(self):  # 被保人工作 学历dztb.add_gaozhi_a_bbr
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_bbr".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_five(self):  # 投保人工作学历 dztb.add_gaozhi_a_tbr
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_tbr".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_allfalse(self):  # 营销员告知 一键全否 dztb.add_gaozhi_a_allFalse
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_allFalse".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_sure(self):  # 营销员告知 确定 dztb.add_gaozhi_a_sure
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_sure".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_yxygz_finish(self):  # 营销员告知 完成 dztb.add_gaozhi_a_finish
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_a_finish".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def xggz_next(self):  # 相关告知 下一步 dztb.add_gaozhi_next
        try:
            locateType,locatorExperession = self.homePage["dztb.add_gaozhi_next".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e

    def syr_next(self):  # 下一步  dztb.add_shouyiren_next
        try:
            locateType,locatorExperession = self.homePage["dztb.add_shouyiren_next".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e



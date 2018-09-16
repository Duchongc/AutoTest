from src.entity.dianZiTouBaoPage import dianZiTouBaoPage
from src.functions.LoginAction import *
from time import sleep
class dianZiTouBaoAction(object):
    @staticmethod
    def add_dianzitoubao(driver,name,idnumber,birthday,YearSalary,HomeDetailAddr,
                         HomeZipCode,GrpName,GrpDetailAddr,GrpZipCode,Mobile,Amnt,amnt):
        dztb = dianZiTouBaoPage(driver)
        sleep(2)
        dztb.clicks().click()
        sleep(5)
        dztb.add_button().click()
        sleep(2)
        dztb.add_and_sure().click()
        sleep(1)
        dztb.bbr_name().send_keys(name)    # 被保人姓名
        sleep(1)
        dztb.bbr_idtype().click()   # 证件类型
        sleep(1)
        dztb.bbr_idtypes().click() # 选择证件类型
        sleep(1)
        dztb.bbr_idnumber().send_keys(idnumber)  # 证件内容
        sleep(1)
        dztb.bbr_idtime().click()   # 证件有效期
        sleep(1)
        dztb.bbr_birthday().send_keys(birthday)   # 出生日期
        dztb.bbr_Marriage().click()  # 选择婚姻状况
        sleep(1)
        dztb.bbr_Marriages().click()
        sleep(5)
        dztb.bbr_HJSZD()  # 户籍所在地
        dztb.bbr_HJSZDs().click()
        dztb.bbr_YearSalary().send_keys(YearSalary)   # 平均年收入
        sleep(5)
        dztb.bbr_PROVNCD()    # 家庭住址，省
        sleep(1)
        dztb.bbr_PROVNCDs().click()
        dztb.bbr_CITYCD()     # 家庭住址，市
        dztb.bbr_CITYCDs().click()
        dztb.bbr_DSTRCTCD().click()     # 家庭住址，县（区）
        dztb.bbr_DSTRCTCDs().click()
        dztb.bbr_HomeDetailAddr().send_keys(HomeDetailAddr)   # 输入详细地址
        dztb.bbr_HomeZipCode().send_keys(HomeZipCode)     # 家庭住址邮编
        dztb.bbr_GrpName().send_keys(GrpName)
        sleep(5)
        dztb.bbr_GRPPROVNCD() # 单位地址 省
        dztb.bbr_GRPPROVNCDs().click()
        dztb.bbr_GRPCITYCD()  # 单位地址 市
        dztb.bbr_GRPCITYCDs().click()
        dztb.bbr_GRPDSTRCTCD()   # 单位地址 县
        dztb.bbr_GRPDSTRCTCDs().click()
        dztb.bbr_GrpDetailAddr().send_keys(GrpDetailAddr)  # 单位详细地址
        dztb.bbr_GrpZipCode().send_keys(GrpZipCode)  # 单位邮编
        dztb.bbr_HealthFlag()   # 医保标志
        dztb.bbr_HealthFlags().click()
        sleep(1)
        dztb.bbr_detailWork().click()    # 点击职业代码
        sleep(3)
        dztb.bbr_detailWork_one().click()  # 职业代码一级
        sleep(1)
        dztb.bbr_detailWork_one_one().click()  # 职业代码 二级
        sleep(1)
        dztb.bbr_detailWork_one_one_one().click()  # 职业代码 三级
        sleep(1)
        dztb.bbr_detailWork_one_one_sure().click()  # 职业代码  确定
        sleep(1)
        dztb.bbr_Mobile().send_keys(Mobile)   # 单位电话
        sleep(1)
        dztb.tbr_action().click()  # 点击投保人
        sleep(5)
        dztb.tbr_Appntrela()   # 选择投保人和被保人关系
        dztb.tbr_Appntrelas().click()
        sleep(5)
        dztb.syr_action().click() # 点击受益人
        sleep(10)
        dztb.tbjh_action().click()  # 点击投保计划
        sleep(10)
        dztb.tbjh_addRiskMain().click()   # 点击添加主险
        sleep(3)
        dztb.tbjh_add_zhuxian().click()   # 选择主险
        dztb.tbjh_add_zhuxian_sure().click()   # 点击确定按钮
        dztb.tbjh_PayIntv()   # 选择缴费方式
        dztb.tbjh_PayIntvs().click()
        sleep(2)
        dztb.tbjh_Amnt().send_keys(Amnt)  # 输入保额
        dztb.tbjh_Prem().click()    # 点击保费
        sleep(3)
        dztb.tbjh_sureAddBtn().click()   # 点击确定按钮
        sleep(5)
        # dztb.tbjh_saveSubRisks().click()  # 点击添加附加险
        # sleep(2)
        # dztb.tbjh_add_fujiaxian().click()  # 选择附加险
        # dztb.tbjh_affirmSubRisks().click()   # 选择附加险确认
        # sleep(1)
        # dztb.tbjh_fjx_PayIntv()  # 选择缴费方式
        # dztb.tbjh_fjx_PayIntvs().click()
        # dztb.tbjh_fjx_Amnt().send_keys(amnt)     # 输入保额
        # dztb.tbjh_fjx_Prem().click()      # 保费
        # dztb.tbjh_fjx_sureAddBtn().click()  # 附加险确认
        sleep(5)
        dztb.xggz_action().click()  # 点击相关告知
        sleep(5)
        dztb.xggz_ybgz_allfalse().click()  # 一般告知一键全否
        sleep(3)
        dztb.xggz_ybgz_sure().click()   # 一键全否 确定
        sleep(2)
        dztb.xggz_ybgz_finish().click()   # 一般告知  完成
        sleep(5)


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://tstmobile.gwcslife.com/NGLife/")
    LoginAction.login(driver,username="sh0000002",password="Aa111111")
    time.sleep(5)
    dianZiTouBaoAction.add_dianzitoubao(driver,'漫漫','1321514','1990-03-04','100000','长生人寿长生人寿','110000','长生人寿','长生人寿长生人寿','110000','13113111111','100000','10000')

    time.sleep(5)
    driver.quit()



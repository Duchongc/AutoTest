import time
from selenium import webdriver
driver = webdriver.Chrome()
#登录
driver.get("http://tstmobile.gwcslife.com/NGLife/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(3)
driver.find_element_by_id("userCode").send_keys("sh0000002")  # 账号
driver.find_element_by_id("password").send_keys("Aa111111")   # 密码
driver.find_element_by_xpath('//*[@id="loginbtn"]').click()    # 点击登录
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element_by_id('RiskDegin').click()   #点击电子投保
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="addEform_1"]').click()  # 点击新增
time.sleep(5)
driver.find_element_by_xpath('//*[@id="confirmbtn"]').click()   # 点击确认事项
time.sleep(5)
driver.find_element_by_xpath('//*[@id="InsureName"]').send_keys("尼尼")  # 输入姓名
time.sleep(5)
drop_downn = driver.find_element_by_xpath('//*[@id="IDType"]')  # 点击证件类型
drop_downn.find_element_by_xpath('//*[@id="IDType"]/option[4]').click()  # 选择证件类型
#证件号码
driver.find_element_by_xpath('//*[@id="IDNo"]').send_keys("2323232323")  # 输入证件号码
driver.find_element_by_xpath('//*[@id="fm"]/fieldset/div[1]/div[8]/label').click()
time.sleep(10)
js = "document.getElementById('birthday').removeAttribute('disabled')"   # 使用js处理日期控件
driver.execute_script(js)
driver.find_element_by_id('birthday').send_keys('1990-08-24')  # 设置出生日期
time.sleep(2)
driver.find_element_by_xpath('//*[@id="InsureAge"]').click()
#婚姻状况
driver.find_element_by_xpath('//*[@id="Marriage"]')
driver.find_element_by_xpath('//*[@id="Marriage"]/option[3]').click()
#户籍所在地
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="HJSZD"]')
driver.find_element_by_xpath('//*[@id="HJSZD"]/option[2]').click()
#平均年收入
driver.find_element_by_xpath('//*[@id="YearSalary"]').send_keys("1000000")
#家庭地址
# 先定位到下拉菜单
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PROVNCD"]')
# 再对下拉菜单中的选项进行选择
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PROVNCD"]/option[10]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="CITYCD"]')
driver.find_element_by_xpath('//*[@id="CITYCD"]/option[2]').click()
driver.find_element_by_xpath('//*[@id="DSTRCTCD"]')
driver.find_element_by_xpath('//*[@id="DSTRCTCD"]/option[2]').click()
driver.find_element_by_xpath('//*[@id="HomeDetailAddr"]').send_keys('不知道不知道')
driver.find_element_by_id('HomeZipCode').send_keys('110000')
driver.find_element_by_id('GrpName').send_keys('不知道')
driver.find_element_by_id('GRPPROVNCD')
driver.find_element_by_xpath('//*[@id="GRPPROVNCD"]/option[10]').click()
driver.find_element_by_id('GRPCITYCD')
driver.find_element_by_xpath('//*[@id="GRPCITYCD"]/option[2]').click()
driver.find_element_by_id('GRPDSTRCTCD')
driver.find_element_by_xpath('//*[@id="GRPDSTRCTCD"]/option[2]').click()
driver.find_element_by_id('GrpDetailAddr').send_keys('不知道')
driver.find_element_by_id('GrpZipCode').send_keys('110000')
driver.find_element_by_id('HealthFlag')
driver.find_element_by_xpath('//*[@id="HealthFlag"]/option[2]').click()
time.sleep(5)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="detailWork"]').click()  # 点击职业  //*[@id="chooseOcc"]
time.sleep(1)
driver.find_element_by_xpath('//*[@id="A"]/div/div[1]').click()   # 职业一层
time.sleep(1)
driver.find_element_by_xpath('//*[@id="AA1"]/div/div[1]').click()  # 职业二层
time.sleep(1)
driver.find_element_by_xpath('//*[@id="A00"]/span').click()  # 职业三层
time.sleep(1)
driver.find_element_by_xpath('//*[@id="subSelect"]').click()  # 职业确定
time.sleep(1)
driver.find_element_by_xpath('//*[@id="Mobile"]').send_keys('13113113111')  # 联系方式
time.sleep(1)
driver.find_element_by_xpath('//*[@id="tabNav"]/ul/li[2]').click()   # 点击投保人
time.sleep(8)
driver.implicitly_wait(20)
driver.find_element_by_id('Appntrela').click()  # 选择关系
driver.find_element_by_xpath('//*[@id="Appntrela"]/option[2]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="tabNav"]/ul/li[3]').click()  # 点击受益人
time.sleep(10)
driver.find_element_by_xpath('//*[@id="digitalNav"]/ul/li[2]/div').click()  # 点击投保计划
time.sleep(8)
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="addRiskMain"]').click()   # 点击添加主险
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mainrisk2PC"]/div[1]/span').click()  # 选择险种
time.sleep(1)
driver.find_element_by_xpath('//*[@id="affirmMainRisk"]').click()   # 险种确认
time.sleep(3)
driver.find_element_by_id('PayIntv')   # 选择缴费方式
driver.find_element_by_xpath('//*[@id="PayIntv"]/option[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="Amnt"]').send_keys('100000')   # 输入保额
driver.find_element_by_xpath('//*[@id="Prem"]').click()   # 点击保费
time.sleep(3)
driver.find_element_by_id('sureAddBtn').click()  # 点击确定
time.sleep(3)
#
# saveSubRisks = driver.find_element_by_id('saveSubRisks') # 点击添加附加险
# ActionChains(driver).move_to_element(saveSubRisks).click().perform()
# jss = 'document.getElementByXpath("//*[@id="saveSubRisks"]").style.display="block";'
# driver.execute_script(jss)
# driver.find_element_by_xpath('//*[@id="saveSubRisks"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="SubRiskType"]/div[1]/span').click()  # 选择附加险
# driver.find_element_by_id('affirmSubRisk').click()  # 附加险确认
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="PayIntv"]')
# driver.find_element_by_xpath('//*[@id="PayIntv"]/option[2]').click()  # 附加险缴费方式
# driver.find_element_by_xpath('//*[@id="Amnt"]').send_keys('10000')  # 附加险保额
# driver.find_element_by_xpath('//*[@id="Prem"]').click()  # 附加险保费
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="sureAddBtn"]').click()  # 附加险确定
time.sleep(5)
driver.find_element_by_xpath('//*[@id="digitalNav"]/ul/li[3]/div').click() # 点击相关告知
time.sleep(5)
driver.implicitly_wait(30)
target = driver.find_element_by_xpath('//*[@id="allFalse_f"]')  # 一般告知 点击一键全否
driver.execute_script("arguments[0].scrollIntoView();",target)
target.click()
time.sleep(3)
'''//*[@id="global-alert-152402287256991-confirm"]'''
 # 一键全否确认
time.sleep(3)
# driver.find_element_by_xpath("//div[contains(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]")  这个需要结尾是‘btn-attention’
driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="finish_f"]').click()  # 点击完成
time.sleep(3)
driver.find_element_by_xpath('//*[@id="HEALTH_1_text_1_1"]').send_keys('175')   # 输入
driver.find_element_by_xpath('//*[@id="HEALTH_1_text_1_2"]').send_keys('70')    # 输入
a = driver.find_element_by_id('allFalse_h')
driver.execute_script("arguments[0].scrollIntoView();",a)
a.click()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()
time.sleep(5)
driver.find_element_by_id('finish_h').click()   # 点击完成
time.sleep(3)
c = driver.find_element_by_xpath('//*[@id="SALESMAN_2_text_1_1"]')  # 营销员告知
driver.execute_script("arguments[0].scrollIntoView();",c)
c.send_keys('五年')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='SerachResult_a']/tbody/tr[4]/td[2]/div[2]/div[1]").click() # 勾选
# driver.find_element_by_xpath("//*[@id='SerachResult_a']/tbody/tr[5]/td[2]/div[2]/div[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='SerachResult_a']/tbody/tr[5]/td[2]/div[2]/div[1]").click()  # 勾选
time.sleep(5)
driver.find_element_by_xpath('//*[@id="SALESMAN_7_text_6_1"]').send_keys('IT 保险')  # 职业学历
driver.find_element_by_xpath('//*[@id="SALESMAN_7_text_6_2"]').send_keys('IT 保险')  # 职业学历
time.sleep(3)
b = driver.find_element_by_id('allFalse_a')
driver.execute_script("arguments[0].scrollIntoView();",b)  # 一键全否
b.click()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()  # 一键全否确定
time.sleep(3)
driver.find_element_by_id('finish_a').click()  # 点击完成
time.sleep(6)
d = driver.find_element_by_xpath("//*[@id='SerachResult_s']/tbody/tr[8]/td[2]/div/div")  # 勾选同意协议 须知与声明
driver.execute_script("arguments[0].scrollIntoView();",d)
d.click()
# driver.find_element_by_xpath("//*[@id='SerachResult_s']/tbody/tr[8]/td[2]/div/div").click()  # 须知与声明
time.sleep(5)
driver.find_element_by_xpath('//*[@id="digitalNav"]/ul/li[4]/div').click()  # 点击转账授权
time.sleep(10)
e = driver.find_element_by_xpath('//*[@id="appICBCBanks"]/div[6]/div')
driver.execute_script("arguments[0].scrollIntoView();",e)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="insICBCBanks"]/div[3]/div/div').click()   # 点击招商银行
time.sleep(5)
accountPro= driver.find_element_by_xpath('//*[@id="accountPro"]')
accountPro.find_element_by_xpath('//*[@id="accountPro"]/option[10]').click()   # 账户所在地选择 （上海）
time.sleep(3)
driver.find_element_by_xpath('//*[@id="accountCity"]')
driver.find_element_by_xpath('//*[@id="accountCity"]/option[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="appAccountCode"]').send_keys('6226090214475432')   # 输入银行卡账号
time.sleep(3)
driver.find_element_by_xpath('//*[@id="tranAuth"]/div[3]/div[2]/button').click()  # 点击下一步
time.sleep(10)
driver.find_element_by_xpath('//*[@id="toubao1"]/a/div/a[2]/a/a/div/div').click() # 点击投保单预览
time.sleep(10)
# all_handles = driver.window_handles
# print(all_handles)
# driver.switch_to.window(all_handles[1])
# driver.close()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="toubao1"]/a/div/a[3]/div/div').click()  # 点击自动核保校验
# time.sleep(10)
# driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="toubao1"]/a/div/a[5]/a/div/div').click() # 点击拍照上传
# time.sleep(3)
# driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="toubao1"]/a/div/a[8]/a/div/div').click()  # 点击投保确认
# time.sleep(5)
# driver.find_element_by_xpath("//button[contains(@id,'-confirm')]").click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="toubao1"]/a/div/a[10]/a/div/div').click() # 点击缴费
time.sleep(20)
driver.quit()
from selenium import webdriver
from src.functions.LoginAction import LoginAction
import ddt, unittest, time
from config.logger import Log
from src.common.testDataMap import testDataMap

@ddt.ddt
class changsheng(unittest.TestCase):
    log = Log()
    log.info("长生项目登录测试开始")
    @classmethod
    def setUpClass(cls):
        cls.log.info("开始初始化浏览器.....")
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 静默执行，不打开浏览器
        option.add_argument('disable-infobars')  # 取消打开浏览器时候提示‘被自动化控制’等字体
        cls.driver = webdriver.Chrome()   # 实例化浏览器
        #cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)   # 隐式等待
#        cls.driver.get("http://tstmobile.gwcslife.com/NGLife/")

    def setUp(self):
        self.driver.get("http://tstmobile.gwcslife.com/NGLife/")
        time.sleep(3)
        self.driver.maximize_window()  # 最大化浏览器
        time.sleep(3)
    testdata = testDataMap()  # 实例化读取Excel数据操作
    @ddt.data(*testdata)
    def test_01(self,data):
        self.log.info('------正确的账号密码-------')
        self.log.info('输入账号密码,开始登录.........................................')
        LoginAction.login(self.driver, data['userName'], data['passWord'])  # 调用登录的方法
        self.assertEqual('长生销售支持系统', self.driver.title, '用例执行成功')  # Excel中的预期结果和页面信息作比较
        self.log.info('账号:%s,密码:%s' % (data['userName'], data['passWord']))
        self.log.info('登录操作结束..................................................')
        self.log.info('用例执行成功')
    def test_02(self):
        self.log.info('------错误的账号密码-------')
        self.log.info('输入账号密码,开始登录.........................................')
        LoginAction.login(self.driver, 'sh0000001', 'Aa111111')  # 调用登录的方法
        self.assertEqual('长生销售支持系统', self.driver.title)  # Excel中的预期结果和页面信息作比较
        self.log.info('账号:sh0000001,密码:Aa111111')
        self.log.info('登录操作结束..................................................')
        self.log.info('用例执行成功')
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

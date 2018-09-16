# -*- coding: utf-8 -*-
import HTMLTestRunner_cn
import unittest,time
from src.common.report_email import *
from src.common.email import *
if __name__ == '__main__':
    path = os.getcwd()
    test_report = path + '\\report\\'  # 获取报告地址
    run_path = path +'\\src\\runner\\'
    now = time.strftime('%Y%m%d_%H-%M-%S')  # 获取当前时间
    filename = path + '\\report\\' + now + '_result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    discover = unittest.defaultTestLoader.discover(run_path,pattern='test*.py')
    run = HTMLTestRunner_cn.HTMLTestRunner(title='测试报告',
                                        description='测试结果',
                                        stream=fp,
                                       )
    run.run(discover)
    fp.close()
    newReport = newReport()
    # sendReport(newReport)
    e = Email(title='长生测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='1978529954@qq.com',
              server='smtp.163.com',
              sender='m18625680375_1@163.com',
              password='DU962464',
              path=newReport,

    )
    e.send()
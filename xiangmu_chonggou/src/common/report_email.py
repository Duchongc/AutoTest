'''
对存放测试报告的html进行排序，发送最新的测试报告
'''
import os
def newReport():
    test_report = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    cur_path = os.path.join(test_report,'report')
    lists = os.listdir(os.path.join(test_report,'report'))  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(cur_path, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new
if __name__ == '__main__':
    newReport()


from src.common.readexcel import ExcelUtil
import os
def testDataMap():
    parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = parentDirPath+"\\testcase\\长生.xlsx"
    testdata = ExcelUtil(filepath, '长生登录账号').dict_data()
    return testdata

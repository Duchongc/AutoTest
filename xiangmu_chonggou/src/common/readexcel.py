# coding:utf-8
import xlrd
class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r



if __name__ == "__main__":
    filepath = "D:\\toors\\xiangmu\\testData\\长生.xlsx"
    sheetName = "长生登录账号"
    data = ExcelUtil(filepath, sheetName)
    for a in data.dict_data():
        print(a)
        print(a['implement'])
        if a['implement'] == 'Y':
            print('执行测试用例')
        elif a['implement'] == 'N':
            print('不执行测试用例')
        else:
            pass
    # print(data.dict_data())
    # print(data.dict_data()[0]['implement'])
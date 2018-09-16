# -*- coding: utf-8 -*-
from src.common.ParseConfigurationFile import ParseCofigFile
def read_ini():
    aa = []
    pc = ParseCofigFile()
    login = pc.getItemsSection("changsheng_login")
    login_key = login.keys()
    list_login_key = list(login_key)
    for a in list_login_key:
        aa.append(a)

    return aa

if __name__ == '__main__':
    read_ini()
from selenium.webdriver.support.ui import WebDriverWait
def getElement(driver, locateType, locatorExperession):
    '''
    :param driver:  实例化浏览器
    :param locateType:   元素定位类型
    :param locatorExperession:    对应的元素
    :return:
    '''
    try:
        element = WebDriverWait(driver, 40).until(lambda x: x.find_element(by=locateType, value=locatorExperession))
        return element
    except Exception as e:
        raise e

def getElements(driver, locateType, locatorExperession):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType, value=locatorExperession))
        return elements
    except Exception as e:
        raise e

def js_execute(driver,js):
    '''执行js'''
    try:
        return driver.execute_script(js)
    except Exception as e:
        raise e

def js_focus_element(driver, locateType,locatorExperession):
    '''聚焦元素'''
    target = getElement(driver,locateType,locatorExperession)
    driver.execute_script("arguments[0].scrollIntoView();", target)

def js_scroll_top(driver):
    '''滚动到顶部'''
    js = "window.scrollTo(0,0)"
    driver.execute_script(js)

def js_scroll_end(driver):
    '''滚动到底部'''
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,"id","kw")
    print (searchBox.tag_name)
    aList = getElements(driver,"tag name","a")
    print (len(aList))
    driver.quit()



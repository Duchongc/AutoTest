from selenium import webdriver

def context_click(driver, element):
    '''点击鼠标右键操作'''
    try:
        context_click = webdriver.ActionChains(driver).context_click(element).perform()
    except Exception as e:
        print('context_click error:%s' % e)
    else:
        return context_click
def double_click(driver, element):
    '''双击鼠标操作'''
    try:
        double_click = webdriver.ActionChains(driver).double_click(element).perform()
    except Exception as e:
        print('double_click error:%s' % e)
    else:
        return double_click
def drag_and_drop(driver, x, y):
    '''拖动鼠标操作'''
    try:
        drag_and_drop = webdriver.ActionChains(driver).drag_and_drop(x, y).perform()
    except Exception as e:
        print('drag_and_drop error:%s' % e)
    else:
        return drag_and_drop
def move_to_element(driver, element):
    '''鼠标悬停操作'''
    try:
        move_to_element = webdriver.ActionChains(driver).move_to_element(element).perform()
    except Exception as e:
        print('move_to_element error:%s' % e)
    else:
        return move_to_element
def left_click(driver, element):
    '''鼠标左键操作'''
    try:
        left_click = webdriver.ActionChains(driver).click(element).perform()
    except Exception as e:
        print('left_click error:%s' % e)
    else:
        return left_click


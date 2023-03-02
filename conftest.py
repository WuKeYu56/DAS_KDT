import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(5)
    # login(driver)
    def end():
        driver.quit()
    request.addfinalizer(end)#终结函数
    #这里为什么不用yield呢因为yield不能return，addfinalizer这个功能可以实现饿yield功能一样
    #而且可以return参数传给后面的用例
    return driver
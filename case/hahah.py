# from common.parseXLS import Parse
#
# def runner():
#     p = Parse("../testdata/case1.xls")
#     p.get_sheet("Sheet1")
#     tcs = p.prepare_tc()
#     print(tcs[0].steps)
#
# def haha():
#     a = 'xpath=//input[@class="naksiamak"]'
#     b = a.split("=", 1)
#     print(tuple(b))
#
# if __name__ == '__main__':
#     haha()

from selenium import webdriver

d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(5)
d.get("http://11.0.0.167:9103/")
d.find_element("xpath", '/html/body/div[1]/div[2]/button').click()
d.find_element("xpath", "/html/body/div[2]/section/div[1]/div/form/div[1]/input").send_keys("gm_admin")
d.find_element("xpath", "/html/body/div[2]/section/div[1]/div/form/div[2]/input").send_keys("qwe123123")
d.find_element("xpath", '/html/body/div[2]/section/div[1]/div/form/div[3]/button').click()

text = d.find_element('id', 'userDropdown').text
print(text)
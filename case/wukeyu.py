import time

from selenium import webdriver

from common.base import Base
from pages.loginpage import login

d = webdriver.Chrome()
login(d)
das = Base(d)
das.open("http://11.0.0.167:9103/v2/dataprocessed/mercatorImageAnalysis.html?siteId=100024&projId=100028")


time.sleep(5)
d.close()
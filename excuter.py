import os

command1 = "pytest ./case/test_login.py --alluredir ./report/result"
command2 = "allure generate ./report/result -o ./report/html --clean"

a = os.system(command1)
print(a)
b = os.system(command2)
print(b)


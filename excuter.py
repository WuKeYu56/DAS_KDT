import os


command1 = "pytest ./case/ --alluredir ./report/result"
command2 = "allure generate ./report/result -o ./report/html --clean"

# os.system('rmdir ./report/result')
os.system(command1)
os.system(command2)


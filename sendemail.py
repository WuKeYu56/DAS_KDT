import os
import smtplib
import zipfile
from email.header import Header
from email.mime.text import MIMEText

#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
    #开始创建压缩包
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, _, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)     #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()



host = 'smtp.126.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式

#发送邮箱
sender = '***@126.com'

#接收邮箱
receiver = '***@qq.com'

#发送邮件主题
subject = 'Python email test'

#发送邮箱服务器
smtpserver = 'smtp.126.com'

username = 'wukeyu56@168.com'  #发送邮箱用户
password = '**************'                #邮箱密码或授权码

#编写 text 类型的邮件正文
#msg = MIMEText('<html><h1>比你更忙的人都在学习！</h1></html>','html','utf-8')
msg = MIMEText('比你更忙的人都在学习！111','plain','utf-8')

msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receiver

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com',25)
smtp.login(username, password)  # 登陆邮箱
smtp.sendmail(msg['From'], msg['To'], msg.as_string())  # 发送邮件！
print("邮件发送成功!")


if __name__ == '__main__':
    soucedir = "./report/html"
    outoutfile = './report/html.zip'
    make_zip(soucedir, outoutfile)
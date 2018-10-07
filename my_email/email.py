import smtplib
from email.mime.text import MIMEText


class Emailer:
    def __init__(self, user, password, host):
        # 邮箱用户名
        self.user = user
        # 邮箱授权码
        self.password = password
        # 163的SMTP服务器
        self.host = host

    def send_email(self, sender, receiver, content, title):
        # 第一部分：准备工作
        # 1.将邮件信息打包成一个对象,内容，格式，编码
        message = MIMEText(content, "plain", "utf-8")
        # 2.设置邮件的发送者
        message["From"] = sender
        # 3.设置邮件的接收方
        message["To"] = ",".join(receiver)
        # 4.设置邮件的标题
        message["Subject"] = title

        # 第二部分：发送邮件
        try:
            # 1.启动SSL发送邮件,参数:SMTP服务器,端口号(一般用465)
            smtpObj = smtplib.SMTP(self.host, 25)
            # 2.登录邮箱并发送验证,参数:邮箱用户名，授权码
            smtpObj.login(self.user, self.password)
            # 3.发送邮件,参数：发送方邮箱，接收方邮箱，邮箱的正文
            smtpObj.sendmail(sender, receiver, message.as_string())

            print("mail has been send successful!")
        except BaseException as e:
            print(e)


mail_user = "15071296340@163.com"
mail_pwd = "p19950330"

sender = "15071296340@163.com"
receiver = ["591006214@qq.com"]

content = '我是你飘哥'  # 邮件的正文
title = "飘哥"  # 邮件的标题

my_email = Emailer(mail_user, mail_pwd, "smtp.163.com")
my_email.send_email(sender, receiver, content, title)

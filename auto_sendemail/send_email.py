import smtplib
from email.mime.text import MIMEText
from email.header import Header

SENDER = "朋友"
SEND_EMAIL = '1458010081@qq.com'
RECEIVER = "郑帅"
RECEIVER_EMAIL = ['18309169600@163.com']
ACTIVE_CODE = ""
SUBJECT = '来自异世界的一封信！'
CONNECT_EMAIL = "smtp.qq.com"


class SendEmail:
    def __init__(self, content):
        self.sender = SENDER
        self.sender_email = SEND_EMAIL
        self.active_code = ACTIVE_CODE
        self.receiver = RECEIVER
        self.receive_email = RECEIVER_EMAIL
        self.subject = SUBJECT
        self.connect_email = CONNECT_EMAIL
        self.content = content

    def send_email(self):
        message = MIMEText(self.content, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = Header(self.receiver, 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        try:
            mail = smtplib.SMTP()
            mail.connect(self.connect_email)
            mail.login(self.sender_email, self.active_code)
            mail.sendmail(self.sender_email, self.receive_email, message.as_string())
            mail.quit()
            return "邮件发送成功"
        except Exception as e:
            return 'Error:无法发送邮箱' + str(e)


if __name__ == '__main__':
    text = "你好，我是帅到爆炸"
    s = SendEmail(content=text)
    print(s.send_email())

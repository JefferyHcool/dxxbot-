import email
# smtplib 用于邮件的发信动作
import smtplib
import connectDB
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
from email.mime.multipart import MIMEMultipart
from  email.mime.image import MIMEImage
from  email.mime.text import MIMEText

class sendEmail():
    def __init__(self):
        pass
    def send(self):
        # 用于构建邮件头
        to_addr = []
        db=connectDB.ConnectDB()
        add=db.read()
        for i in add:
            print(i["QQ_email"])
            to_addr.append(str(i["QQ_email"])+"@qq.com")
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        sender = '211354509@qq.com'
        password = 'aaltwyzzjenkbhhg'

        # 收信方邮箱

        # '2959930146@qq.com',"2583176593@qq.com"

        # 发信服务器

        subject = "最新青年大学习截图"

        # 邮件头信息
        with open("date.txt") as f:
            n=f.read()
        em = MIMEMultipart()
        em['Subject'] = subject
        em['From'] = sender
        em['To'] = ','.join(to_addr)

        content = MIMEText(
            "<h1>青年大学习截图<h1><img src='cid:dxx' alt=""> <h2>大学习答题界面进入可以直接答题<h2> <p>https://dxx.wwwtop.top/dxx_video?a=12&b={}&t=1&z=200&c=1</p>".format(n),
            _subtype='HTML')
        em.attach(content)
        img = MIMEImage(open('dxxend.png', 'rb').read())
        img.add_header("Content-ID", 'dxx')
        em.attach(img)
        smtpserver="smtp.qq.com"
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        smtp.connect("smtp.qq.com")
        smtp.helo()
        smtp.ehlo()
        smtp.login(sender, password)


        smtp.send_message(em)
        smtp.close()
        print("青年大学习发送完毕")
    def testsend(self,qq):
        # 用于构建邮件头
        QQ_Email=qq
        if "@qq.com" in str(qq):
            
            to_addr = [QQ_Email,]
        else:
            QQ_Email=str(qq)+"@qq.com"
            to_addr = [QQ_Email,]
     
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        sender = '211354509@qq.com'
        password = 'aaltwyzzjenkbhhg'

        # 收信方邮箱

        # '2959930146@qq.com',"2583176593@qq.com"

        # 发信服务器

        subject = "最新青年大学习截图"

        # 邮件头信息
        with open("date.txt") as f:
            n=f.read()
        em = MIMEMultipart()
        em['Subject'] = subject
        em['From'] = sender
        em['To'] = ','.join(to_addr)

        content = MIMEText(
            "<h1>青年大学习截图<h1><img src='cid:dxx' alt=""> <h2>大学习答题界面进入可以直接答题<h2> <p>https://dxx.wwwtop.top/dxx_video?a=12&b={}&t=1&z=200&c=1</p>".format(n),
            _subtype='HTML')
        em.attach(content)
        img = MIMEImage(open('dxxend.png', 'rb').read())
        img.add_header("Content-ID", 'dxx')
        em.attach(img)
        smtpserver="smtp.qq.com"
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        smtp.connect("smtp.qq.com")
        smtp.helo()
        smtp.ehlo()
        smtp.login(sender, password)


        smtp.send_message(em)
        smtp.close()
        print("青年大学习发送完毕")

    def setSend(self,addr,subject,contents):
        print(addr)
        if "@qq.com" not in str(addr):
            addr=str(addr)+"@qq.com"

        # 用于构建邮件头

        if addr=="all":
            to_addr = []
            db = connectDB.ConnectDB()
            add = db.read()
            for i in add:
                
                to_addr.append(str(i["QQ_email"]) + "@qq.com")
            print(to_addr)
        else:
            to_addr = []
            to_addr.append(addr)

        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        sender = '211354509@qq.com'
        password = 'aaltwyzzjenkbhhg'

        # 收信方邮箱

        # '2959930146@qq.com',"2583176593@qq.com"

        # 发信服务器

        subject = subject

        # 邮件头信息

        em = MIMEMultipart()
        em['Subject'] = subject
        em['From'] = sender
        em['To'] = ','.join(to_addr)

        content = MIMEText(contents)
        em.attach(content)
        # img = MIMEImage(open('dxxend.png', 'rb').read())
        # img.add_header("Content-ID", 'dxx')
        # em.attach(img)
        smtpserver = "smtp.qq.com"
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.connect("smtp.qq.com")
        smtp.helo()
        smtp.ehlo()
        smtp.login(sender, password)

        smtp.send_message(em)
        smtp.close()
        print("{:+^15}\n发送标题：{}\n发送内容：{}\n发送给：{}".format("发送完毕",subject, contents,addr))
        
if __name__ == '__main__':
    sd=sendEmail()
    sd.send()
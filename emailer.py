# coding: utf-8

# by wangweicheng

'''
    Python SMTP 发送带附件电子邮件
    Author: weicheng wang
    Note:   Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email import utils

class EMailer(object):
    '''邮件操作类
    '''
    def __init__(self, addresses):
        self.address = 'wangweicheng@xxx.com' # 发送的邮箱地址
        auth_info = {}
        auth_info['server'] = 'mail.xxx.com'  # 邮箱服务器
        auth_info['user'] = self.address
        auth_info['password'] = 'xxxxxx' # 邮箱密码
        self.user_info = auth_info
        self.contacts = addresses # 接受邮件的邮箱
        print self.contacts
    
    def send_mail(self, subject, content):
        '''发送邮件私有方法
        '''
        str_to = '; '.join(self.contacts)

        server = self.user_info.get('server')
        smtp_port = 25  # smtp_port 端口
        user = self.user_info.get('user')
        passwd = self.user_info.get('password')

        if not (server and user and passwd):
            print 'incomplete login info, exit now'
            return

        # 设定root信息
        msg_root = MIMEMultipart('related')
        msg_root['Subject'] = subject
        msg_root['From'] = '%s<%s>' % (Header(subject, 'utf-8'), self.address)
        msg_root['To'] = str_to

        msg_alternative = MIMEMultipart('alternative')
        msg_root.attach(msg_alternative)

        # 构造MIMEMultipart对象做为根容器
        main_msg = MIMEMultipart()

        html_msg = MIMEText(
            '<p style="font-size:20px"> 测试邮件 </p>\
            <div>'+ content + '</div>\
            <p style="font-size:14px">* 请勿直接回复此邮件</p>',
            'html',
            'utf-8'
        )

        main_msg.attach(html_msg)
        # 设置根容器属性
        main_msg['From'] = '%s<%s>' % (Header('Python 研发组', 'utf-8'), 'developer@python.com')   # 如果你想隐藏发送邮件邮箱，此处可以伪装
        main_msg['To'] = str_to     # 显示收件人地址
        main_msg['Subject'] = subject
        main_msg['Date'] = utils.formatdate()

        # 得到格式化后的完整文本
        full_text = main_msg.as_string()

        try:
            #发送邮件
            smtp = smtplib.SMTP(server, smtp_port)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(user, passwd)
            smtp.sendmail(self.address, self.contacts, full_text)
            smtp.quit()
            print "邮件发送成功!"
        except Exception, e:
            print "失败：" + str(e)
            

if __name__ == "__main__":
    EMailer(['809405366@qq.com']).send_mail("Python 邮件测试", "这是一封Python自动发送的邮件")

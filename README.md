# python-emailer

Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件

### 配置

```
def __init__(self, addresses):
        self.address = 'wangweicheng@xxx.com' # 发送的邮箱地址
        auth_info['server'] = 'mail.xxx.com'  # 邮箱服务器
        auth_info['password'] = 'xxxxxx' # 邮箱密码

```

### 使用

```
// 发送的邮箱数组，邮件标题，邮件内容
EMailer(['80990366@qq.com']).send_mail("Python 邮件测试", "这是一封Python自动发送的邮件")

```

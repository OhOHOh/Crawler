import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

# 参考了 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000#0

# msg = MIMEText('hello, send by python... FROM 余润身的lab computer', 'plain', 'utf-8')

#     # 输入Email地址和口令:
# from_addr = input('From: ')      # 510350980@qq.com
# password = input('Password: ')   # QQ授权码：hxlvrpbeuugzbjjg
#     # 输入收件人地址:
# to_addr = input('To: ')          # 1075243138@qq.com
#     # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')    # smtp.qq.com

# # server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
# server.login(from_addr, password=password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "510350980@qq.com"
password = "hxlvrpbeuugzbjjg"
to_addr = "1075243138@qq.com"
smtp_server = "smtp.qq.com"

# msg = MIMEText(
#     "<html><body><h1>Hello</h1>" + "<p>this is <a href='http://www.baidu.com'>Baidu</a>...</p></body></html>",
#     'html',
#     'utf-8'
# )

# 尝试往其中添加附件
msg = MIMEMultipart()  # 新建了一个邮件对象！！！ 其中可以包括之前的 MIMEText, 还可以包括 MIMEBase(就是附件)
msg['From'] = _format_addr('余润身 <%s>' % from_addr)
msg['To'] = _format_addr('张静芳 <%s>' % to_addr)
msg['Subject'] = Header("尝试发送html文本，可以包含链接", 'utf-8').encode()

# 邮件正文是 MIMEText
msg.attach(MIMEText("send with file !!!", 'plain', 'utf-8'))
# 附上附件, 就是 MIMEBase
with open('./logo.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='logo.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='logo.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment', '0')
    # 把邮件的附加内容读进来
    mime.set_payload(f.read())
    # 用 Base64 来编码
    encoders.encode_base64(mime)
    # 最后添加到 msg 中
    msg.attach(mime)

# 若想要在邮件正文中加入图片, 而不是在附件中 !
msg.attach(MIMEText(
    "<html><body><h3>with photo</h3><p><img src='cid:0'></p></body></html>",
    'html',
    'utf-8'
))

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
import datetime

my_sender = '24xxxx28@qq.com'  # 发件人邮箱账号
my_receiver = ['24xxxx28@qq.com','26x23@qq.com']# 收件人邮箱账号，可以发送给自己
my_pwd = '授权码'  #如果拿自己的qq邮箱发送，qq邮箱需要打开smtp服务，获得授权码

def send_mail():
    ret = True
    try:
        today_date = datetime.date.today()

        msg = MIMEText('这是一封测试邮件' + '\n' + '此处填写邮件正文内容'+ '\n'*5 +'Less is more', 'plain', 'utf-8') # 此处可以使  html,plain格式
        msg['From'] =  my_sender   #  括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = ";".join(my_receiver)  # 多个收件人,注意用分号
        #msg['To'] = my_receiver   若为单个收件人，注意将 my_receiver = ['24xxxx28@qq.com'] 改为 my_receiver = '24xxxx28@qq.com'
        msg['Subject'] = "Hi,辛,早上好.发布任务---今天是%s" % (today_date)  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pwd)  # 括号中对应的是发件人邮箱账号、邮箱SMTP服务器授权码
        server.sendmail(my_sender, my_receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件内容
        server.quit()  # 关闭连接
        # 注意：
        # MIMEText()["to"]的数据类型为str类型,多个地址使用逗号分隔
        # sendmail(from_addrs, to_addrs, ...)的to_addrs为list类型。
        print("邮件发送success")
    except Exception :  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

if __name__ == '__main__':
    ret = send_mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

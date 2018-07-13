import smtplib
from email.mime.text import MIMEText
import datetime


def send_mail(content):
    my_sender = '2228@qq.com'  # 发件人邮箱账号
    my_receiver = '22203@qq.com'# 收件人邮箱账号，可以发送给自己
    my_pwd = '授权码'  #如果拿自己的qq邮箱发送，qq邮箱需要打开smtp服务，获得授权码
    today_date = datetime.date.today()

    msg = MIMEText(content, 'html', 'utf-8') # 此处可以使  html,plain格式
    msg['From'] =  my_sender   #  括号里的对应发件人邮箱昵称、发件人邮箱账号
    #msg['To'] = ";".join(my_receiver)  # 多个收件人,注意用分号
    msg['To'] = my_receiver
    msg['Subject'] = "Hi,早上好.发布任务---今天是%s" % (today_date)  # 邮件的主题

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
    server.login(my_sender, my_pwd)  # 括号中对应的是发件人邮箱账号、邮箱SMTP服务器授权码
    server.sendmail(my_sender, my_receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件内
    server.quit()  # 关闭连接

def table():
    # border_color_one = '00FF33'
    # border_color_two = 'FF33CC'
    # bgcolor_one = 'FFFF66'
    # bgcolor_two = '99FFCC'

    table_connect = """
    <!DOCTYPE <!DOCTYPE html>
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.baidu.com">有问题找百度</a></p>
    <p align="center">学习任务表</p>
    <table border="2px" bordercolor = 'pink'  align="center" width="600px" height="300px">
        <tr align="center">
            <td >项目</td>
            <td colspan="5" bgcolor = '00ff00' >上班学习</td>
            <td colspan="2" bgcolor = 'ccff33' >宿舍窝着</td>
        </tr>
    
        <tr align="center">
            <td>星期</td>
            <td bgcolor = 'yellow' >Monday</td>
            <td bgcolor = 'yellow' >Tuesday</td>
            <td bgcolor = 'yellow' >Wednesday</td>
            <td bgcolor = 'yellow' >Thursday</td>
            <td bgcolor = 'yellow' >Friday</td>
            <td bgcolor = 'ccff33' >Saturday</td>
            <td bgcolor = 'ccff33' >Sunday</td>
        </tr>
    
        <tr align="center">
            <td rowspan="4" bgcolor='ff6666'>morning</td>
            <td bgcolor = 'd2691e' >python</td>
            <td>machine</td>
            <td>learning</td>
            <td bgcolor = 'd2691e' >python</td>
            <td bgcolor = 'd2691e' >python</td>
            <td>openstack</td>
            <td rowspan="4">休息</td>
        </tr>
        
        <tr align="center">
            <td>math</td>
            <td>数学</td>
            <td bgcolor = 'd2691e' >python</td>
            <td bgcolor = 'd2691e' >python</td>
            <td>化学</td>
            <td>计算机</td>
        </tr>
        
        <tr align="center">
            <td bgcolor = 'd2691e' >python</td>
            <td>英语</td>
            <td>体育</td>
            <td bgcolor = 'd2691e' >python</td>
            <td bgcolor = 'd2691e' >python</td>
            <td>cloud</td>
        </tr>  
    
        <tr align="center">
            <td>数学</td>
            <td>数学</td>
            <td>地理</td>
            <td>历史</td>
            <td>化学</td>
            <td>计算机</td>
        </tr>
    </table>
    """
    return table_connect      #若没有return 报错 TypeError: write() argument must be str, not None


if __name__ == '__main__':
    # 显示table,生成html文件，可用浏览器打开，用于测试
    # table = table()
    # fp_write = open('table_show.html', 'w')  # 若是'wb'就表示写二进制文件
    # fp_write.write(table)
    # fp_write.close()
    table = table()
    send_mail(table)
    print('success sended')
          

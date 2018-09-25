## 豆瓣模拟登录/顶帖  顶帖未成功

import requests
from bs4 import BeautifulSoup
from PIL import Image
import re
import time


# 手动输入验证码
def pre_login():
    url = 'https://accounts.douban.com/login'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    captcha_id = soup.find('input', {'name':'captcha-id'})['value']
    image_url = 'https://www.douban.com/misc/captcha?id={}&size=s'.format(captcha_id)
    with open('code.jpg', 'wb') as f:
        f.write(requests.get(image_url).content) # ??
    image = Image.open('code.jpg')
    image.show()
    return input('请输入验证码'), captcha_id


def login(captcha, captcha_id):
    account = '2xxxxxqq.com'
    password = 'xxxxx6'
    # 审查元素-->Network-->login-->Form Data
    data = {
        'source': 'index_nav',
        'redir': 'https://www.douban.com/',
        'form_email': account,        # 账号
        'form_password': password,    # 密码
        'captcha-solution': captcha,    # input('请输入验证码') 中输入的验证码
        'captcha-id': captcha_id,
        'login': '登录'
    }
    url = 'https://accounts.douban.com/login'

    # r = requests.post(url, data=data)
    # print(r.text) 验证一下 登录成功
    # print('mimo' in r.text)   验证一下 账号在页面中 登录成功

    # 302 请求 不允许跳转，跳转后看不到cookie
    r = requests.post(url, data=data, allow_redirects=False)
    return r.headers


def set_cookie(headers, cookies):
    print(headers['Set-cookie'])
    for raw_cookie in headers['Set-Cookie'].split(','):
        # print(raw_cookie.strip())
        # ue="2438529228@qq.com"; domain=.douban.com; expires=Wed
        # 25-Sep-2019 07:49:20 GMT; httponly
        # dbcl2="185003410:Fu23NkM9cEU"; path=/; domain=.douban.com; httponly
        # as="deleted"; max-age=0; domain=.douban.com; expires=Thu
        # 01-Jan-1970 00:00:00 GMT
        # bid=OfFlQAjUaIU; Expires=Wed
        # 25-Sep-19 07:49:20 GMT; Domain=.douban.com; Path=/

        # 找 as="deleted"; 这样的
        content = re.findall('([\d\w]+)=(.+?);', raw_cookie.strip())
        # print(content)
        if content:
            key, value = content[0]
            if key.lower() == 'ue':
                continue
            if key.lower() == 'dbcl2':
                continue
            if key.lower() == 'as':
                continue
            if key.lower() == 'domain':
                continue
            cookies[key] = value
    #print(cookies)  # 关键是找到bid项
    return cookies


def comment(cookies, content):
    url = 'https://www.douban.com/group/topic/124839268/add_comment'  # 去某一个帖子下边评论，帖子网址
    # strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
    # strftime（）函数将时间格式化为我们想要的格式
    # time.strftime('%Y-%m-%d %H:%M:%S', (2008,2,3,12,12,12,1,1,1))
    # time.time  --->(12345678.111))
    # time.localtime(12345678.111))   --->(2008,2,3,12,12,12,1,1,1)
    data = {
        'ck':'fOOD',
        # 评论顶帖内容
        'rv_comment':time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        'start':'0',
        'submit_btn':'发送',
        'img': '(binary)',
    }
    r = requests.post(url, data=data, cookies=cookies, allow_redirects=False)
    print(r.status_code)
    print('1')
    #print(r.text)
    print('2')
    #print(r.headers)

captcha, captcha_id = pre_login()
headers = login(captcha, captcha_id)
cookies = set_cookie(headers, {})
while True:
    content = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    comment(cookies, content)
    print(content + ' 顶帖成功! ')
    time.sleep(3)

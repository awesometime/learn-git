import requests
import http.cookiejar as cookielib
import re
import urllib3
import time
from PIL import Image
# import pprint

"""
登录流程 :xsrf验证  验证码(需要timestamp)    不知道为啥没用signature hmac 也能登录
TODO   新版知乎  xsrf  不知道在哪里获取      此代码注释掉get_xsrf()也可以登录成功
运行zhihu_login("xxx", "xxx") 之后会生成captcha.jpg /cookies.txt 并不是开始就有cookies.txt
"""



#  关闭SSL认证verify=False会有警告，  禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 第一次运行cookie未能加载，登录成功之后将cookie保存，不会打印cookie未能加载了  以便之后使用
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print ("cookie未能加载")

# headers
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': agent
}


def is_login():
    #通过个人中心某个页面(只有自己的页面才有，比如自己提的问题)返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/question/298757342"
    response = session.get(inbox_url, headers=header, allow_redirects=False, verify=False)
    if response.status_code != 200:
        return False
    else:
        print("已经登录...")
        return True


def get_xsrf():
    #获取xsrf code
    response = session.get("https://www.zhihu.com", headers=header, verify=False)
    print(response.content)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        print(match_obj.group(1))
        return (match_obj.group(1))
    else:
        return ""


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print ("ok")


def get_captcha():   
    t = str(int(time.time()*1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, headers=header, verify=False)
    with open("captcha.jpg","wb") as f:
        f.write(t.content)
        f.close()

    # 自动打开验证码图片
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass

    captcha = input("输入验证码\n>")
    return captcha


def zhihu_login(account, password):
    #知乎登录
    post_url = "https://www.zhihu.com/signup?next=%2F"
    post_data = {
        "_xsrf": get_xsrf(),
        "username": account,
        "password": password,
        "captcha":get_captcha()
    }
    response_text = session.post(post_url, data=post_data, headers=header, verify=False)
    print(response_text)
    print(response_text.content.decode("utf-8"))

    # 登录以后保存cookies 以便之后使用
    session.cookies.save()


zhihu_login("xxx", "xxx")
# get_index()  下载index_page
is_login()   # 判断是否登录成功

# get_captcha()

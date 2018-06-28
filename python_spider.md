## 爬虫一步步进阶

`爬虫方法`

- urllib  加密不好使

- Selenium+Chromedriver 加密的也可以

- Scrapy

`筛选所需内容方法`

- find

- 正则表达式

- BeautifulSoup lxml 


转载自[Python 爬虫煎蛋网 OOXX 妹子图爬虫（1）——解密图片地址](http://www.tendcode.com/article/jiandan-meizi-spider/)

里面有将加密结果，分析加密源代码，分析如何解密，值得看看。

#### 一  利用`urllib.request.Request`和`urllib.request.urlopen`

缺点：

A. urllib抓取网页很容易被当作爬虫来对待，url中加header和使用代理地址和设置time.sleep可以实现一些伪装.

B.不能获取js执行(加密)后的网页内容

煎蛋网对图片进行了加密因此此方法没有成功。

代码未使用正则表达式。

```
import urllib.request
import os
import random
import time


def url_open(url):
    req = urllib.request.Request(url)
    
    # 加header和使用代理地址可以实现伪装
    # 加header
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    # 使用代理地址    
    # proxylist = ['111.192.44.204:9000', '222.82.222.242:9999', '124.202.247.110:8080']
    # proxy = random.choice(proxylist)
    # proxyhandler = urllib.request.ProxyHandler({'htttp': proxy})
    # opener = urllib.request.build_opener(proxyhandler)
    # urllib.request.install_opener(opener)
    # request模块中建立opener

    response = urllib.request.urlopen(url)
    html = response.read()
    return html                       # 记得返回，否则该函数就没有返回值


# 1:确定当前要下载的图片的页码，即47等数字，以便后续获取其所在页面的 完整url
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    # print(html[a:b])
    return html[a:b]                   # 记得返回


# 2：根据 完整url 确定图片的服务器地址
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    # print(html)  此处打印的是加密后的html文件，所以会找不到想要的图片。
    
    img_addrs = []
    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg', a, a + 255)             # 从a位置开始查找.jpg，直到a+255位置，一个网址不会超过255位。
        if b != -1:                                   # 若找到b       
            img_addrs.append(html[a + 9:b + 4])       # 找到后将图片url传入img_addrs列表
            # print(img_addrs)
        else:                                         # 若找不到b
            b = a + 9                                 # 将b重置为a+9的位置
        a = html.find('img src=', b)                # 重新开始查找
    return img_addr       
    # 测试用
    # for each in img_addrs:
    #    print(each)


# 3：根据服务器地址进行下载保存
def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]        # 此处应该用each而不是img_addrs   [-1]表示/分割后取最后一组内容，保存为图片名
        with open('filename', 'wb') as f:
            img = url_open(each)
            f.write(img)                      # 将img写入路径下，命名为filename
    
    
def download_pic(folder='G:\\img', pages=5):            # 爬取5页里的所有图片
    # 创建文件夹
    os.mkdir(folder)
    # 切换到文件夹
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    # 1:确定当前要下载的图片的页码，即47等数字，以便后续获取其所在页面的 完整url
    page_num = int(get_page(url))
    
    for i in range(pages):
        page_num -= i
        # http://jandan.net/ooxx/page-47#comments
        page_url = url + 'page-' + str(page_num) + '#comments'
        # print(page_url)
        
        # 2：根据 完整url 确定图片的服务器地址
        img_addrs = find_imgs(page_url)

        # 3：根据服务器地址进行下载保存
        save_imgs(folder, img_addrs)
        time.sleep(3)

if __name__ == '__main__':  # 注意 = 和 == 区别  ，作为导入模块时不执行，只在自己内部执行    
    download_pic()
```

#### 二  `Selenium+Chromedriver`可以实现对js加密后的网页的爬取

- [Selenium使用详解](https://www.jianshu.com/p/4b89c92ff9b4)

- `Selenium+PhantomJS`UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions 

of Chrome or Firefox instead

Selenium不再支持PhantomJS(无界面浏览器)

- 选择Selenium+Chromedriver(前提要有chrome，两exe文件放在同一文件夹下)

- 使用了`BeautifulSoup`方法，BeautifulSoup是一个模块，该模块用于接收一个HTML或XML字符串，然后将其进行格式化，

之后便可以使用他提供的方法进行快速查找指定元素，从而使得在HTML或XML中查找指定元素变得简单。

- [BeautifulSoup基本用法总结](https://blog.csdn.net/kikaylee/article/details/56841789)

-待解决的问题：无界面，不用打开浏览器

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup


path='G:/img/'        # 图片保存路径
urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(48, 50)]
img_url=[]

# headless 无界面模式（不会用）
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=option)


# 调用环境变量指定的chrome浏览器创建浏览器对象  此处指定chromedriver.exe的路径
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

for url in urls:
    # 打开url网页
    driver.get(url)
    # url网页渲染后的源代码返回给data
    data = driver.page_source
                                                   # BeautifulSoup 需要学习
    bs = BeautifulSoup(data, "html.parser")      # 此处lxml不行，应该是未安装的原因
    images = bs.select("a.view_img_link")
    
    for i in images:
        z=i.get('href')
        if str('gif') in str(z):
           pass
        else:
            http_url = "http:" + z
            img_url.append(http_url)
            #print("http:%s" % z)
    
    for j in img_url:
        r=requests.get(j)
        print('正在下载 %s......' % j)
        with open(path+j[-15:],'wb')as jpg:
            jpg.write(r.content)
```

#### 三         用Python爬虫抓取免费代理IP

- [用Python爬虫抓取免费代理IP](https://mp.weixin.qq.com/s/bhf1CrWzY-btSJpwEMth3g)

```
本代码爬取到了'http://www.youdaili.net/Daili/http/36822.html'中显示的ip，但没有端口（正则表达式不会写）
import requests
import re
from bs4 import BeautifulSoup


def crawl_xici_ip():
    ip_list = []
    url = 'http://www.youdaili.net/Daili/http/36822.html'
    response = requests.get(url)
    # print(response.status_code)
    if response.status_code == 200:
        content = response.text
        # print('0')
        # print(content)
        soup = BeautifulSoup(content, 'html.parser')
        # print('1')
        # print(soup)
    # print('2')
    divs = soup.find_all('div')
    # print(divs)
    for i in range(0, len(divs)):
        div = divs[i]
        # 找到tr中的所有td，返回列表
        ps = str(div.find_all('p'))
        # print(ps)
        # 错误 ，最后一位会出错概率挺大
        # regex = r'(?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5])'
        
        # 匹配ip的正则表达式，正确验证过
        regex = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
        ip_list = re.findall(regex, ps)        
        for each in ip_list:        
           print(each)


if __name__ == '__main__':
    crawl_xici_ip()
```
```
本代码执行到if response.status_code == 200 返回503，服务器问题
将原微信里的mango改为mysql

import random
import requests
import time
import pymysql
from bs4 import BeautifulSoup


# 爬取西刺代理网站的代理ip，传入西刺代理的url
url_ip = "http://www.xicidaili.com/nn/"
# 设定等待时间
set_timeout = 2
# 爬取代理的页数，2表示爬取2页的ip地址
num = 2
# 代理的使用次数
count_time = 5
# 构造headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
# 测试ip的URL = 'http://httpbin.org/get',返回以下内容表示正常
# {"args":{},
# "headers":{"Accept":"*/*",
# 			"Accept-Encoding":"gzip, deflate",
# 			"Connection":"close",
# 			"Host":"httpbin.org",
# 			"User-Agent":"python-requests/2.19.1"
# 			},
# "origin":"118.144.138.205",   # http://httpbin.org/ip则只输出origin
# "url":"http://httpbin.org/get"}
url_for_test = 'http://httpbin.org/ip'


# 爬取ip地址
def crawl_xici_ip(num):
    ip_list = []
    for num_page in range(1, num):
        url = url_ip + str(num_page)
        response = requests.get(url)

        if response.status_code == 200:
            content = response.text
            # print('0')
            print(content)
            soup = BeautifulSoup(content, 'html.parser')
            # print('1')
            # print(soup)
            # 从网页源码找规律，ip保存在tr表格中.找到context中的所有tr表格，返回列表
            trs = soup.find_all('tr')

            for i in range(1, len(divs)):
                tr = trs[i]
                # 找到tr中的所有td，返回列表
                tds = div.find_all('td')
                # 122.114.31.177:808
                ip_item = tds[1].text + ':' + tds[2].text
                # 将ip_item加到ip_list中
                ip_list = ip_list.append(ip_item)
                # 通过集合set,去掉可能重复的ip
                ip_set = set(ip_list)
                # 再将ip_list设为列表
                ip_list = list(ip_set)
            time.sleep(count_time)
    return ip_list
    # print('2')

# 测试爬取到的ip，测试成功使用代理可以访问网页，则存入Mysql
def ip_test(url_for_test, ip_info):
    ip = {}
    for ip_for_test in ip_info:
        # 设置代理
        proxies = {
            'http': 'http://' + ip_for_test,
            'https': 'http://' + ip_for_test
        }
        print(proxies)
        try:
            response = requests.get(url_for_test, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                ip = {'ip': ip_for_test}
                print(response.text)
                print('测试通过')
                write_to_Mysql(ip)
        except Exception as e:
            print(e)
            continue
    return ip

# 将测试通过的ip存入Mysql
def write_to_Mysql(proxies):
    # 连接数据库
    conn = pymysql.Connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # mysql服务器端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='ip_test_628',  # 数据库名
        charset='utf8'  # 连接编码
    )
    print('数据库连接对象为：{}'.format(conn))
    # 获取游标
    cursor = conn.cursor()
    # 创建表
    sql = """CREATE TABLE IF NOT EXISTS ip_ip (
             ip  CHAR(20) NOT NULL,
             ip_num  CHAR(20)      
             )"""
    cursor.execute(sql)
    # SQL 表里插入
    for p in proxies:
        sql = """INSERT INTO ip_ip(ip,ip_num)
                 VALUES ('ip', p)"""
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
    print('存储mysql成功')
    
        
    # 查询表里有啥
    sql = """
            select ip, ip_num FROM ip_ip
            """
    cursor.execute(sql)
    list_test_is_or_not_useful_ip = []
    for row in cursor.fetchall():
        print("-" * 50)  # 输出50个-,作为分界线
        # print("%-10s %s" % ("ip", row[0]))  # 字段名固定10位宽度,并且左对齐
        print("%-20s %s" % ("ip_ip", row[1]))
        list_test_is_or_not_useful_ip.append(row[1])
    return list_test_is_or_not_useful_ip
   
    for i in range(len(list_test_is_or_not_useful_ip)):
        useful_proxy = list_test_is_or_not_useful_ip[i].replace('\n', '')
        proxies = {
            'http': 'http://' + useful_proxy,
            'https': 'http://' + useful_proxy
        }
        response = requests.get(url_for_test, headers=headers, proxies=proxies, timeout=10)
        if response.status_code == 200:
            return useful_proxy
    return useful_proxy
        

def main():
    ip_info = []
    ip_info = crawl_xici_ip(2)
    success_proxy = ip_test(url_for_test, ip_info)
    finally_ip = write_to_Mysql(success_proxy)
    print('取出的ip为:' + str(finally_ip))
    print('运行完了，啥结果也没有')

if __name__ == '__main__':
    main()

```


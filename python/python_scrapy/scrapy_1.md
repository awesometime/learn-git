## 爬虫一步步进阶
慕课网小项目

[node.js爬虫 爬取知乎图片存储到本地](https://www.imooc.com/article/22483)

[nodejs爬虫——知乎专栏](https://www.imooc.com/article/17867)

[如何扒视频 B站、斗鱼等都可以](https://www.imooc.com/article/23007)

[Nodejs，不一样的爬虫实践](https://www.imooc.com/article/4731)

- [ beautifulsoup 中文文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)

学习方法

[爬虫学习在线教程  博客后半部分](https://blog.csdn.net/weicao1990/article/details/52334336)

[Python入门网络爬虫之精华版](https://github.com/lining0806/PythonSpiderNotes)

`爬虫方法`

- urllib  加密不好使

- Selenium+Chromedriver 加密的也可以

- Scrapy

对于爬虫框架而言，页面解析工作是调用者自定义的，框架只需要调用用户定义的解析方法，框架提供的拉取和解析中的解析是

指对页面元素的解析，这个已经由fetcher完成。

大型框架的设计思路是，将流程拆分成大的组件，组件之间使用队列进行连接，队列中传输的task内部封装了所有需要传递给组

件进行使用或调用的数据。

用户的整个spider会被翻译成一系列的task，在组件中进行传递，最后获取到结果。

`筛选所需内容方法`

- find

- 正则表达式

- BeautifulSoup lxml 


转载自[Python 爬虫煎蛋网 OOXX 妹子图爬虫（1）——解密图片地址](http://www.tendcode.com/article/jiandan-meizi-spider/)

里面有将加密结果，分析加密源代码，分析如何解密，值得看看。

#### 0    实现有道翻译

```
####################
#     小甲鱼
####################
import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("Enter the contents need to be translated(输入'q'退出程序):")
    if content == "q":
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 修改隐参headers，防止服务器屏蔽，的两种方法1：Request对象生成前
    # head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    data = {"i": content,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8"}
    data = urllib.parse.urlencode(data).encode('utf-8')


    req = urllib.request.Request(url, data) # head)
    # 修改隐参headers，防止服务器屏蔽，的两种方法2：Request对象生成后，利用add_header()方法
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    print(req.headers)


    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)

    # html --> json
    target1 = json.loads(html)
    # print(target1)
    target2 = target1['translateResult'][0][0]['tgt']
    print(target2)
    time.sleep(5)
    

##########################   控制台输出   ####################################
Enter the contents need to be translated(输入'q'退出程序):中国
{'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
                          {"type":"ZH_CN2EN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"中国","tgt":"China"}]]}

China
Enter the contents need to be translated(输入'q'退出程序):q
```

#### 一    利用`urllib.request.Request`和`urllib.request.urlopen`

缺点：

A. urllib抓取网页很容易被当作爬虫来对待，url中加header和使用代理地址和设置time.sleep可以实现一些伪装.

B.不能获取js执行(加密)后的网页内容



代码未使用正则表达式。

```
####################################################################
#  煎蛋网对图片进行了加密因此此方法没有成功        代码未使用正则表达式   #
####################################################################
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

- 待解决的问题：无界面，不用打开浏览器

```
#####################################
#               爬取到了图片          # 
#####################################
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

print(len(img_url))
for j in img_url:
    r=requests.get(j)
    print('正在下载 %s......' % j)
    with open(path+j[-15:],'wb')as jpg:
        jpg.write(r.content)
```

#### 三         用Python爬虫抓取免费代理IP

- [用Python爬虫抓取免费代理IP](https://mp.weixin.qq.com/s/bhf1CrWzY-btSJpwEMth3g)

```
#######################
#本代码爬取到了'http://www.youdaili.net/Daili/http/36822.html'中显示的ip，但没有端口（正则表达式不会写）
#######################
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
#############################################################################################
#改编自https://mp.weixin.qq.com/s/bhf1CrWzY-btSJpwEMth3g，成功爬取西刺ip port并实现Mysql存取数据#
#############################################################################################
import requests
import time
import pymysql
from bs4 import BeautifulSoup

# 爬取西刺代理网站的代理ip，传入西刺代理的url，爬某一页
url_ip = "http://www.xicidaili.com/nn/1"
# 设定等待时间
set_timeout = 2
# 构造headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
# request.get(http://httpbin.org/ip)可以返回自己使用的代理的ip，从而验证此ip有效
url_for_test = 'http://httpbin.org/ip'


# 爬取ip地址
def crawl_xici_ip():
    ip_list = []
    response = requests.get(url_ip, headers=headers)
    # print(response.status_code)
    
    if response.status_code == 200:                
        content = response.text
        # print('0')
        # print(content)
        

        soup = BeautifulSoup(content, 'html.parser')
        # print('1')
        # print(soup)
        
        # 从网页源码找规律，ip保存在tr表格中.找到context中的所有tr表格，返回列表
        # ip_list = []  在此处申明貌似不可以??UnboundLocalError: local variable 'ip_and_port' referenced before assignment
        
        trs = soup.find_all('tr')
        # print(divs)
        #print(len(trs))
        
        for i in range(1, len(trs)):
            tr = trs[i]
            # 找到tr中的所有td，返回列表
            tds = tr.find_all('td')
            
            ip_item = tds[1].text + ':' + tds[2].text
            # 按和网页一样的顺序，一行一行显示ip_item
            # print(ip_item)

            # 将ip_item加到ip_list中
            # ***ip_list = ip_list.append(ip_item)不对***
            ip_list.append(ip_item)

            # 通过集合set,去掉可能重复的ip
            ip_set = set(ip_list)
            # 再将ip_list设为列表
            ip_list = list(ip_set)
        time.sleep(set_timeout)
    
    # for each in ip_list:
    #    print(each)
    # 乱序显示ip列表
    
    # print(ip_list)  # 测试时用，打印列表ip_list
    # print(len(ip_list)) # 注意print语句要写在return语句前，return语句后面不会执行

    return ip_list


# 测试爬取到的ip，测试成功使用代理可以访问网页，则存入Mysql
def ip_test(url_for_test, ip_info):
    ip_and_port = []
    for ip_for_test in ip_info:
        # 设置代理
        proxies = {
            'http': 'http://' + ip_for_test,
            'https': 'http://' + ip_for_test
        }
        # print(proxies)
        try:
            response = requests.get(url_for_test, headers=headers, proxies=proxies, timeout=4)
            # print(response.text)
            if response.status_code == 200:
                ip_and_port.append(ip_for_test)
                # 返回自己的代理ip内容，并非'http://httpbin.org/ip'网页内容，大概就是这个网页的作用
                # print(response.text)

                print("测试通过------" + ip_for_test)
                # write_to_Mysql(ip_and_port)
        except Exception as e:
            print('未通过:(')
            # print(e)
            continue
    print('ip_test执行完毕，下一步将ip存入数据库')
    # print(ip_and_port)
    return ip_and_port


# python与Mysql搭配  存储数据
# 将测试通过的ip存入Mysql     ,需要时取出去，能存能取
def write_to_Mysql(finded_ip_and_port):
    # 连接数据库
    conn = pymysql.Connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # mysql服务器端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='ip_test_628',  # 数据库名
        charset='utf8'  # 连接编码
    )
    print('数据库已连接，对象为：{}'.format(conn))

    # 获取游标
    cursor = conn.cursor()

    
    # 创建表     *注意最好新建一个不存在的表
    sql = """CREATE TABLE IF NOT EXISTS ip_my (
             ip  CHAR(20) NOT NULL,
             ip_num  CHAR(30)      
             )"""
    cursor.execute(sql)
    print('已创建tabels')

    
    # SQL 表里插入
    sql = """INSERT INTO ip_my(ip,ip_num)
             VALUES ('ip', %s)"""
    cursor.executemany(sql, finded_ip_and_port)
    # 提交到数据库执行
    conn.commit()
    # 如果发生错误则回滚
    # conn.rollback()
    print('mysql数据表已插入')

    
    # 查询表里有啥
    sql = """
            select * FROM ip_my
            """
    cursor.execute(sql)
    fetch_ip = cursor.fetchall()          # 返回元组
    cursor.close()

    # print(cursor.execute(sql))          # 返回指针地址数字
    # return cursor.execute(sql)

    fetch_ip = list(fetch_ip)
    finded_ip = []
    for row in fetch_ip:
        print("-" * 50)                       # 输出50个-,作为分界线
        # print("%-10s %s" % ("ip", row[0]))  # 字段名固定10位宽度,并且左对齐
        print("%-20s %s" % ("ip_port", row[1]))
        finded_ip.append(row[1])
    return finded_ip


def main():
    ip_info = []
    ip_info = crawl_xici_ip()
    finded_proxy = ip_test(url_for_test, ip_info)
    finally_ip = write_to_Mysql(finded_proxy)
    print('#' * 50)
    f = str(finally_ip)
    print('取出的ip为:' + f)
    # print(type(f))
    print('运行完了，结果ok--：):):)')


if __name__ == '__main__':
    main()
```
#### 四  将彩票信息爬取存入Excel
```
import requests
from bs4 import BeautifulSoup
import xlwt                              # xlrd 对 Excel 读   ,xlwt 对 Excel 写

## 转自https://mp.weixin.qq.com/s/VdoJxZNU24u0ILKxYPS4lg
## 步骤：
##   HTML下载器：下载HTML网页                               requests.get
##   HTML解析器：解析出有效数据                              BeautifulSoup(html, 'lxml')
##   数据存储器：将有效数据通过文件或者数据库的形式存储起来      xlwt写入Excel


# 获取第一页的内容
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 63.0.3239.132 Safari / 537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# 解析第一页内容，数据结构化
def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')                                 # lxml ，HTML Parser  文档解析模块
    i = 0
    for item in soup.select('tr')[2:-1]:                               # soup.select
        yield {                                                        # 使用yield的好处?????
            'time': item.select('td')[i].text,
            'issue': item.select('td')[i + 1].text,
            'digits': item.select('td em')[0].text,
            'ten_digits': item.select('td em')[1].text,
            'hundred_digits': item.select('td em')[2].text,
            'single_selection': item.select('td')[i + 3].text,
            'group_selection_3': item.select('td')[i + 4].text,
            'group_selection_6': item.select('td')[i + 5].text,
            'sales': item.select('td')[i + 6].text,
            'return_rates': item.select('td')[i + 7].text
        }
    # 无return可以吗？？？


# 将数据写入Excel表格中
def write_to_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('3D', cell_overwrite_ok=True)
    row0 = ["开奖日期", "期号", "个位数", "十位数", "百位数", "单数", "组选3", "组选6", "销售额", "返奖比例"]
    # 写入第一行
    for j in range(0, len(row0)):
        sheet1.write(0, j, row0[j])     # write(行，列， 具体内容)

    # 依次爬取每一页内容的每一期信息，并将其依次写入Excel
    i = 0
    for k in range(1, 5):  # 这里只爬取5页作为练习
        url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_%s.html' % (str(k))
        html = get_one_page(url)
        print('正在保存第%d页。' % k)
        # 写入每一期的信息
        for item in parse_one_page(html):
            sheet1.write(i + 1, 0, item['time'])
            sheet1.write(i + 1, 1, item['issue'])
            sheet1.write(i + 1, 2, item['digits'])
            sheet1.write(i + 1, 3, item['ten_digits'])
            sheet1.write(i + 1, 4, item['hundred_digits'])
            sheet1.write(i + 1, 5, item['single_selection'])
            sheet1.write(i + 1, 6, item['group_selection_3'])
            sheet1.write(i + 1, 7, item['group_selection_6'])
            sheet1.write(i + 1, 8, item['sales'])
            sheet1.write(i + 1, 9, item['return_rates'])
            i += 1

    f.save('3D.xls')     # 写上完整路径,就会保存在你所写的路径下，否则保存在默认位置


def main():
    write_to_excel()


if __name__ == '__main__':
    main()
```

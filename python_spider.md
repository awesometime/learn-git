## 爬虫一步步进阶

`爬虫方法`

- urllib  加密不好使

- Selenium+Chromedriver 加密的也可以

- Scrapy

`筛选所需内容方法`

-find

-正则表达式

-BeautifulSoup lxml 


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

-[Selenium使用详解](https://www.jianshu.com/p/4b89c92ff9b4)

-`Selenium+PhantomJS`UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions 

of Chrome or Firefox instead

Selenium不再支持PhantomJS(无界面浏览器)

-选择Selenium+Chromedriver(前提要有chrome，两exe文件放在同一文件夹下)

- 使用了`BeautifulSoup`方法，BeautifulSoup是一个模块，该模块用于接收一个HTML或XML字符串，然后将其进行格式化，

之后便可以使用他提供的方法进行快速查找指定元素，从而使得在HTML或XML中查找指定元素变得简单。

-[BeautifulSoup基本用法总结](https://blog.csdn.net/kikaylee/article/details/56841789)

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





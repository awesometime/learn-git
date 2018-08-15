#encoding:utf-8

"""
本程序实现从百度爬取图片
"""

import urllib3
import urllib
import re
import os
import http.cookiejar
import codecs
import socket
import threading

# 从页面中检索到 item.jd.com/23.html 这样的字符串
# 返回http://item.jd.com/23.html
def retrieve_urls_from_page(html):
    reg_exp = 'item\.jd\.com\/[\d]+\.html'
             # item.jd.com/数字.html
    new_url_list = []
    for url in re.findall(reg_exp, html):
        url = 'http://' + url
        new_url_list.append(url)

# 从给定url  download得到jd首页各分类导航标签网址,返回url_list
def download_url_list():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    url = 'http://www.jd.com'

    response = opener.open(url)
    html = response.read().decode('utf-8', 'ignore')
    # 主页左边分类导航栏
    start_pattern = 'class=\"cate_menu_lk\"'
    end_pattern = '</a>'

    start_position = html.find(start_pattern)

    link_str = ''
    while start_position > 0:
        html = html[start_position+len(start_pattern):]
        end_position = html.find(end_pattern)
        if end_position > 0:
            link_str += html[0:end_position]
        start_position = html.find(start_pattern)
    # 找到各分类标签的网址(字符串)如
    # href="//jiadian.jd.com">家用电器 href="//shouji.jd.com/">手机 href="//wt.jd.com">运营商...

    # print(link_str)

    url_re = '\/\/[a-z.\/\d\-]+'
    # '//字母./数字-+'
    url_list = []
    for url in re.findall(url_re, link_str):
        url = 'http:' + url
        url_list.append(url)

    # print(url_list)
    # ['http://jiadian.jd.com', 'http://shouji.jd.com/', 'http://wt.jd.com',...]
    return url_list
# 前两def未调用过？？



visited = {}
item_urls = []

# 返回''
def retrive_info_by_pattern(html, start_pattern, end_pattern):
    start_pos = html.find(start_pattern)
    #print ('start_pos', start_pos)

    # sku-name
    if start_pos > 0:
        end_pos = html.find(end_pattern, start_pos)

        info = html[start_pos:end_pos]
        start_pos = info.rfind('>')
        data = info[start_pos + 1:].strip()
        return data.replace('\t', ' ')
    # href = "//jiadian.jd.com" > 家用电器 href = "//shouji.jd.com/" > 手机
    # 输出'家用电器'、'手机'、'运营商'、'数码'这样的sku-name
    return ''
    # 为什么返回'',而且找sku-name时不需要用循环找到所有的sku-name？？？
    # 我改成 return data
    # return data

# retrieve_sku_info(html)
# return [sku_category1,sku_category2,sku_category3,sku_name]
# 调用retrive_info_by_pattern(html, start_pattern, end_pattern)
def retrieve_sku_info(html):
    # sku-name
    start_pattern = 'sku-name'
    end_pattern = '</div>'

    sku_name = retrive_info_by_pattern(html, start_pattern, end_pattern)

    #sku-type
    start_pattern = 'mbNav-1'
    end_pattern = '</a>'
    sku_category1 = retrive_info_by_pattern(html, start_pattern, end_pattern)
    sku_category1 = sku_category1.replace(' ', '')

    start_pattern = 'mbNav-2'
    end_pattern = '</a>'
    sku_category2 = retrive_info_by_pattern(html, start_pattern, end_pattern)
    sku_category2 = sku_category2.replace(' ', '')

    start_pattern = 'mbNav-3'
    end_pattern = '</a>'
    sku_category3 = retrive_info_by_pattern(html, start_pattern, end_pattern)
    sku_category3 = sku_category3.replace(' ', '')

    return [sku_category1,sku_category2,sku_category3,sku_name]

# return   new_url_list, sku_information
# 调用retrieve_sku_info(html)
def crawl(parent_url):
    print ('do crawl')
    cookie = http.cookiejar.CookieJar()
    handler = urllib3.HTTPCookieProcessor(cookie)
    opener = urllib3.build_opener(handler)

    response = opener.open(parent_url)
    html = response.read().decode('gbk', 'ignore')

    html = html.replace('\\/','/')

    new_url_list = []
    sku_information = []
    links = re.findall(r'href\=\"(\/\/[a-zA-Z0-9\.\/\-]+)\"', html)
    for link in links:
        # python 多个and啥意思来着
        if link.find('jd.com') > 0 and link.find('club.jd.com') < 0 and link.find('item.m.jd.com') < 0 and link.find('help.jd.com') < 0 and link.find('yp.jd.com') < 0:
            link = 'http:' + link
            new_url_list.append(link)

    if parent_url.find('item.jd.com') >= 0:
        id_reg_exp = '[\d]+'
        all_found = re.findall(id_reg_exp, parent_url)
        sku_information.append(all_found[0])
        for item in retrieve_sku_info(html):
            sku_information.append(item)

    print ('sku',sku_information)

    #print sku_information
    return new_url_list, sku_information

# 将sku_information  save到'G:/jd/sku.txt'
def save_sku_information(sku_list):
    #print 'sku_list:',sku_list
    #with codecs.open('/home/exocr/workspace/data/jd/sku.txt','a+','utf-8') as f:
    with codecs.open('G:/jd/sku.txt','a+','utf-8') as f:
        for sku in sku_list:
            line = u'\t'.join(sku)
            f.write(line)
            f.write('\r')

# save url_list=[...] to G:/jd/url.txt,
# save visited={...} to G:/jd/visited.txt
def save_url_info():
    #with codecs.open('/home/exocr/workspace/data/jd/url.txt', 'w', 'utf-8') as f:
    with codecs.open('G:/jd/url.txt', 'w', 'utf-8') as f:
        #f.writelines(item_urls)
        for url in item_urls:
            f.write(url)
            f.write('\r')

    #with codecs.open('/home/exocr/workspace/data/jd/visited.txt', 'w', 'utf-8') as f:
    with codecs.open('G:/jd/visited.txt', 'w', 'utf-8') as f:
        for key,val in visited.items():
            f.write(key)
            f.write('\r')

mutex = threading.Lock()
url_joined = {}

# 主要函数process，子线程
# 调用def crawl(parent_url)
#     save_url_info()
#     save_sku_information(sku_list)
def process():
    sku_list = []
    while True:
        print (len(item_urls))
        if len(item_urls) == 0:
            break
        else:
            mutex.acquire()
            url = item_urls.pop(0)
            mutex.release()

            print ('url:', url)

            if len(url) == 0:
                continue

            #already crawled
            # if visited.has_key(url):
            if url in visited:
                print ('it is visited')
                continue

            visited[url] = 1

            try:
                # def crawl(parent_url)：
                new_urls, sku_information = crawl(url)
            except:
                print ('except....................................................')
                continue

            #return

            for url in new_urls:
                #already visited
                #if url_joined.has_key(url):
                if url in url_joined:
                    continue

                url_joined[url] = 1
                item_urls.append(url)

            if len(sku_information) > 0:
                print (u','.join(sku_information))

            sku_list.append(sku_information)

            if len(sku_list) > 1000:
                mutex.acquire()

                # 将sku_information  save到'G:/jd/sku.txt'
                # def save_sku_information(sku_list)
                save_sku_information(sku_list)

                sku_list = []

                # save url_list=[...] to G:/jd/url.txt,
                # save visited={...} to G:/jd/visited.txt
                # def save_url_info()
                save_url_info()

                mutex.release()



if __name__ == '__main__':
    socket.setdefaulttimeout(5)
    try:
        #visited_url_file = '/home/exocr/workspace/data/jd/visited.txt'
        visited_url_file = 'G:/jd/visited.txt'
        with open(visited_url_file, 'r') as f:
            # visited_urls = {list} [, , , , ]
            visited_urls = f.readlines()
            for url in visited_urls:
                if len(url) > 0:
                    visited[url] = 1
    # {dict} visited = {'https://sale.jd.com/act/ZKihCPSVnO1WseFd.html\n': 1, 'https://yp.jd.com/act/ZKihCPSVnO1WseFd.html\n': 1, 'https://item.m.jd.com/\n': 1, 'https://me.jd.com/act/\n': 1, 'https://club.jd.com/act/\n': 1, 'https://help.jd.com/act/\n': 1, 'https://group.jd.com/act/ZKihCPSVnO1WseFd.html\n': 1, 'https://sale.jd.com/act/ZKihCPSVnO1WseFd.html': 1}

    except:
        pass

    #item_url_file = '/home/exocr/workspace/data/jd/url.txt'
    item_url_file = 'G:/jd/url.txt'
    with open(item_url_file, 'r') as f:
        lines = f.read().split('\r')
        for line in lines:
            if line.find('yp.jd.com') < 0 and line.find('item.m.jd.com') < 0 and line.find('me.jd.com') < 0 and line.find('group.jd.com') < 0 and line.find('group.jd.com') < 0 and line not in url_joined:
                item_urls.append(line.strip())
                url_joined[line] = 1

    print (len(item_urls))

    #print item_urls
    #for i in range(500):
    for i in range(3):
        t = threading.Thread(target=process, args=())
        t.setDaemon(True)
        t.start()
        t.join()

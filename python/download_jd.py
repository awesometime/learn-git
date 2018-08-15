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

def retrieve_urls_from_page(html):
    reg_exp = 'item\.jd\.com\/[\d]+\.html'

    new_url_list = []
    for url in re.findall(reg_exp, html):
        url = 'http://' + url
        new_url_list.append(url)

def download_url_list():
    cookie = cookielib.CookieJar()
    handler = urllib3.HTTPCookieProcessor(cookie)
    opener = urllib3.build_opener(handler)
    url = 'http://www.jd.com'

    response = opener.open(url)
    html = response.read().decode('utf-8', 'ignore')

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

    #print link_str

    url_re = '\/\/[a-z.\/\d\-]+'
    url_list = []
    for url in re.findall(url_re, link_str):
        url = 'http:' + url
        url_list.append(url)

    #print url_list

    return url_list

visited = {}
item_urls = []

def retrive_info_by_pattern(html, start_pattern, end_pattern):
    start_pos = html.find(start_pattern)
    #print 'start_pos', start_pos

    # sku-name
    if start_pos > 0:
        end_pos = html.find(end_pattern, start_pos)

        info = html[start_pos:end_pos]
        start_pos = info.rfind('>')
        data = info[start_pos + 1:].strip()
        return data.replace('\t', ' ')

    return ''

def retrieve_sku_info(html):
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

def crawl(parent_url):
    print ('do crawl')
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    response = opener.open(parent_url)
    html = response.read().decode('gbk', 'ignore')

    html = html.replace('\\/','/')

    new_url_list = []
    sku_information = []
    links = re.findall(r'href\=\"(\/\/[a-zA-Z0-9\.\/\-]+)\"', html)
    for link in links:
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

def save_sku_information(sku_list):
    #print 'sku_list:',sku_list
    with codecs.open('/home/exocr/workspace/data/jd/sku.txt','a+','utf-8') as f:
        for sku in sku_list:
            line = u'\t'.join(sku)
            f.write(line)
            f.write('\r')


def save_url_info():
    with codecs.open('/home/exocr/workspace/data/jd/url.txt', 'w', 'utf-8') as f:
        #f.writelines(item_urls)
        for url in item_urls:
            f.write(url)
            f.write('\r')

    with codecs.open('/home/exocr/workspace/data/jd/visited.txt', 'w', 'utf-8') as f:
        for key,val in visited.items():
            f.write(key)
            f.write('\r')

mutex = threading.Lock()
url_joined = {}
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
            if visited.has_key(url):
                print ('it is visited')
                continue

            visited[url] = 1

            try:
                new_urls, sku_information = crawl(url)
            except:
                print ('except....................................................')
                continue

            #return

            for url in new_urls:
                #already visited
                if url_joined.has_key(url):
                    continue

                url_joined[url] = 1
                item_urls.append(url)

            if len(sku_information) > 0:
                print (u','.join(sku_information))

            sku_list.append(sku_information)

            if len(sku_list) > 1000:
                mutex.acquire()
                save_sku_information(sku_list)
                sku_list = []
                save_url_info()
                mutex.release()



if __name__ == '__main__':
    socket.setdefaulttimeout(5)
    try:
        #visited_url_file = '/home/exocr/workspace/data/jd/visited.txt'
        visited_url_file = 'G:/jd/visited.txt'
        with open(visited_url_file, 'r') as f:
            visited_urls = f.readlines()
            for url in visited_urls:
                if len(url) > 0:
                    visited[url] = 1
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
    for i in range(500):
        t = threading.Thread(target=process, args=())
        t.setDaemon(True)
        t.start()
        t.join()

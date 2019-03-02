#encoding:utf-8

"""
本程序实现从百度爬取图片
"""

import urllib2
import urllib
import re
import os
import cookielib
import codecs
import socket
import threading
import xml.etree.ElementTree as ET

from pyquery import PyQuery as pq


def retrieve_urls_from_page(html):
    reg_exp = 'item\.jd\.com\/[\d]+\.html'

    new_url_list = []
    for url in re.findall(reg_exp, html):
        url = 'http://' + url
        new_url_list.append(url)

def download_url_list():
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
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
    print 'do crawl'
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

    print 'sku',sku_information

    #print sku_information
    return new_url_list, sku_information

def process(stock_exchange_name):
    all_security_list = []
    for page in range(1, 1000):
        url = 'http://app.finance.ifeng.com/list/stock.php?t=%s&f=chg_pct&o=desc&p=%d' % (stock_exchange_name,page)
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)

        response = opener.open(url)
        html = response.read().decode('utf-8', 'ignore')

        pq_html = pq(html)
        table_html = pq_html.find('table')
        pq_tr_list = table_html.find('tr')

        security_list = []

        for pq_tr in pq_tr_list.items():
            pq_td_list = pq_tr.find('td').items()

            td_html_list = []

            for pq_td in pq_td_list:
                td_html_list.append(pq_td.text())

            if len(td_html_list) < 2:
                continue

            id = td_html_list[0]
            name = td_html_list[1]
            if len(name) == 0:
                continue
            print id,name
            security_list.append([id, name])
            all_security_list.append([id,name])

        if len(security_list) == 0:
            print 'done after page:', page, len(all_security_list)
            break

    return all_security_list




if __name__ == '__main__':
    socket.setdefaulttimeout(5)

    exchange_list = ['ha', 'hb', 'sa', 'sb', 'zxb', 'cyb', 'zs', 'jj', 'etf', 'zq']
    all_security_list = []
    for exchange in exchange_list:
        security_list = process(exchange)
        for security in security_list:
            all_security_list.append(security)

    print len(all_security_list)

    with codecs.open('/home/exocr/workspace/images/securities.txt', 'w', 'utf-8') as f:
        for security in all_security_list:
            line = u'\t'.join(security)
            f.write(line)
            f.write('\n')
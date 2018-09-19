##############
config.json    #貌似没用，不太需要

# https://moshuqi.github.io/2016/08/12/Python%E7%88%AC%E8%99%AB-PySpider%E6%A1%86%E6%9E%B6/
##############
{
	"taskdb": "mysql+taskdb://127.0.0.1:3306/pyspider_taskdb",
  	"projectdb": "mysql+projectdb://127.0.0.1:3306/django_99",
  	"resultdb": "mysql+resultdb://127.0.0.1:3306/pyspider_resultdb",
  	//"message_queue": "redis://127.0.0.1:6379/db",
	"webui": {
		"port": 5000
	}
}
################




#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-09-19 14:53:50
# Project: https://reeoo.com/

from pyspider.libs.base_handler import *
import pymysql

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://reeoo.com/', callback=self.index_page,validate_cert=False)    # http 599

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div[class="thumb"]').items():       # css 选择器
            detail_url = each('a').attr.href
            #print (detail_url)
            self.crawl(detail_url, callback=self.detail_page,validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        header = response.doc('body > article > section > header')
        title = header('h1').text()

        tags = []
        for each in header.items('a'):
            tags.append(each.text())

        content = response.doc('div[id="post_content"]')
        description = content('blockquote > p').text()

        website_url = content('a').attr.href

        image_url_list = []
        for each in content.items('img[data-src]'):
            image_url_list.append(each.attr('data-src'))

        return {
            "title": title,
            "tags": tags,
            "description": description,
            "image_url_list": image_url_list,
            "website_url": website_url,
             }
    
    
    def on_result(self, result):
        if not result:
            return

        data = {
            'title': result['title'],
            'tags': str(result['tags']),            # tag是一个列表，有多列，插入数据库时报 Operand should contain 1 column(s) ,转成str
            'description': result['description'],
            'website_url': result['website_url'],
            'image_url_list': result['image_url_list']
             }
        
        conn = pymysql.Connect(
                host='localhost',  
                port=3306,  
                user='root',  
                passwd='root',  
                db='django_99',  
                charset='utf8'  
                     )
        cursor = conn.cursor()
        
        sql = """INSERT INTO pyspider_reeoo(title, tags, description, website_url, image_url_list)
                     VALUES (%s, %s, %s, %s, %s)"""		
        cursor.execute(sql,(data['title'], data['tags'], data['description'], data['website_url'], data['image_url_list']))
        
        conn.commit()           # commit() 数据库才能插入
        conn.close()
        
        print (' dump into mysql success :):):) ')
        
        
        
        
        
        
        
        
        

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-09-19 19:35:44
# Project: douban_movie

################
# 待解决：：：

# 检测到有异常请求从你的 IP 发出，请 登录 使用豆瓣。
# genre nation 抓取方法   英文名字分隔
# url    return 加url
# 存数据库
################


from pyspider.libs.base_handler import *
import pymysql

class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        i =-25
        while  i<225:
            i += 25
            url = 'https://movie.douban.com/top250?start=' + str(i) +'&filter='
            self.crawl(url, callback=self.index_page,validate_cert=False)
        print('on_start运行完follow 有10个url，点击follow中每个url分别调用index_page(),点击insex_page后的三角进入每一页的25个影片吧')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        
        
        for each in response.doc('#content > div > div.article > ol > li > div > div.info > div.hd > a').items():
            url = each.attr.href
            self.crawl(url, callback=self.detail_page,validate_cert=False)
            return url  # 未验证
        print('每一页的25个影片找到，继续调用detail_page()得到每一影片详情')
        
        
        
    @config(priority=2)
    def detail_page(self, response, url):
        
        mv_url = url  # 未验证
         
        No= response.doc('#content > div.top250 > span.top250-no').text()

        Zh_name= response.doc('#content > h1 > span:nth-child(1)').text().split(' ')[0]

        # 单词未分开
        En_name= ''.join(response.doc('#content > h1 > span:nth-child(1)').text().split(' ')[1:])

        director= response.doc('#info > span:nth-child(1) > span.attrs > a').text()

        writers = response.doc('#info > span:nth-child(3) > span.attrs > a').text()
                    
        actors = response.doc('#info > span.actor > span.attrs')('a').text()
                    
        rating_num= response.doc('#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong').text()
        
        #genre= []
        #print(response.xpath("//*[@id="info"]/text()[2]"))
            #genre.append(each.html())
        
        # nation 不会抓
        # url 加上
        
        print('top 250共10页 ——>  每页25个电影  ——>  现在在每部电影的详情页 ------<<<<<<  :):):)')
        
        return {
            "mv_url":url,
            "No":No ,
            "Zh_name": Zh_name,
            "En_name" :En_name,
            "director": director,
            "writers": writers,
            "actors": actors,
            #"genre": genre,
            "rating_num":rating_num,
                }
        
    # 未验证   
    def on_result(self, result):
            if not result:
                return

            data = {
                "mv_url":result['mv_url'],
                "No":result['No'],
                "Zh_name": result['Zh_name'],
                "En_name" :result['En_name'],
                "director": result['director'],
                "writers": result['writers'],
                "actors": result['actors'],            
                "rating_num":result['rating_num'],
                    }

            conn = pymysql.Connect(
                    host='localhost',  
                    port=3306,  
                    user='',  
                    passwd='',  
                    db='99',  
                    charset='utf8'  
                         )
            cursor = conn.cursor()

            sql = """INSERT INTO pyspider_doubanmv(No, Zh_name, En_name, director, writers, actors, rating_num)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""		
            cursor.execute(sql,(data['No'], data['Zh_name'], data['En_name'], data['director'], data['writers'], data['actors'], data['rating_num']))

            conn.commit()          
            conn.close()

            print (' dump into mysql success :):):) ')

        
        
    

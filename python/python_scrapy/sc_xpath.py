# -*- coding: utf-8 -*-
import scrapy
import re
from Artical_spider.items import ArticalSpiderItem

class JobboleSpider(scrapy.Spider):
    """
    功能：爬取
    """
    # 爬虫名
    name = "jobbole"
    # 爬虫作用范围
    allowed_domains = ["blog.jobbole.com"]

    url = "http://blog.jobbole.com/114407/"


    def parse(self, response):
        #title = response.xpath('//*[@id="post-114407"]/div[1]/h1/text()').extract()[0]
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        
        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
        
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        
        # 正文
        content = response.xpath("//div[@class='entry']").extract()

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endwith('评论')]
        #tag_list = ['IT技术', 'Redis', '数据库']
        tags = ",".join(tag_list)
        # tags = 'IT技术,Redis,数据库'

        pass

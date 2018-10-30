### CrawlSpiders

- [Scrapy框架CrawlSpiders的介绍以及使用详解](https://www.jb51.net/article/129351.htm)

### Scrapy框架

-[Scrapy框架学习（四）----CrawlSpider、LinkExtractors、Rule及爬虫示例](https://blog.csdn.net/qq_33689414/article/details/78669514)

-[scrapy——高级深度操作  Spider CrawlSpider完成数据深度爬取](https://www.jianshu.com/p/09e29b0a4b29)

-[Scrapy 中文网](http://www.scrapyd.cn/)

-[Scrapy 0.24 文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24)



### 1  创建虚拟环境,参考Django   下载好scrapy相关依赖包   新建工程

### 2  不利用虚拟环境,直接在g:\\python\\python-3.6.5\\lib\\site-packages下载好相关依赖包   新建工程
```
F:\Python\projects>            scrapy startproject tencent
New Scrapy project 'tencent', using template directory 'c:\\linuix\\python37\\lib\\site-packages\\scrapy\\templates\\project', created in:
    F:\Python\projects\tencent

You can start your first spider with:
    cd tencent
    scrapy genspider example example.com

F:\Python\projects>cd tencent
F:\Python\projects\tencent>     scrapy genspider --list

F:\Python\projects\tencent>     scrapy genspider -t crawl tencent hr.tencent.com
Cannot create a spider with the same name as your project

F:\Python\projects\tencent>      scrapy genspider -t crawl tencentjob hr.tencent.com
Created spider 'tencentjob' using template 'crawl' in module:
  tencent.spiders.tencentjob
```    
### 3 Debug 调试程序

`G:\PyCharm\PythonProjects\Artical_spider>scrapy shell http://blog.jobbole.com/114407/`

shell中加请求头

`G:\PyCharm\PythonProjects\Article_spider>scrapy shell -s USER_AGENT="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36" https://www.zhihu.com/`

```python
#G:\PyCharm\PythonProjects\Artical_spider>scrapy shell http://blog.jobbole.com/114407/

#2018-09-26 16:17:23 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: Artical_spider)
#2018-09-26 16:17:23 [scrapy.utils.log] INFO: Versions: lxml 4.2.3.0, libxml2 2.9.5, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0h  27 Mar 2018), cryptography 2.2.2, Platform Windows-10-10.0.17134-SP0

[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x0000012A00E70CC0>
[s]   item       {}
[s]   request    <GET http://blog.jobbole.com/114407/>
[s]   response   <200 http://blog.jobbole.com/114407/>
[s]   settings   <scrapy.settings.Settings object at 0x0000012A02177898>
[s]   spider     <JobboleSpider 'jobbole' at 0x12a02411400>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
In [1]: re_selector = response.xpath('//*[@id="post-114407"]/div[1]/h1/text()')

In [2]: re_selector
Out[2]: [<Selector xpath='//*[@id="post-114407"]/div[1]/h1/text()' data='Redis 避不开的五种数据结构'>]

In [3]: re_selector.extract()
Out[3]: ['Redis 避不开的五种数据结构']

In [4]: re1_selector = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()')

In [5]: re1_selector
Out[5]: [<Selector xpath='/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()' data='Redis 避不开的五种数据结构'>]

In [6]: re1_selector.extract()
Out[6]: ['Redis 避不开的五种数据结构']

In [7]: re2_selector = response.xpath('//div[@class="entry-header"]/h1/text()')

In [8]: re2_selector
Out[8]: [<Selector xpath='//div[@class="entry-header"]/h1/text()' data='Redis 避不开的五种数据结构'>]

In [9]: re2_selector.extract()
Out[9]: ['Redis 避不开的五种数据结构']

In [10]: re2_selector.extract()[0]
Out[10]: 'Redis 避不开的五种数据结构'

In [14]: response.xpath("//p[@class='entry-meta-hide-on-mobile']")
Out[14]: [<Selector xpath="//p[@class='entry-meta-hide-on-mobile']" data='<p class="entry-meta-hide-on-mobile">\r\n\r'>]

In [16]: response.xpath("//p[@class='entry-meta-hide-on-mobile']").extract()
Out[16]: ['<p class="entry-meta-hide-on-mobile">\r\n\r\n            2018/09/25 ·  <a href="http://blog.jobbole.com/category/it-tech/" rel="category tag">IT技术</a>\r\n            \r\n            \r\n\r\n            \r\n             ·  <a href="http://blog.jobbole.com/tag/redis/">Redis</a>, <a href="http://blog.jobbole.com/tag/database/">数据库</a>\r\n            \r\n</p>']

In [18]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()
Out[18]:
['\r\n\r\n            2018/09/25 ·  ',
 '\r\n            \r\n            \r\n\r\n            \r\n             ·  ',
 ', ',
 '\r\n            \r\n']

In [19]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0]
Out[19]: '\r\n\r\n            2018/09/25 ·  '

In [20]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip()
Out[20]: '2018/09/25 ·'

In [21]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace(".","")
Out[21]: '2018/09/25 ·'

In [26]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","")
Out[26]: '2018/09/25 '

In [27]: response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
Out[27]: '2018/09/25'

In [28]: response.xpath("//span[contains(@class, 'vote-post-up')]")
Out[28]: [<Selector xpath="//span[contains(@class, 'vote-post-up')]" data='<span data-post-id="114407" class=" btn-'>]

In [29]: response.xpath("//span[contains(@class, 'vote-post-up')]").extract()
Out[29]: ['<span data-post-id="114407" class=" btn-bluet-bigger href-style vote-post-up   register-user-only "><i class="fa  fa-thumbs-o-up"></i> <h10 id="114407votetotal">1</h10> 赞</span>']

In [30]: response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()
Out[30]: ['1']

In [31]: int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
Out[31]: 1

In [43]: response.xpath("//a[@href='#article-comment']/span")
Out[43]: [<Selector xpath="//a[@href='#article-comment']/span" data='<span class="btn-bluet-bigger href-style'>]

In [44]: response.xpath("//a[@href='#article-comment']/span/text()")
Out[44]: [<Selector xpath="//a[@href='#article-comment']/span/text()" data='  评论'>]

In [45]: response.xpath("//a[@href='#article-comment']/span/text()").extract()
Out[45]: ['  评论']

In [46]: response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
Out[46]: '  评论'

```

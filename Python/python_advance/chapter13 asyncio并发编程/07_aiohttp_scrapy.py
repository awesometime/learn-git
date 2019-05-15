# aiohttp实现高并发爬虫 
# asyncio爬虫， 去重， 入库

import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery

stopping = False

start_url = 'http://www.jobbole.com'
waitting_urls = []
seen_urls = set()  # 实际使用爬虫去重时，数量过多，需要使用布隆过滤器


async def fetch(url, session):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                print('url status: {}'.format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):  # html中提取所有url
    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        if url and url.startwith('http') and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(urls)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):  # 获取文章详情并解析入库
    html = await fetch(url, session)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq('title').text()  # 为了简单， 只获取title的内容
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('SELECT 42;')
            insert_sql = "insert into article_test(title) values('{}')".format(
                title)
            await cur.execute(insert_sql)  # 插入数据库
            # print(cur.description)
            # (r,) = await cur.fetchone()
            # assert r == 42


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:  # 如果使用asyncio.Queue的话， 不需要我们来处理这些逻辑。
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print('start get url:{}'.format(url))
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:  # 是没有处理过的url，则处理
                    asyncio.ensure_future(article_handler(url, sssion, pool))
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url))


async def main(loop):
    # 等待mysql连接建立好
    pool = await aiomysql.creat_pool(host='127.0.0.1', port=3306, user='root',
                                     password='', db='aiomysql_test', loop=loop, charset='utf8', autocommit=True)
    # charset  autocommit必须设置， 这是坑， 不写数据库写入不了中文数据
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()

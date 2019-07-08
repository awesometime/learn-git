	Redis为什么这么快？redis采用多线程会有哪些问题？

	Redis支持哪几种数据结构；

	Redis跳跃表的问题；

	Redis单进程单线程的Redis如何能够高并发?

	Redis如何使用Redis实现分布式锁？

	Redis分布式锁操作的原子性，Redis内部是如何实现的


  * [1 install and docs](#1-install-and-docs)
  * [2 redis 基础语法](#2-redis-基础语法)
  * [3 redis-py python 操作 redis](#3-redis-py-python-操作-redis)
  * [4 ]
  
### 1 install and docs

- [redis 安装配置](https://www.cnblogs.com/joyet/p/6103041.html)
- [redis 中文网](http://www.redis.cn/)
- [redis 中文网 redis 知识树](http://www.redis.cn/map.html)
- [github redis-py文档](https://github.com/andymccurdy/redis-py)
- [Welcome to redis-py’s documentation](https://redis-py.readthedocs.io/en/latest/)
- [通过思维导图整理redis的重要知识点](https://github.com/Weiwf/redis-mindmap)

### 2 redis 基础语法

https://www.runoob.com/redis/redis-data-types.html

https://www.cnblogs.com/dddyyy/p/9803828.html

string
```
String Key-Value

set key value  设置值
get key        获取值
mset           设置多个值
mget           获取多个值
append
del
incr/decr      对应的 value 自增/减1,如果没有这个key值 自动给你创建创建 并赋值为1
```
list
```
lpush rpush
lrange
ltrim 截完原来list中就没有了
lpop rpop
lpushx rpushx

```
set
```
无顺序，不能重复
sadd key members   添加
srem key a-member  删除
sismember
smembers key     查询 打印集合中的成员
sdiff
sinter
sunion
```
hash
```
hset-key-filed-value

HMSET myhash field1 "Hello" field2 "World"
HGET myhash field1
HGET myhash field2
```
SortedSet（zset）
```
有顺序，不能重复

适合做排行榜 排序需要一个分数属性

zadd zset1 9 a 8 c 10 d 1 e   （添加元素 zadd key score member ）

(ZRANGE key start stop [WITHSCORES])(查看所有元素：zrange key  0  -1  withscores)

如果要查看分数，加上withscores.

zrange zset1 0 -1 (从小到大)

zrevrange zset1 0 -1 (从大到小)

zincrby zset2 score member (对元素member 增加 score)
```

### 3 redis-py python 操作 redis
```python
import redis


class TestString(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def test_set(self):
		rest = self.r.set("user1", "hanmeimei")
		print(rest)
		return rest


	def test_get(self):
		rest = self.r.get("user1")
		print(rest)
		return rest


	def test_mset(self):
		dict = {
				'user2': 'bob',
				'user3': 'bobbo',
				}
		rest = self.r.mset(dict)
		print(rest)
		return rest


	def test_mget(self):
		list = ['user2', 'user3']
		rest = self.r.mget(list)
		print(rest)
		return rest


	def test_delete(self):
		rest = self.r.delete('user1')
		print(rest)


class TestList(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def test_push(self):
		"""lpush rpush"""
		t = ('awo', 'bwo', 'cff', 'dgg')
		# [b'dgg', b'cff', b'bwo', b'awo']
		rest = self.r.lpush("l_eat1", *t)
		print(rest)
		result = self.r.lrange("l_eat1", 0, -1)
		print(result)


	def test_pop(self):
		"""lpop rpop"""		
		rest = self.r.lpop("l_eat1")
		print(rest)
		result = self.r.lrange("l_eat1", 0, -1)
		print(result)


class TestSet(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def test_sadd(self):
		"""sadd"""
		l = ['adongwu', 'bhouzi', 'cff', 'dogg']
		# [b'dgg', b'cff', b'bwo', b'awo']
		rest = self.r.sadd("zoo1", *l)
		print(rest)
		r = self.r.smembers("zoo1")
		print(r)

	
	def test_srem(self):
		"""srem"""		
		rest = self.r.srem("zoo", "dogg")
		print(rest)
		r = self.r.smembers("zoo")
		print(r)


	def test_sinter(self):
		""" intersection"""		
		rest = self.r.sinter("zoo", "zoo1")
		print(rest)
		



def main():
	# str_obj = TestString()
	# str_obj.test_set()
	# str_obj.test_get()

	# str_obj.test_mset()
	# str_obj.test_mget()

	# str_obj.test_delete()

	# list_obj = TestList()
	# list_obj.test_push()
	# list_obj.test_pop()

	set_obj = TestSet()
	set_obj.test_sadd()
	set_obj.test_srem()
	set_obj.test_sinter()


if __name__ == '__main__':
	main()
```

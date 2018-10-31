  * [1 install and docs](#1-install-and-docs)
  * [2 redis 基础语法](#2-redis-基础语法)
  * [3 redis-py python 操作 redis](#3-redis-py-python-操作-redis)
  
### 1 install and docs

- [redis 安装配置](https://www.cnblogs.com/joyet/p/6103041.html)
- [redis 中文网](http://www.redis.cn/)
- [redis 中文网 redis 知识树](http://www.redis.cn/map.html)
- [github redis-py文档](https://github.com/andymccurdy/redis-py)
- [Welcome to redis-py’s documentation](https://redis-py.readthedocs.io/en/latest/)

### 2 redis 基础语法
string
```
set   设置值
get    获取值
mset   设置多个值
mget   获取多个值
append
del
incr/decr
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
sadd srem
sismember
smembers   打印集合中的成员
sdiff
sinter
sunion
```
hash
```

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

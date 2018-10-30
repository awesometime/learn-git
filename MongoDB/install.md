
### docs
```
https://api.mongodb.com/
https://api.mongodb.com/python/3.7.1/ 
```

### 安装

添加\bin到环境变量

在bin同级目录下新建data

cmd 中先执行   mongod --dbpath D:\MongoDB\data
 
另一cmd中执行  mongo

### mongo shell 实战
```
>>>use students
>>>db
students
清屏
>>>cls   
>>>db.students.find()
>>> db.students.insertMany(
... [{name : "lala", age : 13, gender : "male",   grade : 89},
... {name : "fsa",   age : 63, gender : "famale", grade : 9},
... {name : "fafla", age : 53, gender : "male",   grade : 68},
... {name : "vxzla", age : 33, gender : "male",   grade : 8},
... {name : "mfhla", age : 23, gender : "famale", grade : 89},
... {name : "yyua",  age : 43, gender : "male",   grade : 19},
... {name : "cngha", age : 11, gender : "famale", grade : 9},
... {name : "jmla",  age : 51, gender : "famale", grade : 79},
... {name : "zxla",  age : 31, gender : "male",   grade : 69},
... {name : "iya",   age : 11, gender : "male",   grade : 65},
... ])
>>>db.students.find()
>>>db.students.find({gender: "famale"})
>>>db.students.find({gender: "famale"}, {name:true, age:1, _id:0})

查询 grade >=60                 "le" --> "<="    "te" --> ">="     g get
>>>db.students.find({grade: {"$gte":60} }, {name:true, age:1, _id:0})

查询男性11岁和女性23岁
>>>db.students.find({"$or" : [{gender: "male", age : 11}, {gender: "famale", age : 23}]})   

查询，只显示name age gender
>>>db.students.find({"$or" : [{gender: "male", age : 11}, {gender: "famale", age : 23}]}, {name:1,age:1,gender:1,_id:0})

正序
>>>db.students.find().sort({age:1})

倒序
>>>db.students.find().sort({age:-1})

将 name : "yyua"  的内容更新
>>>db.students.update({name : "yyua"},{"$set": {address: "haidian"} })

{ }  只改第一条
>>>db.students.update({},{"$set": {address: "dahai"} })

{ }  multi 修改全部
>>>db.students.update({},{"$set": {address: "dahai"} },{multi:true})

全部 grade + 100
>>>db.students.update({},{"$inc": {grade: 100} },{multi:true})

```

### pymongo 

```python
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

class TestMongo(object):

	def __init__(self):
		self.client = MongoClient("mongodb://localhost:27017/")
		# print(dir(self.client))
		self.db = self.client["students"]
		#print(dir(self.db))
#['_BaseObject__codec_options', '_BaseObject__read_concern', '_BaseObject__read_preference', 
# '_BaseObject__write_concern', '_Database__client', '_Database__incoming_copying_manipulators', 
# '_Database__incoming_manipulators', '_Database__name', '_Database__outgoing_copying_manipulators', 
# '_Database__outgoing_manipulators', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', 
#  '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#   '__subclasshook__', '__weakref__', '_apply_incoming_copying_manipulators', '_apply_incoming_manipulators',
#    '_command', '_create_or_update_user', '_default_role', '_fix_incoming', '_fix_outgoing',
#     '_list_collections', '_read_preference_for', '_write_concern_for', 'add_son_manipulator', 'add_user',
#      'authenticate', 'client', 'codec_options', 'collection_names', 'command', 'create_collection', 
#      'current_op', 'dereference', 'drop_collection', 'error', 'eval', 'get_collection', 
#      'incoming_copying_manipulators', 'incoming_manipulators', 'last_status', 'list_collection_names', 
#      'list_collections', 'logout', 'name', 'next', 'outgoing_copying_manipulators', 'outgoing_manipulators',
#       'previous_error', 'profiling_info', 'profiling_level', 'read_concern', 'read_preference', 'remove_user', 
#       'reset_error_history', 'set_profiling_level', 'system_js', 'validate_collection', 'watch', 'write_concern']
	

	def add_one(self):
		"""新增数据"""
		post1 = {
		"name" : "hgg",
		"age" : "24",
		"gender" : "male",
		"create_at" : datetime.now()
		}
		#print(dir(self.db.students.insert_one(post1)))
		return self.db.students.insert_one(post1)


	def get_one(self):
		return self.db.students.find_one()


	def get_more(self):
		return self.db.students.find({"age" : 11})


	def get_one_from_objid(self, id):
		"""根据id查询指定数据"""
		obj = ObjectId(id)
		return self.db.students.find_one({"_id": obj})


	def update(self):
		"""修改数据"""
		# grade:189 有多条但只改一条
		# rest = self.db.students.update_one({"grade":189}, {'$inc':{"grade": 100}})  # 无multi用法, {multi:true})
		# return rest
		
		# grade:189 有多条 同时修改
		# rest = self.db.students.update_many({"grade":189}, {'$inc':{"grade": 100}})
		# return rest
		
		rest = self.db.students.update_many({}, {'$inc':{"grade": 100}})
		return rest


	def delete(self):
		"""删除一条数据"""
		#return self.db.students.delete_one({"name":"h"})
		"""删除多条数据"""
		return self.db.students.delete_many({"name":"hanmeimei"})

def main():
	obj = TestMongo()
	# result = obj.add_one()
	# print(result.inserted_id)
 
 #['_InsertOneResult__acknowledged', '_InsertOneResult__inserted_id', '_WriteResult__acknowledged',
 # '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
 # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', 
 # '__str__', '__subclasshook__', '_raise_if_unacknowledged', 'acknowledged', 'inserted_id']


	# result = obj.get_one()
	# print(type(result))  # dict
	# print(result)
	
	# result = obj.get_more()
	# print(type(result))  # <class 'pymongo.cursor.Cursor'>
	# print(result)        # <pymongo.cursor.Cursor object at 0x00000226C5ECC470>
	# for item in result:
	# 	print(item)

	# result = obj.get_one_from_objid("5bd7bfe5329ad8dbeb6acb64")
	# print(type(result))  # dict
	# print(result)
    
	# rest = obj.update()
	# print(rest.matched_count)
	# print(rest.modified_count)

	rest = obj.delete()
	print(rest.deleted_count)
	#print(rest.modified_count)


if __name__ == "__main__":
	main()
```

### MongoEngine   ODM   Object-Document Mapper

- [MongoEngine 文档](http://docs.mongoengine.org/)

```

```

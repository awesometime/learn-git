# 需要在 cmd 中
# ipython
# In [1]: from sql1 import Table2

# In [2]: from sql1 import engine

# In [3]: Table2.metadata.create_all(engine)



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pymysql


engine = create_engine('mysql+pymysql://用户名:密码@localhost:3306/数据库名')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Table2(Base):
	"""docstring for ClassName"""
	__tablename__ = "table2"      # table名
	id = Column(Integer, primary_key=True)
	name = Column(String(10), nullable=False)    #Column类创建一个字段
	age = Column(Integer, nullable=False)    
	gender = Column(String(5), )
	work = Column(String(10), )
    

class OrmTest(object):
	def __init__(self):
		self.session = Session()

	
	def add_one(self):
		"""新增一条记录"""
		new_obj = Table2(
            name = "wzw",
            age = "24",
            gender ="男",
            work = "student",
			)
		self.session.add(new_obj)
		self.session.commit()
		return new_obj


	def get_one(self):
		return self.session.query(Table2).get(1)


	def get_more(self):
		return self.session.query(Table2).filter_by(gender="男")


	def updata_data(self, id):
		"""修改单条数据"""
		new_obj = self.session.query(Table2).get(id)
		if new_obj:
			new_obj.name = "neinei"
			self.session.add(new_obj)
			self.session.commit()
			return True
		return False
    

	def updata_more_data(self):    
		# 修改多条数据
		data_list = self.session.query(Table2).filter_by(gender="男")
		for item in data_list:
		    item.name = "nei"
		    self.session.add(item)
		self.session.commit()
		return True


	def delete_data(self, id):
		new_obj = self.session.query(Table2).get(id)
		self.session.delete(new_obj)
		self.session.commit()


def main():
	obj = OrmTest()
	# result = obj.add_one()
	# print(result.id)

	# result = obj.get_one()
	# if result:
	#    print('name :{0} , age :{1}'.format(result.name, result.age))
	# else:
	#    print("not exist")

	# result = obj.get_more()
	# print(result.count())
	# for obj in result:
	# 	print('name :{0} , age :{1}'.format(obj.name, obj.age))

	# print(obj.updata_data(2))
	# print(obj.updata_more_data())
	
	obj.delete_data(3)


if __name__ == "__main__":
	main()

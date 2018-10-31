# [MongoEngine User Documentation](http://docs.mongoengine.org/)


from mongoengine import *

connect('students')   # 数据库名 students

GENDER_CHOICES = (
			('male', '男'),   # 写male  female 不能写 男女
    	    ('female', '女'),
        )


class Grade(EmbeddedDocument):
	"""成绩"""
	name = StringField(required=True)
	score = FloatField(required=True)


class Student(DynamicDocument):          # students.student 集合名
	gender = StringField(choices=GENDER_CHOICES, required=True)
	name = StringField(max_length=32, required=True)
	age = IntField(required=True)
	grade = FloatField()
	address = StringField()
	grades =ListField(EmbeddedDocumentField(Grade))
	# remark = StringField()

	meta = {
	"collections" : "students", # 指定集合为students (即students.students),若不指定则默认集合名为类名(class Student),即students.student 集合
	"ordering" : ['-age'],
	}


class TestMongoEngine(object):
	
	def add_one(self):
		"""增"""
		chinese = Grade(
			name='语文',
			score=90,
			)
		math = Grade(
			name='数学',
			score=100,
			)
		stu_obj = Student(
			name='yinyin',
			age=24,
			gender='female',
			grades=[chinese, math],
			)
		stu_obj.remark = 'remark'
		stu_obj.save()
		return stu_obj


	def query_one(self):
		return Student.objects.first()


	def query_more(self):
		return Student.objects.all()


	def query_from_objid(self, objid):
		return Student.objects.filter(pk=objid).first()
		
	
	def update(self):
		rest = Student.objects.filter(gender="male").update(inc__age=10)	
		# rest = Student.objects.filter(gender="male").update_one(inc__age=10)	
		return rest


	def delete(self):
		#return Student.objects.filter(gender="male").first().delete()
		return Student.objects.filter(gender="male").delete()


def main():
	obj = TestMongoEngine()
	# rest = obj.add_one()
	# print(rest.id)
	# print(rest.pk) # primary key
	
	# print(obj.query_one().id)
	# print(obj.query_one().name)

	# rows = obj.query_more()
	# for row in rows:
	# 	print(row.name)

	# rest = obj.query_from_objid("5bd813266627832074e24dc2")
	# if rest:	
	# 	print(rest.id)
	# 	print(rest.name)

	# rest = obj.update()
	# print(rest)


if __name__ =='__main__':
	main()

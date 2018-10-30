### 安装

添加\bin到环境变量

在bin同级目录下新建data

cmd 中先执行   mongod --dbpath D:\MongoDB\data
 
另一cmd中执行  mongo

### 实战
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

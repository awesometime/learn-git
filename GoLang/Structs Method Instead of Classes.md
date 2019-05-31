[ 结构体+方法  取代类](https://mp.weixin.qq.com/s/My1sXXRZS4vxCZPCmbmqPA)

employee.go

```py
package employee

import (  
    "fmt"
)

type employee struct {  
    firstName   string
    lastName    string
    totalLeaves int
    leavesTaken int
}

// New() function instead of constructors(Java)
func New(firstName string, lastName string, totalLeave int, leavesTaken int) employee {  
    e := employee {firstName, lastName, totalLeave, leavesTaken}
    return e
}

func (e employee) LeavesRemaining() {  
    fmt.Printf("%s %s has %d leaves remaining", e.firstName, e.lastName, (e.totalLeaves - e.leavesTaken))
}
```

main.go
```py
package main  

import "oop/employee"

func main() {  
    // 1
    e := employee.Employee {
            FirstName: "Sam",
            LastName: "Adolf",
            TotalLeaves: 30,
            LeavesTaken: 20,
        }
    
    // 2 New() function instead of constructors
    e := employee.New("Sam", "Adolf", 30, 20)
    e.LeavesRemaining()
}
```
```
为了新建一个合法的对象 使用New()

Go 并不支持构造器。如果某类型的零值不可用，需要程序员来隐藏该类型，避免从其他包直接访问。程序员应该提供一种
名为 NewT(parameters) 的 函数，按照要求来初始化 T 类型的变量。按照 Go 的惯例，应该把创建 T 类型变量的函数
命名为 NewT(parameters)。这就类似于构造器了。如果一个包只含有一种类型，按照 Go 的惯例，应该把函数命名为
New(parameters)， 而不是 NewT(parameters)。
```

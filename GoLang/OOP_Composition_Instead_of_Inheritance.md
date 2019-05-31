OOP_Composition_Instead_of_Inheritance.md

Composition by embedding structs Composition Instead of Inheritance - OOP in Go

[通过嵌套结构体进行组合  取代继承](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651435370&idx=1&sn=3cfb0b8a318c411e2a1b76066ce7aba8&chksm=80bb6f98b7cce68e5f24cb715de71b6455bf3871e41a59a773b75954d37ba74edbe35795392c&mpshare=1&scene=1&srcid=0529Y1iJ7aMjhlvW8BO6psjR&from=singlemessage&ascene=1&devicetype=android-28&version=2700043b&nettype=WIFI&abtest_cookie=BAABAAoACwASABMABgAjlx4AVpkeAL%2BZHgDcmR4A9ZkeAAOaHgAAAA%3D%3D&lang=zh_CN&pass_ticket=6NFrC%2BvqM1C%2Bzqy8DJVTshi3ylnKB54NSQOWmYt8atUz7rO%2BMkZjXfrQn6%2FoUc%2Be&wx_header=1)

```go
package main

import (  
    "fmt"
)

type author struct {  
    firstName string
    lastName  string
    bio       string
}

func (a author) fullName() string {  
    return fmt.Sprintf("%s %s", a.firstName, a.lastName)
}

type post struct {  
    title   string
    content string
    author
}

func (p post) details() {  
    fmt.Println("Title: ", p.title)
    fmt.Println("Content: ", p.content)
    fmt.Println("Author: ", p.fullName())
    fmt.Println("Bio: ", p.bio)
}

// Embedding slice of structs   结构体切片的嵌套
type website struct {  
 posts []post
}

func (w website) contents() {  
    fmt.Println("Contents of Website\n")
    for _, v := range w.posts {
        v.details()
        fmt.Println()
    }
}

func main() {  
    author1 := author{
        "Naveen",
        "Ramanathan",
        "Golang Enthusiast",
    }
    
    post1 := post{
        "Inheritance in Go",
        "Go supports composition instead of inheritance",
        author1,
    }
    
    post2 := post{
        "Struct instead of Classes in Go",
        "Go does not support classes but methods can be added to structs",
        author1,
    }
    
    post3 := post{
        "Concurrency",
        "Go is a concurrent language and not a parallel one",
        author1,
    }
    
    w := website{
        posts: []post{post1, post2, post3},
    }
    
    w.contents()
}
```

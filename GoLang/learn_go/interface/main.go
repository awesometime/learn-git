/*
接口  实现者：只要实现Get方法即可     调用者download
func download(r Retriever) string {
	return r.Get(url)
}


接口变量里有什么 T v
实现者的类型;实现者的值
或者说是实现者的类型;实现者的指针 -->指向实现者

查看接口变量的类型  https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/11.4.md
fmt.Printf("%T %v\n", r, r)
Type assertion
Type-switch

任何类型
interface{}
*/

package main

import (
	"fmt"

	"time"

	"awesomeProject/interface/mock"
	"awesomeProject/interface/real"
)

type Retriever interface {
	Get(url string) string
}

type Poster interface {
	Post(url string,
		form map[string]string) string
}

// 接口的组合
type RetrieverPoster interface {
	Retriever
	Poster
}

const url = "http://www.imooc.com"

// 函数
func download(r Retriever) string {
	return r.Get(url)
}

func post(poster Poster) {
	poster.Post(url,
		map[string]string{
			"name":   "ccmouse",
			"course": "golang",
		})
}

func session(s RetrieverPoster) string {
	s.Post(url, map[string]string{
		"contents": "another faked imooc.com",
	})
	return s.Get(url)
}

func main() {
	var r Retriever  // 接口变量

	mockRetriever := mock.Retriever{
		Contents: "this is a fake imooc.com"}
	r = &mockRetriever
	fmt.Printf("%T %v\n", r, r)
	// *mock.Retriever Retriever: {Contents=this is a fake imooc.com}
	inspect(r)

	r = &real.Retriever{
		UserAgent: "Mozilla/5.0",
		TimeOut:   time.Minute,
	}
	fmt.Printf("%T %v\n", r, r)
	// *real.Retriever &{Mozilla/5.0 1m0s}
	inspect(r)

	//fmt.Println(download(r))

	// Type assertion 【r.(*mock.Retriever)】
	// 测试一个struct的值mock.Retriever  是否实现了某个接口r Retriever
	if mockRetriever, ok := r.(*mock.Retriever); ok {
		fmt.Println(mockRetriever.Contents)
	} else {
		fmt.Println("r is not a mock Retriever")
	}

	fmt.Println(
		"Try a session with mockRetriever")
	fmt.Println(session(&mockRetriever))
}

func inspect(r Retriever) {
	fmt.Println("Inspecting", r)
	fmt.Printf(" > Type:%T Value:%v\n", r, r)
	fmt.Print(" > Type switch: ")
	switch v := r.(type) {       //【r.(type)】
	case *mock.Retriever:
		fmt.Println("Contents:", v.Contents)
	case *real.Retriever:
		fmt.Println("UserAgent:", v.UserAgent)
	}
	fmt.Println()
}


/*
interface{}
空接口里面没有方法，所以它也不具有任何能力，其作用相当于 Java 的 Object 类型，可以容纳任意对象，它是一个万能容器。
比如一个字典的 key 是字符串，但是希望 value 可以容纳任意类型的对象，
类似于 Java 语言的 Map 类型，这时候就可以使用空接口类型 interface{}。

package main

import "fmt"

func main() {
    // 连续两个大括号，是不是看起来很别扭
    var user = map[string]interface{}{
        "age": 30,
        "address": "Beijing Tongzhou",
        "married": true,
    }
    fmt.Println(user)
    // 类型转换语法来了
    var age = user["age"].(int)
    var address = user["address"].(string)
    var married = user["married"].(bool)
    fmt.Println(age, address, married)
}

-------------
map[age:30 address:Beijing Tongzhou married:true]
30 Beijing Tongzhou true
*/

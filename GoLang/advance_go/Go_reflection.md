[reflect包](https://www.cnblogs.com/golove/p/5909541.html)

反射和接口的关系

[Go Blog的一篇文章《The law of reflection》](https://blog.golang.org/laws-of-reflection)

[大彬LIB  Go高级实践：反射3定律](http://lessisbetter.site/2019/02/24/go-law-of-reflect/)

[掘金 图解反射](https://juejin.im/post/5d27f572e51d4550bf1ae900)

[![pic](https://user-gold-cdn.xitu.io/2019/7/12/16be416ecd20d1ef?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)](https://user-gold-cdn.xitu.io/2019/7/12/16be416ecd20d1ef?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

```go
package main

import (
	"fmt"
	"reflect"
)

func main() {

	x := 10
	v1 := reflect.ValueOf(x)
	fmt.Println("setable:", v1.CanSet())
	fmt.Println("v1:", v1)

	p := reflect.ValueOf(&x)
	fmt.Println(p)
	fmt.Println("p:", p)
	fmt.Printf("p: %T", p)
	fmt.Println("setable:", p.CanSet())

	v2 := p.Elem()
	fmt.Println(v2)
	fmt.Println("setable:", v2.CanSet())

}

setable: false
v1: 10
0xc000080000
p: 0xc000080000
p: reflect.Valuesetable: false
10
setable: true


```
反射三定律
```go
1  Reflection goes from interface value to reflection object.
// 获取某个变量的值，但值是通过reflect.Value对象描述的。
reflect.ValueOf({}interface) reflect.Value

// 获取某个变量的静态类型，但值是通过reflect.Type对象描述的，是可以直接使用Println打印的
reflect.TypeOf({}interface) reflect.Type

// 获取变量值的底层类型（类别），注意不是类型，是Int、Float，还是Struct，还是Slice
reflect.Value.Kind() Kind

// 获取变量值的类型，效果等同于reflect.TypeOf
reflect.Value.Type() reflect.Type



2  Reflection goes from reflection object to interface value.
func (v Value) Interface() (i interface{})



3  To modify a reflection object, the value must be settable.

```

reflct 包函数 

Elem

Value


```go
package main

import (
	"fmt"
	"reflect"
	"strings"
)

var testRawString = "HOST;000012000629948340196501;ipv4;3; ips: user_id=2;user_name=172.21.1.102;policy_id=1;src_mac=52:54:00:62:7f:4a;dst_mac=58:69:6c:7b:fa:e7;src_ip=172.21.1.102;dst_ip=172.22.2.3;src_port=48612;dst_port=80;app_name=网页浏览(HTTP);protocol=TCP;app_protocol=HTTP;event_id=1311495;event_name=HTTP_Nikto_WEB漏洞扫描;event_type=安全扫描;level=warning;ctime=2019-12-26 11:17:17;action=pass"

type IpsItem struct {
	UserId      int    `json:"user_id"`
	UserName    string `json:"user_name"`
	SrcIp       string `json:"src_ip"`
	DstIp       string `json:"dst_ip"`
	SrcPort     int    `json:"src_port"`
	DstPort     int    `json:"dst_port"`
	AppName     string `json:"app_name"`
	Protocol    string `json:"protocol"`
	AppProtocol string `json:"app_protocol"`
	EventId     int    `json:"event_id"`
	EventName   string `json:"event_name"`
	EventType   string `json:"event_type"`
	Level       string `json:"level"`
	Ctime       string `json:"ctime"`
	Action      string `json:"action"`
}

func NewIpsItem(raw string) *IpsItem {
	//清除非法的字符
	raw = strings.ReplaceAll(raw, ":", ";")

	ins := IpsItem{}
	t := reflect.TypeOf(ins)
	//遍历结构体属性
	for i := 0; i < t.NumField(); i++ {
		//获取属性structField
		sf := t.Field(i)
		//属性名称
		fieldName := sf.Name
		//tag json的值
		tagName := sf.Tag.Get("json")

		//获取字段值
		fieldValue := reflect.ValueOf(&ins).Elem().FieldByName(fieldName)

		//属性的值 type
		switch sf.Type.Name() {
		case "int":
			var someInt int64
			scanValueFromString(raw, tagName, tagName+"=%d", &someInt)
			//给属性赋值
			fieldValue.SetInt(someInt)
			//todo:: 支持更多类型
		default:
			var someString string
			scanValueFromString(raw, tagName, tagName+"=%s", &someString)
			////给属性赋值
			fieldValue.SetString(someString)
		}

	}
	return &ins
}

//scanValueFromString 字符串 字段的值
func scanValueFromString(raw string, tagJsonValue, format string, someV interface{}) {
	for _, ss := range strings.Split(raw, ";") {
		ele := strings.TrimSpace(ss)
		if strings.HasPrefix(ele, tagJsonValue) {
			fmt.Sscanf(ele, format, someV)
			//n, err := fmt.Sscanf(ele, format, someV)
			//fmt.Println(n, err)
			return
		}
	}
}

func main() {
	ii := NewIpsItem(testRawString)
	fmt.Printf("%+v\n", ii)
}

```

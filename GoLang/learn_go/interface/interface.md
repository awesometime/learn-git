Go只有封装

> 用接口来实现多态
```go
type Fruitable interface {
    eat()
}

type Fruit struct {
    Name string  // 属性变量
    Fruitable  // 匿名内嵌接口变量
}

// 通过组合属性变量（Name）和接口变量（Fruitable）来模拟多态，
// 属性变量是对象的数据，而接口变量是对象的功能，将它们组合到一块就形成了一个完整的多态性的结构体。
```

> 接口的组合实现继承

```go
type Smellable interface {
  smell()
}

type Eatable interface {
  eat()
}

type Fruitable interface {
  Smellable
  Eatable
}
```

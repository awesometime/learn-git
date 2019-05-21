/*
每个目录一个package
main包包含可执行入口
*/

package struct_method_test

import "fmt"

/*
值接收者 VS 指针接收者

要改变内容必须使用指针接收者;  值接收者是一个拷贝改不了原数据
结构体过大也考虑使用指针接收者,结构体过大时拷贝开销过大

值接收者,是go语言特有; 指针接收者,如self，this
值/指针接收者均可接收值/指针
*/

type treeNode struct {
	Value       int
	Left, Right *treeNode   // 递归结构体 链表 树
}

// 使用指针作为方法接受收者
// 只有使用指针才可以改变结构体内容
func (node *treeNode) SetValue(value int) {
	if node == nil {
		fmt.Println("Setting Value to nil " +
			"node. Ignored.")
		return
	}
	node.Value = value
}

// 为结构定义方法,值作为方法的接收者
// 这时候传入node时传入的是node的**拷贝**,所以即使改变node的值,改变的是node的拷贝,原来node并不变
func (node treeNode) Print() {
	fmt.Print(node.Value, " ")
}

func (node *treeNode) Traverse() {
	if node == nil {
		return
	}
	node.Left.Traverse()
	node.Print()
	node.Right.Traverse()
}

// *type 表明这是一个地址类型  var p *int = &value
// *p是一个int值
// 工厂方法创建结构体实例
func myCreateNode(value int) *treeNode {
	return &treeNode{Value: value}
	// 返回了局部变量的地址  堆上分配
}

func ExampleCreateNode() {
	// 构造 treeNode的方法1-struct as a value type:
	var root treeNode
	root = treeNode{Value: 3}
	// 3—struct as a literal 字面量
	root.Left = &treeNode{}
	root.Right = &treeNode{5, nil, nil}
	// 2—struct as a pointer;
	// new(treeNode) 返回一个指向treeNode类型的指针
	root.Right.Left = new(treeNode)
	// 4-工厂方法创建结构体实例
	root.Left.Right = myCreateNode(2)

	nodes := []treeNode{
		{Value: 3},
		{},
		{6, nil, &root},
	}

	root.Right.Left.SetValue(4)
	root.Right.Left.Print()

	root.Print()
	root.SetValue(100)
	fmt.Println(nodes)

	pRoot := &root
	pRoot.SetValue(500)
	pRoot.Print()

	var nRoot *treeNode
	nRoot.SetValue(200) //验证nil.SetValue   但是nil.value不能执行
	nRoot = &root
	nRoot.SetValue(99)
	nRoot.Print()
}

package main

import "fmt"

type Node struct {
	Value       int
	Left, Right *Node
}

type myTreeNode struct {
	node *Node
}

func (node Node) Print() {
	fmt.Print(node.Value, " ")
}

func (node *Node) SetValue(value int) {
	if node == nil {
		fmt.Println("Setting Value to nil " +
			"node. Ignored.")
		return
	}
	node.Value = value
}

func CreateNode(value int) *Node {
	return &Node{Value: value}
}

func (myNode *myTreeNode) postOrder() {
	if myNode == nil || myNode.node == nil {
		return
	}
	// 构造新建 myTreeNode
	left := myTreeNode{myNode.node.Left}
	right := myTreeNode{myNode.node.Right}

	left.postOrder()
	right.postOrder()
	myNode.node.Print()
}

// 1 最基础的树的遍历
func (node *Node) BaseTraverse() {
	if node == nil {
		return
	}
	node.Left.BaseTraverse()
	node.Print()
	node.Right.BaseTraverse()
}

// 2 函数式编程 闭包
// 定义TraverseFunc  指明该函数需要一个func(*Node)的参数
// 具体func(*Node)的逻辑在调用时有调用者根据自己的需要决定
func (node *Node) TraverseFunc(f func(*Node)) {
	if node == nil {
		return
	}

	node.Left.TraverseFunc(f)
	f(node)              // 可以定制方法逻辑 比较灵活
	node.Right.TraverseFunc(f)
}

func (node *Node) Traverse() {
	node.TraverseFunc(func(n *Node) {
		n.Print()
	})
	fmt.Println()
}

// 3 通过channel遍历树  实现类似python yield的功能
func (node *Node) TraverseWithChannel() chan *Node {
	out := make(chan *Node)
	go func() {
		node.TraverseFunc(func(node *Node) {
			out <- node
		})
		close(out)
	}()
	return out
}

func main() {
	var root Node

	root = Node{Value: 3}
	root.Left = &Node{}
	root.Right = &Node{5, nil, nil}
	root.Right.Left = new(Node)
	root.Left.Right = CreateNode(2)
	root.Right.Left.SetValue(4)

	fmt.Print("In-order traversal: ")
	root.Traverse()

	fmt.Print("My own post-order traversal: ")
	myRoot := myTreeNode{&root}
	myRoot.postOrder()
	fmt.Println()

	fmt.Print("1 base traversal: ")
	root.BaseTraverse()
	
	fmt.Print("2 traversal functional: ")
	nodeCount := 0
	root.TraverseFunc(func(node *Node) {
		nodeCount++
	})
	fmt.Println("Node count:", nodeCount)

	fmt.Println("3 Traverse tree with Channel:")
	c := root.TraverseWithChannel()
	maxNodeValue := 0
	for node := range c {
		if node.Value > maxNodeValue {
			maxNodeValue = node.Value
		}
	}
	fmt.Println("Max node value:", maxNodeValue)
}


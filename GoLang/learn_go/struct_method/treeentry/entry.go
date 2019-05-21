package main

import (
	"fmt"

	"awesomeProject/struct_method"
)

// 扩充系统类型或者别人的类型
// 1 定义别名
// 2 使用组合

//使用组合
type myTreeNode struct {
	node *struct_method.Node
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

func main() {
	var root struct_method.Node

	root = struct_method.Node{Value: 3}
	root.Left = &struct_method.Node{}
	root.Right = &struct_method.Node{5, nil, nil}
	root.Right.Left = new(struct_method.Node)
	root.Left.Right = struct_method.CreateNode(2)
	root.Right.Left.SetValue(4)

	fmt.Print("In-order traversal: ")
	root.Traverse()

	fmt.Print("My own post-order traversal: ")
	myRoot := myTreeNode{&root}
	myRoot.postOrder()
	fmt.Println()

	nodeCount := 0
	root.TraverseFunc(func(node *struct_method.Node) {
		nodeCount++
	})
	fmt.Println("Node count:", nodeCount)

	c := root.TraverseWithChannel()
	maxNodeValue := 0
	for node := range c {
		if node.Value > maxNodeValue {
			maxNodeValue = node.Value
		}
	}
	fmt.Println("Max node value:", maxNodeValue)
}


//In-order traversal: 0 2 3 4 5
//My own post-order traversal: 2 0 4 5 3
//Node count: 5
//Max node value: 5
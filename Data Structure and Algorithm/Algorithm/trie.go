package gee

import (
	"fmt"
	"strings"
)

// https://geektutu.com/post/gee-day3.html
// 前缀树路由
// web路由查找匹配

type node struct {
	pattern  string  // 待匹配路由，例如 /hello/:lang, 最后一层节点才会设置该值
	part     string  // 路由中的一部分,两个//中间的部分,例如 hello,:lang
	children []*node // 子节点，例如 [doc, tutorial, intro]
	isWild   bool    // 是否精确匹配，part 含有 : 或 * 时为true
}

func (n *node) String() string {
	return fmt.Sprintf("node{pattern=%s, part=%s, isWild=%t}", n.pattern, n.part, n.isWild)
}

func (n *node) insert(pattern string, parts []string, height int) {
	// 递归结束条件
	if len(parts) == height {
		// 最后一层节点 pattern才会设置
		n.pattern = pattern
		return
	}
	// pattern /hello/b/c
	// parts [hello,b,c]
	part := parts[height]
	child := n.matchChild(part) // child *node
	if child == nil {
		child = &node{part: part, isWild: part[0] == ':' || part[0] == '*'}
		n.children = append(n.children, child)
	}
	// 递归
	child.insert(pattern, parts, height+1)
}

// 第一个匹配成功的节点，用于插入
func (n *node) matchChild(part string) *node {
	for _, child := range n.children {
		if child.part == part || child.isWild {
			return child
		}
	}
	return nil
}

func (n *node) search(parts []string, height int) *node {
	if len(parts) == height || strings.HasPrefix(n.part, "*") {
		if n.pattern == "" {
			return nil
		}
		return n
	}

	part := parts[height]
	children := n.matchChildren(part)

	for _, child := range children {
		// 递归
		result := child.search(parts, height+1)
		if result != nil {
			return result
		}
	}

	return nil
}

// 所有匹配成功的节点，用于查找
func (n *node) matchChildren(part string) []*node {
	nodes := make([]*node, 0)
	for _, child := range n.children {
		if child.part == part || child.isWild {
			nodes = append(nodes, child)
		}
	}
	return nodes
}

func (n *node) travel(list *([]*node)) {
	if n.pattern != "" {
		*list = append(*list, n)
	}
	for _, child := range n.children {
		child.travel(list)
	}
}

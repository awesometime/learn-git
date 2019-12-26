package main

import (
	"fmt"
	"sync"
	"time"
)


func main() {
	a:=1
	m:=sync.Mutex{}
	for i:=0;i<3;i++{
		go func() {
			m.Lock()
			a+=a
			m.Unlock()
			fmt.Print(a)
		}()
	}
	time.Sleep(time.Second)

}
// 248

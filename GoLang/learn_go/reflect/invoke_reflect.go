package main


import "fmt"
import "reflect"

func main() {
	//var s int = 42
	//var x float64 = 3.4
	//fmt.Println(reflect.TypeOf(s))
	//fmt.Println(reflect.ValueOf(s))
	//fmt.Println(reflect.TypeOf(x))
	//fmt.Println(reflect.ValueOf(x))
	//type MyInt int
	//var m MyInt = 5
	//v := reflect.ValueOf(m)
	//fmt.Println(v)

	var x float64 = 3.4
	fmt.Println("type:", reflect.TypeOf(x))
	v := reflect.ValueOf(x)
	fmt.Println("value:", v)
	fmt.Println("type:", v.Type())
	fmt.Println("kind:", v.Kind())
	fmt.Println("value:", v.Float())
	fmt.Println(v.Interface())
	fmt.Printf("value is %5.2e\n", v.Interface())
	y := v.Interface().(float64)
	fmt.Println(y)
}


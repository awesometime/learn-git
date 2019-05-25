// https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/11.14.md#1114-%E7%BB%93%E6%9E%84%E4%BD%93%E9%9B%86%E5%90%88%E5%92%8C%E9%AB%98%E9%98%B6%E5%87%BD%E6%95%B0
// 结构体、集合和高阶函数
package main

import (
	"fmt"
)

type Any interface{}
type Car struct {
	Model        string
	Manufacturer string
	BuildYear    int
	// ...
}
type Cars []*Car

func main() {
	// make some cars:
	ford := &Car{"Fiesta", "Ford", 2008}
	bmw := &Car{"XL 450", "BMW", 2011}
	merc := &Car{"D600", "Mercedes", 2009}
	bmw2 := &Car{"X 800", "BMW", 2008}
	
  
  // query:
	allCars := Cars([]*Car{ford, bmw, merc, bmw2})
	allNewBMWs := allCars.FindAll(
		func(car *Car) bool {
			return (car.Manufacturer == "BMW") && (car.BuildYear > 2010)
		})
	fmt.Println("AllCars: ", allCars)
	fmt.Println("New BMWs: ", allNewBMWs)
	
  
  //
	manufacturers := []string{"Ford", "Aston Martin", "Land Rover", "BMW", "Jaguar"}
	sortedAppender, sortedCars := MakeSortedAppender(manufacturers)
	allCars.Process(sortedAppender)
	fmt.Println("Map sortedCars: ", sortedCars)
	BMWCount := len(sortedCars["BMW"])
	fmt.Println("We have ", BMWCount, " BMWs")
}


// Process all cars with the given function f:
func (cs Cars) Process(fy func(car *Car)) {
	for _, c := range cs {
		fy(c) //fy 这个函数具体是干嘛呢 需要在调用它的地方才知道 也就是cs.Process这个地方 line50
		/*
			fy(c)=      // FindAll方法中的
			func(c *Car) {
					if fr(c) {
						cars = append(cars, c)
					}
				}
		*/
	}
}


// Find all cars matching a given criteria.
func (cs Cars) FindAll(fr func(car *Car) bool) Cars {
	cars := make([]*Car, 0) // =python  cars=[]

	cs.Process(func(c *Car) {
		if fr(c) { //fr 这个函数具体是干嘛呢 需要在调用它的地方才知道 也就是 allCars.FindAll这个地方 line24
			cars = append(cars, c)
		}
	})
	/*
		fr(c)=
		func(car *Car) bool {
				return (car.Manufacturer == "BMW") && (car.BuildYear > 2010)}
	*/
	return cars
}


// 执行顺序
// allCars.FindAll  --> cs.Process  --> Process --> fy(c) --> cs.Process --> fr(c) --> func(car *Car) bool line25


// Process cars and create new data.   没用到Map
func (cs Cars) Map(fg func(car *Car) Any) []Any {
	result := make([]Any, len(cs))   // []  nil
	ix := 0
	cs.Process(func(c *Car) {
		result[ix] = fg(c)
		ix++
	})
	return result
}


func MakeSortedAppender(manufacturers []string) (func(car *Car), map[string]Cars) {
	// Prepare maps of sorted cars.
	sortedCars := make(map[string]Cars)   // 初始化map[]
	fmt.Println(sortedCars)

	for _, m := range manufacturers {
		sortedCars[m] = make([]*Car, 0)
		fmt.Println(sortedCars)

	}
	sortedCars["Default"] = make([]*Car, 0)

	// Prepare appender function:
	appender := func(c *Car) {
		if _, ok := sortedCars[c.Manufacturer]; ok {
			sortedCars[c.Manufacturer] = append(sortedCars[c.Manufacturer], c)
		} else {
			sortedCars["Default"] = append(sortedCars["Default"], c)
		}
	}
	return appender, sortedCars
}


//AllCars:  [0xc000068300 0xc000068330 0xc000068360 0xc000068390]
//New BMWs:  [0xc000068330]
//map[]
//map[Ford:[]]
//map[Aston Martin:[] Ford:[]]
//map[Aston Martin:[] Ford:[] Land Rover:[]]
//map[Aston Martin:[] BMW:[] Ford:[] Land Rover:[]]
//map[Aston Martin:[] BMW:[] Ford:[] Jaguar:[] Land Rover:[]]
//Map sortedCars:  map[Aston Martin:[] BMW:[0xc000068330 0xc000068390] Default:[0xc000068360] Ford:[0xc000068300] Jaguar:[] Land Rover:[]]
//We have  2  BMWs

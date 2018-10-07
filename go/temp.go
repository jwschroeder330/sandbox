// temp.go
package main

// it is a compile error to import something
// but not use it
import (
	"fmt"
	"log"
	"math"
)

// visible to other pakages: capitalized
const English = "Welcome"
const German = "Wilkommen"

// not visible to other packages: lowercase
const spanish = "Hola"

// visible anywhere in main package
var myNumber = 1.23

func main() {
	roundedUp := math.Ceil(myNumber)
	roundedDown := math.Floor(myNumber)
	fmt.Println(roundedUp, roundedDown)
	var a, b int
	a, b = 1, 2
	c := 4
	// type can be inferred
	var d = 5
	// most common way of assigning variables
	e := 6
	// same as
	var f int = 6
	// we are required to use every variable!
	fmt.Println(a, b, c, d, e, f)
	// it is possible to use blocks by themselves
	{
		var g = "hey"
		fmt.Println(g)
	}
	myFunction()
	sum := add(4, 8)
	difference := difference(9, 2)
	fmt.Println(sum, difference)
	// call square root, check for errors
	squareRoot, err := squareRoot(9)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(squareRoot)
	// note, use _ to ignore error
	// will cause a panic if the error is not nil
}

func myFunction() string {
	return "return"
}

func add(a float64, b float64) (sum float64) {
	sum = a + b
	return
}

func difference(a, b float64) (difference float64) {
	difference = a - b
	return
}

func squareRoot(x float64) (float64, error) {
	if x < 0 {
		return 0, fmt.Errorf("Can't take square root of negative number")
	}
	return math.Sqrt(x), nil
}

// temp_ii
package main

import (
	"fmt"
)

// for loop example
func main() {
	// accessible inside and outside loop
	beforeLoop := 888
	for i := 1; i <= 3; i++ {
		// accessible only within loop
		inLoop := 999
		fmt.Println(i)
		fmt.Println(inLoop)
	}
	fmt.Println(beforeLoop)
	// fmt.Println(i) = Error
	// fmt.Println(inLoop) = Error

	// if examples
	if !true {
		fmt.Println("This code will not be run")
	}
	if !false {
		fmt.Println("This code will run")
	}
	if true && false {
		fmt.Println("This entire expression is false")
	}
	if true && true {
		fmt.Println("This will run")
	}
	if true || false {
		fmt.Println("Will run, no need to worry about false.")
	}
	if true || true {
		fmt.Println("Only needed one of these to be true")
	}
	if true {
		fmt.Println("if")
	} else if {
		fmt.Println("else if")
	} else {
		fmt.Println("else")
	}
	// Note: variables defined within the 
	// if block scope, are limited to that scope 
	// and cannot be accessed outside it
	
	// switch statement example
	doorNumber := 2
	switch doorNumber {
		// only the selected case runs by default
		// however fallthrough lets you run multiple case
		case 1:
			fmt.Println("a new car!")
			fallthrough  // example of fallthrough usage
		case 2:
			fmt.Println("a boat!")
		case 3: 
			fmt.Println("a house!")
		default:
			fmt.Println("nothing!")
	}
}
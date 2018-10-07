// temp_iii
package main

import (
	"fmt"
)

func main() {
	var aValue float64 = 1.23
	// pointer assigns aValue to pointer
	// like byRef in VBA
	var aPointer *float64 = &aValue
	fmt.Println("The actual value of the pointer itself:")
	fmt.Println("aPointer:", aPointer)
	fmt.Println("The value the pointer is pointing to")
	fmt.Println("*aPointer:", *aPointer)

	// examples where the functions have to affect their arguments
	// don't want to alter a copy of the argument!
	myNumber := 2.6
	halve(&myNumber) // pass the address of myNumber to halve
	fmt.Println("myNumber is ", myNumber)

	// arrays and slices example
	// slices are built on top of arrays
	var months [3]string // number represents size, and type
	months[0] = "Apr"
	months[1] = "Apr"
	months[2] = "Apr"
	var salesByMonth [3]float64
	salesByMonth[0] = 1719.32
	salesByMonth[1] = 2233.43
	salesByMonth[2] = 5653.98
	fmt.Println(months[0], salesByMonth[0])
	fmt.Println(months[1], salesByMonth[1])
	fmt.Println(months[2], salesByMonth[2])

	// same as above, just more efficient
	// need to know values beforehand
	newMonths := [3]string{"Apr", "May", "Jun"}
	newSalesByMonth := [3]float64{2342.32, 234524.43, 234523.34}
	for i := 0; i < len(months); i++ {
		fmt.Println(newMonths[i], newSalesByMonth[i])
	}

	// range examples, like for each
	// often safer
	for i, month := range months {
		fmt.Println(month, salesByMonth[i])
	}
	// example, omitting index if not needed
	for _, month := range months {
		fmt.Println(month)
	}
	// length of arrays is fixed
	// hence, why slices are often used instead
	a := [5]int{0, 1, 2, 3, 4}
	s1 := a[0:3]
	s2 := a[2:]
	fmt.Println(a, s1, s2)

	// length of a slice
	fmt.Println(len(s1))
	// capacity: number of elements between
	// start of slice and end of the original array
	// original array is a in this case
	fmt.Println(cap(s1))
	s1 = append(s1, 5) // append 5 to end of s1
	fmt.Println(s1)
	fmt.Println(cap(s1))

	// changes to slices can be risky
	// if the slice append yields a new
	// array, then the other slices and
	// original array will not be affected
	// by new value assignments as they
	// normally would

	// best way to create list of item in go
	sEmpty := []int{}   // example with no preset values
	s := []int{1, 2, 3} // example with preset values
	s = append(s, 4, 5)
	s = append(s, 6, 7, 8)
	fmt.Println(sEmpty, s)
	// using a for range loop with a slice
	for x, y := range s {
		fmt.Println("element:", x, "value:", y)
	}
	fmt.Println(NobleGases())

	// maps - like dictionaries in pyton
	// and objects in javascript
	// * map keys must all be the same type
	ages := map[string]float64{}
	ages["Jake"] = 24
	fmt.Println(ages["Jake"])
	for name, age := range ages {
		fmt.Println(name, age)
	}
	// prepopulated example
	newAges := map[string]float64{
		"John":  12,
		"Alice": 36,
	}
	for _, age := range newAges {
		fmt.Println(age)
	}
}
func NobleGases() []string {
	return []string{"He", "Ne", "Ar", "Kr", "Xe", "Rn"}
}

// accept a pointer, rather than a value
func halve(number *float64) {
	// work with the value by address
	// rather than a copy of the value
	*number = *number / 2
}

#!/bin/bash

echo "This program enables and disables a function"


testFn(){

	echo "========================="
	echo "From inside test function"
	echo "========================="

	echo "First argument is " $1
	echo "Second argument is " $2
	echo "Number of arguments is " $#
}


# Calling up function
testFn 2 3

# Disable the function, unsets permanently, can't be called back
unset testFn

# Calling again to check if its working
testFn


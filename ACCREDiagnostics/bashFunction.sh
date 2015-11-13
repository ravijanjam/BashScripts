#!/bin/bash

testFn(){

	echo "From inside test function"
}


# Calling up function
testFn

# Disable the function, unsets permanently, can't be called back
unset testFn

# Calling again to check if its working
testFn


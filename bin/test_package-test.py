"""Test package-test file
"""
from package-test import *

__author__ = "help@castellanidavide.it"
__version__ = "2.0 2020-11-29"

def test():
	"""Tests the package-test function in the package-test class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert package-test.test(), "test failed"
	#assert package-test.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()

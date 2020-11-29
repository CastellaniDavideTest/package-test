"""package-test
"""
from flask import Flask
server = Flask(__name__)

__author__ = "help@castellanidavide.it"
__version__ = "2.0 2020-11-29"

class package-test:
	def __init__ (self):
		"""Where it all begins
		"""
		print(package-test.package-test())
	
	@server.route("/")
	def package-test():
		"""package-test first funtion
		"""
		return "This is the output by package-test project." #for the test (see test_package-test.py)

	def test():
		return True

if __name__ == "__main__":
	server.run(host='0.0.0.0')

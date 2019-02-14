from flask import Flask, jsonify
import re

import config #Local config file

app = Flask(__name__)

# Simplest form from stack overflow
def recursion_fib(n):
	#Recursive function to print Fibonacci sequence"""
	if n <= 1:
		return n
	else:
		return(recursion_fib(n-1) + recursion_fib(n-2))

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/numbers/<input>') #Using string format instead of int here - to be able to accept everything: numers, negatives and other stuff (to match the Flask route)
def api(input):
	#Check the input for numbers with optional minus in the beginning
	if re.match(r"^-?\d+$", input):
		#Make an integer to work with
		limit = int(input)
		#Check expected lenght of the list according to config
		if(limit > config.MAX_LIST_LENGTH):
			return jsonify({"warning":"Sorry - you are requesting too much horsepower from a minimal VPS:) Please expect %d Fibonacci numbers max" % config.MAX_LIST_LENGTH})
		elif(limit > 0):
			#Prepare result
			result = []
			#Calculate numbers and push to result set
			for i in range(limit):
				result.append(recursion_fib(i))
			return jsonify(result)
		else:
			return jsonify({"error":"Invalid value - please pass a possitive number"})
	else:
		return jsonify({"error":"Invalid value - please pass a number"})
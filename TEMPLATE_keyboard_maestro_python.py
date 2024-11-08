#!/usr/bin/env python
import os
import sys

def example():
	# access local, global, and instance variables
	example_variable = str(os.environ["KMVAR_Variable_Name"]) 
	
	# access the input text from the Keyboard Maestro action
	input_text = sys.stdin.read()

	with open(os.path.expanduser("~/Downloads/TEST.txt"), "x") as f:
		f.write(example_variable + "\n")
		f.write(input_text)

example()

# Execute the following from an "Execute Shell Script" action in Keyboard Maestro
# with input from text to pass multiple variables
# $(which python) /Users/USER/Downloads/keyboard_maestro_python_example.py








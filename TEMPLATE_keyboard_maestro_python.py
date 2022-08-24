#!/usr/bin/env python3
import os

def example():
	example_variable = str(os.environ["KMVAR_Variable_Name"])

	with open("/Users/USER/Downloads/TEST.txt", "x") as f:
		f.write(example_variable)

example()

# Execute the following from an "Execute Shell Script" action in Keyboard Maestro
# with input from text to pass multiple variables
# $(which python3) /Users/USER/Downloads/keyboard_maestro_python_example.py








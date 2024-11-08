#!/usr/bin/env python
import sys
import os

def example():
	# example_variable = str(os.environ["KMVAR_PW_test"])
	# example_variable = str(os.environ["KMINFO_Trigger"])
	example_variable = str(os.environ["KMVAR_TEST"])
	example_variable2 = str(os.environ["KMINFO_TriggerValue"])
	input_text = sys.stdin.read()
	# example_variable = str(os.environ["KMVAR_local_test"])

	with open(os.path.expanduser("~/Downloads/TEST.txt"), "w") as f:
		f.write(example_variable + "\n\n")
		f.write(example_variable2 + "\n\n")
		f.write(input_text)

example()

# Execute the following from an "Execute Shell Script" action in Keyboard Maestro
# with input from text to pass multiple variables
# $(which python) /Users/USER/Downloads/keyboard_maestro_python_example.py

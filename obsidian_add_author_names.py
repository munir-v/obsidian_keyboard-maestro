# updates the titles and names of linked notes in target_file with the added author name
# searches for "![[", replaces the next "]]" with add_to_end

import os #used to renames files
import pathlib #used to get working directory

current_path = pathlib.Path().resolve() #current working directory

def refactor():
	file_array = []
	with open(target_file, "r") as f:
		file_array = f.readlines()
		for index, line in enumerate(file_array): 
			if "![[" in line:
				partitioned_string = line[3:].partition("]") # substring 3 until first closing bracket
				linked_file_title = partitioned_string[0]+".md" # file title without starting and closing brackets

				old_file_name = current_path / linked_file_title
				new_line = line.replace("]]", add_to_end+"]]") # add author name to end within the main file
				file_array[index] = new_line

				new_target_file = linked_file_title[:len(linked_file_title)-3]+add_to_end+".md" # new file name 
				new_file_name = current_path / new_target_file # new file path

				os.rename(old_file_name, new_file_name) # rename the old files

	with open(target_file, "w") as f: # write changes to the original file
		f.writelines(file_array)

def printResult():
	with open(target_file, "r") as f:
		for line in f:
			print(line, end='')
		print()

target_file = "Some Answered Questions.md" # file to add author names to end
add_to_end = " - ʻAbdu'l-Bahá"

refactor()
printResult()




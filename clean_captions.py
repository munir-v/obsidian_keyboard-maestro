#!/usr/bin/env python3
import os
import sys

# Ensure that a caption file is provided as an argument
if len(sys.argv) != 2:
    print("Usage: clean_captions.py <caption_file>")
    sys.exit(1)

caption_file = sys.argv[1]
base_filename = os.path.splitext(os.path.basename(caption_file))[0]
output_file = os.path.expanduser(f'~/Downloads/{base_filename} cleaned.txt')

# List of substrings that if found in a line, exclude that line
bad_words = ['-->', '</c>']

# Initialize a set to store unique lines
unique_lines = set()

# Open the original .vtt file to read and the final file to write simultaneously
with open(caption_file, 'r') as oldfile, open(output_file, 'w') as newfile:
    for line in oldfile:
        # Check if the line does not contain any of the bad words
        if not any(bad_word in line for bad_word in bad_words):
            # Optionally, strip ">>" from the line. Adjust accordingly if this is not what's intended.
            cleaned_line = line.replace(">>", "").strip()
            # Add the cleaned line to the set if it's not a duplicate
            if cleaned_line not in unique_lines:
                unique_lines.add(cleaned_line)
                # Write the unique line to the new file
                newfile.write(cleaned_line + '\n')

# Note: Since sets are used, the order of lines in the final file may not match the original order.

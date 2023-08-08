#!/usr/bin/env python3

import os

def make_cloze():
	cloze_counter = int(os.environ["KMVAR_StartFromCloze"])

	input = str(os.environ["KMVAR_Input"])
	input.strip()
	input_words = input.split()

	for i, word in enumerate(input_words): # add spaces back
		input_words[i] = word + ' '

	input_words.insert(0,'{{c' + str(cloze_counter) + '::')

	for i, word in enumerate(input_words):
		words_per_cloze = int(os.environ["KMVAR_Words"])
		if i>1 and i % (words_per_cloze + 1) == 0:
			cloze_counter += 1
			input_words.insert(i,'}} {{c' + str(cloze_counter) + '::')
	input_words.append('}}')

	result = ''.join(input_words)
	return result.replace(' }}','}}')

print(make_cloze())



# Regular expressions
import glob
import re

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Characters
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def legal_char_for_char(c):
	if   c == '\n': return ' '
	return c

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Words
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Sentences
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def sentence_to_wordlist(sent):
	cleansent = re.sub("[^a-zA-Z]"," ", sent)
	words = cleansent.split()
	return words

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def sentence_end_char(c):
	if   c == '.':  return True
	elif c == '?':  return True
	elif c == '!':  return True
	return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def mid_sentence_abbr(str):
	if   str.endswith("Mr."):  return True
	elif str.endswith("Mrs."): return True
	elif str.endswith("Dr."):  return True
	elif str.endswith("Hon."): return True
	elif str.endswith("etc."): return True
	elif str.endswith("ie."):  return True
	elif str.endswith("AM."):  return True
	elif str.endswith("PM."):  return True
	return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Files
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def import_textfile_to_sentencelist(filepath):
	accumulated_sentence = ""
	sentencelist = []
	c = ' '
	with open (filepath, "r") as f:
		while c: 
			c = f.read(1)
			accumulated_sentence += legal_char_for_char(c)

			if ( (sentence_end_char(c)) and not (mid_sentence_abbr(accumulated_sentence)) ):
				sentencelist.append(accumulated_sentence.strip().lower())
				accumulated_sentence = ""

	return sentencelist

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def import_textfile_to_linelist(filepath):
	with open (filepath, "r") as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content] 
	return content

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


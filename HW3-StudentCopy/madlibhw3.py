# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

from nltk import word_tokenize,sent_tokenize
from nltk.book import text2

text=text2[:150] #first 150 tokens
tagged_tokens = nltk.pos_tag(text) # fix "text" vs "tokens" idk


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRON": "a pronoun"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "PRON":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

original=[]
for x in text:
	original.append(spaced(x))
print ("".join(original))

final_words = []
for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


print("\n\nEND*******")

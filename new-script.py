#!/bin/python3
import sys #system functions and parameters
from datetime import datetime as dt
print(dt.now())

my_name = "Danny"
print(my_name[0])
print(my_name[-1])

sentence = "this is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "he said, \"give me all your money\""
print(quote)

too_much_space = "       hello                  "
print(too_much_space.strip())

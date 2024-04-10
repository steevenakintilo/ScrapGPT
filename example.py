from scrap import *
import traceback
import yaml

print("Testing ScrapGPT")
list_of_question = ["Naruto becomes the best-selling manga in history","How much is 4162 + 2","What is the capital of China?","Hello"]

list_output = maker(list_of_question,len(list_of_question))

for elem in list_output:
  print(elem)

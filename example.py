from scrap import *

# The maker function takes 1 argument a list that will contain all the question you want to ask to the bot it can either be 1,9 or any number you want

print("Testing ScrapGPT")

list_of_question = ["Naruto becomes the best-selling manga in history","How much is 4162 + 2","What is the capital of China?","Hello"]

list_output = maker(list_of_question)

for elem in list_output:
  print(elem)

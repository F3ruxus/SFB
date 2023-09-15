# Juan Garcia, Mia Juarez
# ##################################### String Methods#################################
# # String Methods Practice #1
# # Print the following text in uppercase, using the specific string method:
# # "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.count("in"))
# print(sentence.replace("in", "o"))
# print(sentence.startswith("Hello"))
# print(sentence.endswith("sugar"))

# # splitting a string and join
# txt = "Hello, World! World, world fugar mya "
# print(txt[0]) # prints H
# print(txt[1]) # prints e
# newString = txt.split(",")
# print(newString)
# print(newString[1]) # prints world
# print(newString[2])
# string3 = txt.split(" ")
# print(string3)
# print(string3[1])
# print(string3[-1])
# string4 = txt.split("d")
# print(string4)
# string5 = txt.split("o")
# print(string5)

# i = " ".join(newString)
# print(i)

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple", "is", "better", "than", "complex."]
o = " ".join(word_list)
print(o)

# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
prnt = "If the implementation is hard to explain, it might be a bad idea."
print(prnt.replace("hard", "easy"))
print(prnt.replace("bad", "good"))
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

word = "Repitition "
print(word * 15)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
text = "'Whitecaps on the bay: A broken signboard banging In the April wind.' — Richard Wright, collected in Haiku: This Other World, 1998"
print(text.find("beach"))  # if it prints -1, it's not found

booolean = "beach" in text.lower()
print(booolean)

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.

text2 = " electroencephalographist."
print(len(text2))

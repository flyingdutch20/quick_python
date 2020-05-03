"""Read a file and return the number of lines, words and characters"""

infile = open('exercise_answers/word_count.tst')
text = infile.read()
punct = str.maketrans("","","!.,:;-?/n")

line_count = len(text.split("\n"))
word_count = len([word for word in text.replace("\n", " ").split(" ") if word])
char_count = len(text.translate(punct))

words = [word for word in text.replace("\n", " ").split(" ") if word]

print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))
print(words)
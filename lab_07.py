#open moby_clean and count the words

wordcount = {}
with open("moby_01_clean.txt") as infile:
    for word in infile:
        word = word.strip()
        if len(word) > 0:
            wordcount[word] = wordcount.get(word, 0) + 1

print("*** sorted by word ***")
sorted_keys = sorted(wordcount.keys())
for word in sorted_keys:
    print("The word '{0}' occurs {1} times in Moby Dick chapter 1".format(word, wordcount[word]))
print("")

print("*** words occurring more than once ***")
sorted_by_value = sorted(wordcount.items(),key=lambda x:x[1],reverse=True)
for word in sorted_by_value:
    if word[1] > 1:
        print("The word '{0}' occurs {1} times in Moby Dick chapter 1".format(word[0],word[1]))

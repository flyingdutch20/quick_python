#lab_6 refactored into functions
def output_words(infile, outfile):
    punct = str.maketrans("","","!.,:;-?")
    with open(infile) as infile, open(outfile, "w") as outfile:
        for line in infile:
            line = line.lower()                        # make all one case
            line = line.translate(punct)               # remove punctuation
            split = line.split()                       # split into words
            if split:                                  # if not empty
                cleaned_words = "\n".join(split) + "\n"    # write all words for line
                outfile.write(cleaned_words)

output_words("exercise_answers/moby_01.txt", "moby_01_clean.txt")


# lab_07 refactored into functions

# "moby_01_clean.txt"

def count_words(infile):
    wordcount = {}
    with open(infile) as infile:
        for word in infile:
            word = word.strip()
            if word:
                wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount

def print_wordcount_by_word(dict_of_words):
    print("*** sorted by word ***")
    sorted_keys = sorted(dict_of_words.keys())
    for word in sorted_keys:
        print("The word '{0}' occurs {1} times in the list".format(word, dict_of_words[word]))

def print_wordcount_more_than_once(dict_of_words):
    print("*** words occurring more than once ***")
    sorted_by_value = sorted(dict_of_words.items(),key=lambda x:x[1],reverse=True)
    for word in sorted_by_value:
        if word[1] > 1:
            print("The word '{0}' occurs {1} times in the list".format(word[0],word[1]))

def lab_07(infile):
    output_words(infile, "moby_01_clean.txt")
    my_dict = count_words("moby_01_clean.txt")
    print_wordcount_by_word(my_dict)
    print_wordcount_more_than_once(my_dict)

lab_07("exercise_answers/moby_01.txt")

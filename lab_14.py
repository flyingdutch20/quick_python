#lab 14; lab_09 with exception handling
import os

def output_words(infile, outfile):
    punct = str.maketrans("","","!.,:;-?")
    try:
        with open(infile) as infile:
            try:
                with open(outfile, "w") as outfile:
                    for line in infile:
                        line = line.lower()                        # make all one case
                        line = line.translate(punct)               # remove punctuation
                        split = line.split()                       # split into words
                        if split:                                  # if not empty
                            cleaned_words = "\n".join(split) + "\n"    # write all words for line
                            outfile.write(cleaned_words)
                    print("Finished without error")
            except IOError:
                print("Error: could not write to {0}".format(outfile))
    except FileNotFoundError:
        print("Error: could not find file {0}".format(infile))
    except IOError:
        print("Error: could not read {0}".format(infile))

output_words("excise_answers/moby_01.txt", "output/moby_01_clean.txt")
output_words("exercise_answers/moby_01.txt", "utput/moby_01_clean.txt")

output_words("exercise_answers/moby_01.txt", "output/moby_01_clean.txt")


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
    if not os.path.exists("output"):
        os.mkdir("output")
    output_words(infile, "output/moby_01_clean.txt")
    my_dict = count_words("output/moby_01_clean.txt")
    print_wordcount_by_word(my_dict)
    print_wordcount_more_than_once(my_dict)

# lab_07("exercise_answers/moby_01.txt")

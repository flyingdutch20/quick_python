# ### LAB 6: PREPROCESSING TEXT
# In processing raw text it’s quite often necessary to clean and normalize the text before doing anything else. If we want to find the frequency of words in a text for example, we can make the job easier if before we start counting we make sure that everything is lower case (or upper case, if you prefer) and that all punctuation has been removed. It can also make things easier if the text is broken into a series of words.
#
# In this lab the task is to read an excerpt of the first chapter of Moby Dick, make sure that everything is one case, remove all punctuation, and write the words one per line to a second file. Again, since we haven’t yet covered reading and writing files, the code for those operations is supplied below.
# ```

punct = str.maketrans("","","!.,:;-?")
with open("exercise_answers/moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
     for line in infile:
         line = line.lower()                        # make all one case
         line = line.translate(punct)               # remove punctuation
         split = line.split()                       # split into words
         if split:                                  # if not empty
             cleaned_words = "\n".join(split) + "\n"    # write all words for line
             outfile.write(cleaned_words)

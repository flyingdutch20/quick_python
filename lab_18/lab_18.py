from lab_18 import clean_line, get_words, count_words, word_stats, EmptyStringError

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        try:
            cleaned_line = clean_line(line)
        except EmptyStringError:
            continue

        cleaned_words = get_words(cleaned_line)

        # write all words for line
        outfile.write(cleaned_words)

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())

word_count = count_words(moby_words)

most, least = word_stats(word_count)
print("Most common words:")
for word in most:
    print(word)
print("\nLeast common words:")
for word in least:
    print(word)

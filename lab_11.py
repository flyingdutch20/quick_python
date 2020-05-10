"""Read a file and return the number of lines, words and characters"""

from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("filename", help='text file to be read')
    parser.add_argument("-w", "--words", help="report the number of words",
                        action="store_true", default=False)
    parser.add_argument("-l", "--lines", help="report the number of lines",
                        action="store_true", default=False)
    parser.add_argument("-c", "--characters", help="report the number of characters",
                        action="store_true", default=False)
    args = parser.parse_args()

    infile = open(args.filename)
    text = infile.read()
    punct = str.maketrans("", "", "!.,:;-?/n")

    line_count = len(text.split("\n"))
    word_count = len([word for word in text.replace("\n", " ").split(" ") if word])
    char_count = len(text.translate(punct))

    if args.words:
        print("File has {0} words".format(word_count))
    if args.lines:
        print("File has {0} lines".format(line_count))
    if args.characters:
        print("File has {0} characters".format(char_count))
    if (not args.words and not args.lines and not args.characters):
        print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))

main()
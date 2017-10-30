import sys

def cli():
    filename = sys.argv[1]
    specific_file = open(filename,"U")
    file_text = specific_file.readlines()
    specific_file.close()
    unique_words(file_text)

def unique_words(text):
    if len(text) == 0:
        print 0
        return

    all_words = dict()
    word_list = list()
    unique = list()

    for line in text:
        line = line.split()
        for word in line:
            word_list.append(word.lower())
            all_words[word] = int(word_list.count(word))

    for word in all_words:
        if all_words[word] == 1:
            unique.append(word)

    print len(unique)

if __name__ == '__main__':
    cli()

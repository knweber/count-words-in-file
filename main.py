import sys

def cli():
    filename = sys.argv[1]
    specific_file = open(filename,"U")
    file_text = specific_file.readlines()
    specific_file.close()
    unique_words(file_text)

def unique_words(text):
    if len(text) == 0:
        return

    all_words = list()

    for line in text:
        line = line.split()
        for word in line:
            all_words.append(word)

            


    curr_count = 0


if __name__ == '__main__':
    cli()

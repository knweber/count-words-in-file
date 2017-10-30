import sys

def cli():
    filename = sys.argv[1]
    specific_file = open(filename,"U")
    file_text = specific_file.readlines()
    specific_file.close()
    unique_words(file_text)

def line_to_words(text):
    text = text.split(" ")
    return text

def unique_words(text):
    if len(text) == 0:
        return

    curr_count = 0



if __name__ == '__main__':
    cli()

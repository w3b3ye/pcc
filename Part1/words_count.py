
#A simple program to count words in given files.
#Files in this examples are downloaded from Project 'Gutenberg' http://gutenberg.org/
def words_count(filename):
    """Cont the approx number of words in a file.';"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt','pirate.txt','xyz.txt','kidswolf.txt']
for filename in filenames:
     words_count(filename)

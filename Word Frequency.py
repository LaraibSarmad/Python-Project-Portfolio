import string


def read_file(filename):

    """Reads the contents of a text file and returns a list of the words in the file"""

    with open(filename, 'r') as f:

        # Read the contents of the file

        contents = f.read()

        # Split the contents into a list of words

        words = contents.split()

        # Remove punctuation from each word

        words = [word.strip(string.punctuation) for word in words]

        # Remove any empty strings from the list

        words = [word for word in words if word]

        return words


def create_word_frequency_dict(words):

    """Creates a dictionary with the frequency of each word"""

    word_frequency_dict = {}

    for word in words:

        if word in word_frequency_dict:

            word_frequency_dict[word] += 1

        else:

            word_frequency_dict[word] = 1

    return word_frequency_dict


def print_word_frequencies(word_frequency_dict):

    """Prints the frequency of each word in the dictionary"""

    for word, frequency in word_frequency_dict.items():

        print(f'{word}: {frequency}')


def main():

    # Read the words from the file

    words = read_file('file.txt')

    # Create a dictionary with the frequency of each word

    word_frequency_dict = create_word_frequency_dict(words)

    # Print the frequency of each word

    print_word_frequencies(word_frequency_dict)


if __name__ == '__main__':

    main()



import sys
def get_book_text(filepath):
    """
    Reads the contents of a text file and returns it as a string.

    Parameters:
        filepath (str): The relative or absolute path to the text file.

    Returns:
        str: The contents of the file.
    """
    """
    try:
    """
    with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
        return file.read()
    """except FileNotFoundError:
        return "The file was not found. Please check the path."
    except Exception as e:
        return f"An error occurred: {e}"
"""
from stats import number_of_words

from stats import number_of_characters

from stats import print_dict

def main():
    # Adjust the path if your frankenstein.txt is in a subdirectory
    try:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
    # Print the number of words in the book
        word_count = number_of_words(book_text)
    #print("----------- Word Count ----------")
    #print(f"Found {word_count} total words")
        num_char = number_of_characters(book_text)
    #print("----------- Character Count ----------")
        print_dict(num_char)
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print("============= END ===============")
    #print(book_text)

# Run the main function
if __name__ == '__main__':
    main()
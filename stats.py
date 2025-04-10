def number_of_words(text):
    return len(text.split())

def number_of_characters(text):
    char_counts = {}
    with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.isalpha():  # Check if the character is a letter
                    char = char.lower()  # Convert to lowercase
                    char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def get_book_text(file_path):
    """
    Reads the content of a text file and returns it as a string.
    
    Parameters:
        file_path (str): The path to the text file.
    
    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def print_dict(dictionary):
    """
    Prints the contents of a dictionary in a formatted way.
    
    Parameters:
        dictionary (dict): The dictionary to print.
    """
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")

def main():
    
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    # Print the number of words in the book
    word_count = number_of_words(book_text)
    print("----------- Word Count ----------")
    print(f"{word_count} words found in the document")
    num_char = number_of_characters(book_text)
    print("----------- Character Count ----------")
    print_dict(num_char)
    #print(book_text)

if __name__ == "__main__":
    main()
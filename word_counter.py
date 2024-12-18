# word_counter.py

# Function to count words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Function to read from a file and count words
def count_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return count_words(content)
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Main execution
if __name__ == "__main__":
    print("1. Enter text manually")
    print("2. Provide a file path to count words in a file")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        user_input = input("Enter a sentence or text to count the words: ")
        word_count = count_words(user_input)
        print(f"The text contains {word_count} words.")
    elif choice == "2":
        file_path = input("Enter the path to the text file: ")
        word_count = count_words_from_file(file_path)
        if word_count is not None:
            print(f"The file contains {word_count} words.")
    else:
        print("Invalid option. Please choose 1 or 2.")

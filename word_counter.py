# Function to count words in a string
def count_words(text):
    words = text.split()  # Split text into words
    return len(words)

# Function to read content from a file and count words
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
    print("Choose an option:")
    print("1. Enter text manually")
    print("2. Read text from a file")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        user_input = input("Enter a sentence or text to count the words: ")
        word_count = count_words(user_input)
        print(f"The text contains {word_count} words.")
    elif choice == "2":
        file_path = input("Enter the file path: ")
        word_count = count_words_from_file(file_path)
        if word_count is not None:
            print(f"The file contains {word_count} words.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
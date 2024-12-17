 
# word_counter.py

# Function to count words in a string
def count_words(text):
    words = text.split()  # Split text into words
    return len(words)

# Main execution
if __name__ == "__main__":
    user_input = input("Enter a sentence or text to count the words: ")
    word_count = count_words(user_input)
    print(f"The text contains {word_count} words.")

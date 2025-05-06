import time
import os
from textblob import TextBlob

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def word_counter(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    unique_words = set(words)

    return word_count, char_count, unique_words

def detect_typos(text):
    blob = TextBlob(text)
    typos = {}
    for word in blob.words:
        corrected = word.correct()
        if corrected.lower() != word.lower():
            typos[word] = corrected
    return typos

def display_summary(text):
    word_count, char_count, unique_words = word_counter(text)
    typos = detect_typos(text)

    typing_effect("\nAnalyzing your text...\n", delay=0.05)
    time.sleep(0.5)

    print("========== SUMMARY ==========")
    print(f"Total Characters : {char_count}")
    print(f"Total Words      : {word_count}")
    print(f"Unique Words     : {len(unique_words)}")
    print(f"Unique Word List : {', '.join(sorted(unique_words))}")
    print("=============================")

    if typos:
        print("\n!!! POSSIBLE TYPING ERRORS DETECTED !!!")
        for word, correction in typos.items():
            print(f" - '{word}' might be a typo. Suggestion: '{correction}'")
    else:
        print("\nNo obvious spelling errors detected.")
    print("=============================\n")

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main Program
if __name__ == "__main__":
    clear_screen()
    typing_effect("Welcome to the Python Word Counter with Spell Checker!", delay=0.05)
    
    print("\nWould you like to check text manually or upload a text file?")
    print("1. Type manually")
    print("2. Upload .txt file")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        user_input = input("\nEnter your text: ")
        display_summary(user_input)

    elif choice == '2':
        filepath = input("\nEnter the path to your .txt file: ").strip()
        content = read_file_content(filepath)
        if content:
            display_summary(content)
    else:
        print("Invalid choice. Please restart the program.")

def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        # print(file_contents)
        
        count_words(file_contents)
        print("\n")
        count_letters(file_contents)
        
        
        

def count_words(text):
    words = text.split()
    print(f"Total words: {len(words)}")


def count_letters(text):
    letters = {}
    
    for char in text:
        char = char.lower()
        
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
    
    for key, value in letters.items():        
        print(f"The '{key}' was found ;{value}' times")

if __name__ == "__main__":
    main()
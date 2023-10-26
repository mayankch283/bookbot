with open("/home/mayankch283/workspace/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(file):
    return len(file.split())

def count_letters(file):
    count = {}
    for ch in file:
        if ch.isalpha():
            if ch.lower() in count:    
                count[ch.lower()] += 1
            else:
                count[ch.lower()] = 1
    
    return sorted(count.items())

num_of_words = count_words(file_contents)
frequency_of_letters = count_letters(file_contents)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_of_words} words found in the document\n")

for subset in frequency_of_letters:
        print(f"The '{subset[0]}' character was found {subset[1]} times")

print("--- End report ---")


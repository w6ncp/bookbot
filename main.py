def read_book(pathToBook):
    output = ""
    with open(pathToBook) as file:
        output = file.read()
    return output

def word_count(textToCount):
    return len(textToCount.split())

def char_count(textToCount):
    return len(textToCount)

def unique_char(textToCount):
    lower = textToCount.lower()
    count = {
        "a": 0, "b": 0, "c": 0,
        "d": 0, "e": 0, "f": 0,
        "g": 0, "h": 0, "i": 0,
        "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0,
        "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0,
        "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0, "1": 0,
        "2": 0, "3": 0, "4": 0, 
        "5": 0, "6": 0, "7": 0,
        "8": 0, "9": 0, "0": 0,
    }
    extras = {}
    for char in lower:
        if char in count:
            count[char] += 1
        elif char in extras:
            extras[char] += 1
        else:
            extras[char] = 1
    total = {}
    total.update(count)
    total.update(extras)
    return len(total), count

def order_unique(dictUnique):
    return {key: value for key, value in sorted(dictUnique.items(), key=lambda item: item[1], reverse=True)}

def main(bookPath):
    textContents = ""
    try:
        textContents = read_book(bookPath)
        wordCount = word_count(textContents)
        charCount = char_count(textContents)
        numUnique, uniqueChar = unique_char(textContents)
        sortedUniques = order_unique(uniqueChar)
    except FileNotFoundError:
        print("File is not found or path not valid.")
    except:
        print("Another error occured")
    # print(text)
    print(f"=== Begin report for {bookPath} ===")
    print(f"Words in text:      {wordCount}")
    print(f"Characters in text: {charCount}")
    print(f"Unique Characters:  {numUnique}")
    print(f"Sorted uniques characters by count:")
    for char, num in sortedUniques.items():
        print(f"The \'{char}\' character was found {num} times")
    print("=== End report ===")
    return textContents

pathToBook = "books/frankenstein.txt"
textContents = main(pathToBook)
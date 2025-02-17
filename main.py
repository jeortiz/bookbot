def getAplhabetCount(text) -> list:
    char_count = {}

    for word in text:
        for char in word:
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
    
    return char_count
    
def sort_on(dict):
    return dict['num']
    
def main() -> int:
    path = "books/frankenstein.txt"

    print(f'--- Begin the report of {path} ---')
    
    with open(path) as f:
        file_contents = f.read()
    
    wordList = file_contents.lower().split()
    wordCount = len(wordList)

    print(f"{wordCount} words found in the document\n")

    charCount = getAplhabetCount(wordList)
    wordCountList = [{"name": key, "num":value} for key, value in charCount.items()]

    wordCountList.sort(reverse=True, key=sort_on)

    for char in wordCountList:
        print(f"The '{char['name']}' character was found {char['num']} times")

    print('--- End report ---')

main()
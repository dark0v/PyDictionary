import json

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Ups! I can't find that word. Please, check it again")

word = input('Enter the word you want to search: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print("- " + item)
else:
    print(output)
import json, os

FILEPATH = os.path.join(os.path.dirname(__file__), "languages.json")

def load_languages(filepath=FILEPATH):
    with open(filepath) as languagefile:
        languages = json.load(languagefile)
    for l in languages.keys():
        words = languages[l]['words']
        words_with_spaces = map(lambda w: w.replace("_", " "), words)
        languages[l]['words'] = list(words_with_spaces)
    return languages

if __name__ == "__main__":
    languages = load_languages()
    for l in languages.keys():
        print(languages[l])

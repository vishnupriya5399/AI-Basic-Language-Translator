class Translator:
    def __init__(self):
        # Dictionary for English to Spanish translations
        self.dictionary = {
            'howareyou': 'Cómo estás',
            'goodbye': 'adiós',
            'goodnight': 'buenas noches',
            # Add more translations as needed
        }

    def translate(self, word):
        # Check if the word is in the dictionary
        if word.lower() in self.dictionary:
            return self.dictionary[word.lower()]
        else:
            return "Translation not available for '{}'.".format(word)

def main():
    translator = Translator()

    while True:
        # Get user input
        word_to_translate = input("Enter a word or phrase in English (type 'exit' to quit): ")

        # Check if the user wants to exit
        if word_to_translate.lower() == 'exit':
            break

        # Translate the input
        translation = translator.translate(word_to_translate)

        # Display the translation
        print("Translation: {}".format(translation))
        print()

if __name__ == "__main__":
    main()

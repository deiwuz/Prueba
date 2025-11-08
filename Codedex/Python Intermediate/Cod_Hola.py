

def translator(language):
    translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate_word(word: str):
        if word.lower() in translations[language]:
            return translations[language][word.lower()]
        else:
            return ("We don't have the translation for that word")
    
    return translate_word

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola
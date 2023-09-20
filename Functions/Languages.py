def language_recognizer():
    print("Bitte wählen Sie die gewünschte Sprache, D für Deutsch F für Französisch oder E für Englisch: ")
    language = input("Welche Sprache wünschen Sie? ")
    if language == "D":
        print("Willkommen")
    elif language == "F":
        print("Bonjour")
    elif language == "E":
            print("Welcome")
    else:
        print("Your language is not supported, sorry!")

language_recognizer()
def translate(text, lang):
    from googletrans import Translator
    translator = Translator()
    translated = translator.translate(text, dest=lang)
    return translated.text
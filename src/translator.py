def translate(text: str, lang: str):
    """Returns the text translated through the Google translation engine.

    :param text: text to translate
    :type text: str
    :param lang: language to be translated
    :type lang: str
    :return: translated text
    :rtype: _type_
    """
    from googletrans import Translator
    translator = Translator()
    translated = translator.translate(text, dest=lang)
    
    return translated.text
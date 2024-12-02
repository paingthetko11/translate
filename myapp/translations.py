# translations.py
from .en_translations import translations as en_translations
from .my_translations import translations as my_translations

all_translations = {
    "en": en_translations,
    "my": my_translations,
}

def translate(text, language_code):
    translation = all_translations.get(language_code, {}).get(text)
    if translation:
        return translation
    components = text.split(" - ")
    translated_components = [
        all_translations.get(language_code, {}).get(comp, comp) for comp in components
    ]
    translated_text = " - ".join(translated_components)
    return translated_text
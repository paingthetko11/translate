# myapp/templatetags/translate_filters.py
from django import template
from myapp.translations import translate

register = template.Library()
@register.filter(name='custom_translate')
def custom_translate(text, language_code):
    translation = translate(text, language_code)
    if translation == text:
        print(f"Translation not found for '{text}' in language '{language_code}'")
    return translation
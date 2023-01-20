import random
import json

def findVoice(langCode: str, gender: str, country: str) -> str:
    with open('static/voiceList.json') as fp:
        voices = json.load(fp)

    if gender == 'Select':
        gender = 'Female'

    def lang_check(voice):
        if country != 'Select':
            return langCode in voice['Locale'] and voice['Gender'] == gender and country in voice['Language']
        else:
            return langCode in voice['Locale'] and voice['Gender'] == gender

    rlist = list(filter(lang_check, voices))
    return random.choice(rlist)['Voice name']


def findCountries(langcode: str) -> list:
    with open('static/voiceList.json') as fp:
        voices = json.load(fp)

    values = []
    for voice in voices:
        if langcode in voice['Locale']:
            country = voice['Language'].split(' ')[1:]
            country = ' '.join(country)
            if country not in values:
                values.append(country)

    values.sort()
    return values


def getLanguages():
    with open('static/voiceList.json') as fp:
        voices = json.load(fp)

    values = []
    for voice in voices:
        lang = [voice['Locale'].split('-')[0], voice['Language'].split(' ')[0]]
        if lang not in values:
            values.append(lang)

    return values

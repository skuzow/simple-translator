# -*- coding: utf-8 -*-
# Author: LegendNightt

from googletrans import Translator

translator = Translator()


# Translator
def translatorA(msg):
    translation = translator.detect(msg)
    if translation.lang == 'en':
        spanishtrans = translator.translate(msg, dest='es')
        text = spanishtrans.text
    else:
        englishtrans = translator.translate(msg, dest='en')
        text = translation.text = englishtrans.text
    return str(text)


# MCDReforged
def on_info(server, info):
    if info.is_player == 1 and info.content.startswith('t '):
        result = translatorA(info.content[2:])
        server.say('§7[T]<' + info.player + '> §f' + result)


def on_load(server, old):
    server.add_help_message('Translator (t )',
                            'Use t and space and then what you want to translate, EN to ES and ES to EN auto')

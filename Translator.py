from google_trans_new import google_translator
translator = google_translator()

PLUGIN_METADATA = {
    'id': 'translator',
    'version': '1.0.0',
    'name': 'Translator',
    'description': 'Translates text ingame',
    'author': [
        'LegendNightt',
    ],
    'link': 'https://github.com/LegendNightt/MCDR-Translator'
}

# Translator
def translatorA(msg):
    translation = translator.detect(msg)
    if translation[0] == 'en':
        result = translator.translate(msg, lang_tgt='es')
    else:
        result = translator.translate(msg, lang_tgt='en')
    return str(result)

# MCDReforged
def on_info(server, info):
    if info.is_player and info.content.startswith('t '):
        server.say(f'§7[T]<{info.player}> §f{translatorA(info.content[2:])}')

def on_load(server, old):
    server.register_help_message('Translator (t )',
                                 'Use t and space and then what you want to translate, EN to ES and ES to EN auto')

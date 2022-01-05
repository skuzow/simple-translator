from mcdreforged.api.all import *
from googletrans import Translator
translator = Translator()

# autoTranslator stuff
def autoTranslator(msg: str):
    if translator.detect(msg).lang == 'en':
        return translator.translate(msg, dest='es').text
    else:
        return translator.translate(msg, dest='en').text

# MCDReforged stuff
def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('t '):
        server.reply(info, f'§7[T]<{info.player}> §f{autoTranslator(info.content[2:])}')

def on_load(server: ServerInterface, old_module):
    server.register_help_message('Translator (t )',
                                 'Use t and space, then what you want to translate, EN to ES & ALL LANGUAGES to EN auto')

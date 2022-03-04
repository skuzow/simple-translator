from mcdreforged.api.all import *
from googletrans import Translator

translator = Translator()


def auto_translator(msg: str):
    if translator.detect(msg).lang == 'en':
        return translator.translate(msg, dest='es').text
    else:
        return translator.translate(msg, dest='en').text


def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('t '):
        server.say(f'§7[T]<{info.player}> §f{auto_translator(info.content[2:])}')


def on_load(server: PluginServerInterface):
    server.register_help_message('Translator (t )',
                                 'Use t and space, then what you want to translate, EN to ES & ALL LANGUAGES to EN auto')

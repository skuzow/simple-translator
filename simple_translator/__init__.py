import os
from typing import Optional

from googletrans import Translator
from mcdreforged.api.all import *

plugin_metadata = ServerInterface.get_instance().as_plugin_server_interface().get_self_metadata()


class Config(Serializable):
    global_language: str = 'en'
    secondary_language: str = 'es'


config: Optional[Config] = None
server_inst: PluginServerInterface
translator = Translator()


def auto_translator(message: str):
    return translator.translate(message, dest=config.secondary_language).text if translator.detect(message).\
           lang == config.global_language else translator.translate(message, dest=config.global_language).text


def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('t '):
        server.say(f'§7[Translate]<{info.player}> §f{auto_translator(info.content[2:])}')


def on_load(server: PluginServerInterface, old):
    global server_inst
    server_inst = server
    load_config(None)
    prefix = '!!t translate-text'
    help_message = f'Use t and space, then what you want to translate, works from {config.global_language} to ' \
                   f'{config.secondary_language} & all languages to {config.global_language}'
    server.register_help_message(prefix, help_message)


def load_config(source: Optional[CommandSource]):
    global config, server_inst
    config_file_path = os.path.join('config', '{}.json'.format(plugin_metadata.id))
    config = server_inst.load_config_simple(config_file_path, in_data_folder=False, source_to_reply=source,
                                            echo_in_console=False, target_class=Config)

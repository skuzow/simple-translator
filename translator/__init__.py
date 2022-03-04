import os
from typing import Optional

from googletrans import Translator
from mcdreforged.api.all import *

PLUGIN_METADATA = ServerInterface.get_instance().as_plugin_server_interface().get_self_metadata()


class Config(Serializable):
    global_language: str = 'en'
    secondary_language: str = 'es'


config: Optional[Config] = None
translator = Translator()
prefix = 'Translator (t )'
plugin_name = PLUGIN_METADATA.name
server_inst: PluginServerInterface


def auto_translator(msg: str):
    return translator.translate(msg, dest=config.secondary_language).text if translator.detect(
        msg).lang == config.global_language else translator.translate(msg, dest=config.global_language).text


def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('t '):
        server.say(f'§7[T]<{info.player}> §f{auto_translator(info.content[2:])}')


def on_load(server: PluginServerInterface, old):
    global server_inst
    server_inst = server
    load_config(None)
    help_message = f'Use t and space, then what you want to translate, {config.global_language.upper()} to ' \
                   f'{config.secondary_language.upper()} & ALL LANGUAGES to {config.global_language.upper()} auto'
    server.register_help_message(prefix, help_message)


def load_config(source: Optional[CommandSource]):
    global config, server_inst
    config_file_path = os.path.join('config', '{}.json'.format(PLUGIN_METADATA.id))
    config = server_inst.load_config_simple(config_file_path, in_data_folder=False, source_to_reply=source,
                                            echo_in_console=False, target_class=Config)

# 🌐 Simple Translator

[![license](https://img.shields.io/github/license/skuzow/simple-translator.svg)](https://github.com/skuzow/simple-translator/blob/master/LICENSE)
[![package](https://github.com/skuzow/simple-translator/actions/workflows/package.yml/badge.svg?branch=master)](https://github.com/skuzow/simple-translator/actions/workflows/package.yml)
[![python versions](https://img.shields.io/badge/python->=%203.6%20-blue)](https://www.python.org/downloads)

Really simple [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) in-game translator plugin.

More plugins in [MCDReforgedPluginsCatalogue](https://github.com/MCDReforged/PluginCatalogue/blob/catalogue/readme.md).

## 🗿 How it works?

Basically translates from all languages to `global_language`, and `secondary_language` to `global_language`.

To use it simply type: `t what you want to translate`

<img src="https://user-images.githubusercontent.com/61398114/177015561-606cfec3-78be-4a16-9846-40388561618e.png" alt="example" width="650"/>

## 💾 Config

Location: `config/simple_translator.json`

```json
{
    "global_language": "en",
    "secondary_language": "es"
}
```

## 🗂️ Required Python libraries

- [googletrans](https://pypi.org/project/googletrans/4.0.0rc1) == 4.0.0rc1
- [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) >= 1.2.0

To install them execute:

```bash
pip install -r requirements.txt
```

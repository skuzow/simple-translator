# mcdr-translator

[![license](https://img.shields.io/github/license/legendnightt/MCDR-Translator.svg)](https://github.com/legendnightt/MCDR-Translator/blob/master/LICENSE)
[![plugin package build status](https://github.com/legendnightt/MCDR-Translator/actions/workflows/package.yml/badge.svg?branch=master)](https://github.com/legendnightt/MCDR-Translator/actions/workflows/package.yml)
[![supported python versions](https://img.shields.io/badge/python->=%203.6%20-blue)](https://www.python.org/downloads)

Really simple [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) plugin for translating text ingame, from all languages to `global_language`, and `secondary_language` to `global_language` automatically.

More plugins in [MCDReforgedPluginsCatalogue](https://github.com/MCDReforged/PluginCatalogue/blob/catalogue/readme.md).

## How it works?

Simply type `t what you want to translate`.

### Example:

![example](https://raw.githubusercontent.com/legendnightt/MCDR-Translator/master/img/example.png)

## Required python modules

- [googletrans](https://pypi.org/project/googletrans/4.0.0rc1) == 4.0.0rc1
- [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) >= 1.2.0

To install them execute:
```bash
pip install googletrans==4.0.0rc1 mcdreforged
```
Or download [requirements.txt](https://github.com/legendnightt/mcdr-translator/blob/master/requirements.txt), and execute:
```bash
pip install -r requirements.txt
```

## Config

`config/translator.json`

```json
{
    "global_language": "en",
    "secondary_language": "es"
}
```

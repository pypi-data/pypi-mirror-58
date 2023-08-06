"""Support for loading/getting configuration dictionaries.
"""

import os

import toml


def load_config(config_path, encoding='utf-8'):
    config = toml.loads(config_path.read_text(encoding=encoding))
    gk_config = config.get('godkjenn', {})
    gk_config['root_dir'] = str(config_path.parent)
    return gk_config


def default_config(root_path=None):
    if root_path is None:
        root_dir = os.getcwd()
    else:
        root_dir = str(root_path)

    return {
        'root_dir': root_dir
    }

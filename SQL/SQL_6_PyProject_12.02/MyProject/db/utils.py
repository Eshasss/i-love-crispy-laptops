"""
util file
"""

import os


def get_script_from_file(filename: str) -> str:
    """
    импорт скриптов sql
    """
    with open(os.path.join("./db", "scripts", filename), "r", encoding='utf8') as f:
        return f.read()

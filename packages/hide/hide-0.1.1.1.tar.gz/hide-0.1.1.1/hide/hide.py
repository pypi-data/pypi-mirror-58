from __future__ import unicode_literals
from prompt_toolkit import prompt

def hide(input=""):
    return prompt(input,is_password=True)

from __future__ import unicode_literals

def hide(input=""):
    from prompt_toolkit import prompt
    return str(prompt(input,is_password=True))

#coding: utf-8
def hidoood(input=""):
    from prompt_toolkit import prompt
    try:
      return str(prompt(input,is_password=True))
    except ValueError:
      raise Exceptions ("\n\x1b[1;32mEnter This On Your Code\nfrom __future__ import unicode_literals")

def hide(input=""):
    from prompt_toolkit import prompt
    hidoood(unicode(input))

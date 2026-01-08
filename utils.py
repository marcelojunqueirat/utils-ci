import os
from dotenv import load_dotenv
from robot.api.deco import keyword

@keyword
def carregar_env(path):
    load_dotenv(path)

@keyword
def coletar_env(var_name, default=None):
    return os.getenv(var_name, default)

@keyword
def teste_nome(string):
    return string
    
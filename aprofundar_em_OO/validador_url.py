"""
codigo sobre Expressões Regulares
valida de a URL é aceita para ser usado em extrator_url

"""

import re

url = 'www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida")

print('A URL é válida')
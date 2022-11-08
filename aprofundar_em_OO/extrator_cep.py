"""
codigo sobre Expressões Regulares
encontra o padrao CEP na string
para ser usado em extrator_url

"""

endereco = "Rua das flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

import re # regular expression

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # 5 digitos de 0 a 9, hifen opcional, mais 3 digitos de 0 a 9
busca = padrao.search(endereco) # match
if busca:
    cep = busca.group()
    print(cep)
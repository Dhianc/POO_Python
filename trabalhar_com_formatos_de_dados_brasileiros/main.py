from acesso_cep import BuscaEndereco
import requests

cep = "38410366"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, estado = objeto_cep.acessa_via_cep()
print(estado)
import requests
import pprint

uf = "RJ"
cidade = "Rio de Janeiro"
logradouro = "Avenida Rio Branco"

link = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"

requisicao = requests.get(link)
pprint.pprint(requisicao)

dic_requisicao = requisicao.json()
pprint.pprint(dic_requisicao)
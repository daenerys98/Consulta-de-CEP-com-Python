import requests

cep = "59610210"

cep = cep.replace("-", "").replace(",", "").replace("", "") # Substituem os caracteres caso coloquem o cep como se fosse: 5961-0210 ou de outras formas e deixa ele só os números para poder localizar

if len(cep) == 8:

    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link) # pegar informações do link acima

    print(requisicao) # chama todo o endereço

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']

    cidade = dic_requisicao['localidade']

    print(uf, cidade)  # chama só os que passamos acima, já que é um dicionario chama assim como acima

else:
    print("CEP inválido!")
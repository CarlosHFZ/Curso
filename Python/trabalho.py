import requests


nome = str(input('Digite seu nome: '))
response = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}').json()
print(response)
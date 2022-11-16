import requests

nome = str(input('Digite seu nome: '))
response = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}').json()


for i in range(len(response[0]['res'])):
    arrumado = response[0]['res'][i]['periodo'].replace('[','').replace(',',' a ') 
    print(f"Entre {arrumado}, o nome {nome} teve {response[0]['res'][i]['frequencia']} registros")



# [
#     {
#         'nome': 'CARLOS', 
#         'sexo': None, 
#         'localidade': 'BR', 
#         'res': [
#                     {'periodo': '1930[', 'frequencia': 4659}, {'periodo': '[1930,1940[', 'frequencia': 15620}, {'periodo': '[1940,1950[', 'frequencia': 53410}, {'periodo': '[1950,1960[', 'frequencia': 154038}, {'periodo': '[1960,1970[', 'frequencia': 267228}, {'periodo': '[1970,1980[', 'frequencia': 258333}, {'periodo': '[1980,1990[', 'frequencia': 270843}, {'periodo': '[1990,2000[', 'frequencia': 198370}, {'periodo': '[2000,2010[', 'frequencia': 266690}]}]
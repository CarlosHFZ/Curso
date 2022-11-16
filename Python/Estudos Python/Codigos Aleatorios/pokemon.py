
import requests

r = str(input('Digite o nome do Pokemon: '))
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{r}/').json()

def nome():
    global response
    return response['forms'][0]['name']
def peso():
    global response
    return response['weight']
def altura():
    global response
    return response['height']
def sprite():
    global response
    return response['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
def tipo():
    global response
    return response['types'][0]['type']['name']
def main():
    global response
    print(f'O nome do pokemon é: {nome()}')
    print(f'Ele tem: {peso()} libras')
    print(f'Ele tem: {altura()} polegadas')
    print(f'Essa é um gif animado dele: {sprite()}')
    print(f'Seu tipo é: {tipo()}')

main()   
    

#nome do pokemon(se não encontrar, notificar usuario)
#sprite do pokemon (imagem) geração 5
#os tipos
#tamanho
#peso





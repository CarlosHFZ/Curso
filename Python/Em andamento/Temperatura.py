

import requests





while True:
    cidade = str(input('Digite o nome da cidade: ou se deseja encerrar digite 0. '))   
    if cidade == "0":
        break
    else:
        tempo = requests.get(f'https://weather.contrateumdev.com.br/api/weather/city/?city={cidade}').json() 
        print(f'A temperatura atual em {cidade} é {tempo["main"]["temp"]} \nA temperatura minima em {cidade} é {tempo["main"]["temp_min"]} \nA temperatura maxima em {cidade} é {tempo["main"]["temp"]}')


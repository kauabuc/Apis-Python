import requests


def converter(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")

    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None


print('--Conversor de Modas(Terminal)--')
print('Principais moedas disponíveis: USD, BRL, EUR, JPY, BTC, ETH, DOGE, ETC')

valor = float(input('Valor para converter: '))
de = input('Converter de (Escolha uma das opções acima):')
para = input('Converter para (Escolha uma das opções acima novamente.):')

para_U = para.upper()
de_U = de.upper()

cotacao = converter(valor, de, para)

if cotacao is not None:
    print(f'{valor}{de_U} é equivalente a {cotacao}{para_U}')
else:
    print('Erro: moeda inválida.')

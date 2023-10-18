# Calculadora para saber a idade com base no ano de nascimento
import datetime

# Início da função

def calculadora_idade():
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = datetime.datetime.now().year
        idade = ano_atual - ano_nascimento
        print(f"Sua idade é aproximadamente {idade} anos.")
    except ValueError:
        print("Digite um ano válido.")
"""
Para Calcular a idade 
é só informar o ano 
"""
calculadora_idade()

import datetime

def calculadora_idade():
    """
    Calcula a idade com base no ano de nascimento.
    """
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = datetime.datetime.now().year
        idade = ano_atual - ano_nascimento

        if idade < 0:
            print("Você digitou um ano de nascimento no futuro. Verifique e tente novamente.")
        else:
            print(f"Sua idade é de {idade} anos.")
    except ValueError:
        print("Digite um ano de nascimento válido (formato: YYYY).")

if __name__ == "__main__":
    calculadora_idade()

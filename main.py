# Identificação
print('Bem-vindo a Companhia de Logística Adriana C. G. Thume RU 1902469')


# Início da função dimensoesObjeto
def dimensoesObjeto():
    print('------Dimensões do Objeto------')
    while True:
        # Tratamento de exceção
        try:
            # Entrada de dados pelo usuário
            altura = int(input('Digite a altura do objeto(em cm): '))
            comprimento = int(input('Digite o comprimento do objeto(em cm): '))
            largura = int(input('Digite o largura do objeto(em cm): '))

            volume = altura * largura * comprimento

            if (volume > 0) and (volume < 1000):
                return 10
            elif (volume >= 1000) and (volume < 10000):
                return 20
            elif (volume >= 10000) and (volume < 30000):
                return 23
            elif (volume >= 3000) and (volume < 100000):
                return 50
            else:
                print('O volume do objeto é (em cm³): {:.1f}'.format(volume))
                print('Não aceitamos objetos com dimensões tão grandes.')
                continue
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico.')
            print('Por favor, entre com as dimensões desejadas novamente.')
            continue


# Início da função pesoObjeto
def pesoObjeto():
    print('------Peso do Objeto------')
    while True:
        # Tratamento de exceção
        try:
            # Entrada de dados pelo usuário
            peso = float(input('Digite o peso do objeto(em kg): '))
            if (peso > 0) and (peso <= 0.1):
                return 1
            elif (peso >= 0.1) and (peso < 1):
                return 1.5
            elif (peso >= 1) and (peso < 10):
                return 2
            elif (peso >= 10) and (peso < 30):
                return 3
            else:
                print('O peso do objeto é (em kg): {}'.format(peso))
                print('Não aceitamos objetos tão pesados')
                continue
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico.')
            print('Por favor, entre com o peso desejado novamente.')
            continue


# Início da função rotaObjeto
def rotaObjeto():
    print('------Rota do Objeto------')
    while True:
        print('Selecione a rota: ')
        print('RS - De Rio de Janeiro até São Paulo')
        print('SR - De São Paulo até Rio de Janeiro')
        print('BS - De Brasília até São Paulo')
        print('SB - De São Paulo até Brasília')
        print('BR - De Brasília até Rio de Janeiro')
        print('RB - De Rio de Janeiro até Brasília')
        # Entrada de dados pelo usuário
        rota = input('')

        if rota == 'RS':
            return 1
        elif rota == 'SR':
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'SB':
            return 1.2
        elif rota == 'BR':
            return 1.5
        elif rota == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe.')
            print('Por favor, entre com a rota desejada novamente.')
            continue


# Retornos das funções
valor = dimensoesObjeto()

multiplicador = pesoObjeto()

multiplicador2 = rotaObjeto()
# Cálculo
total = valor * multiplicador * multiplicador2

# Saída de dados
print('Total a pagar(R$): {:.2f} (dimensões: {:.1f} * peso: {:.1f} * rota: {:.1f})'
      .format(total, valor, multiplicador, multiplicador2))

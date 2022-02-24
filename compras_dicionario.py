produtos = {  # Declaração de valores no dicionario
    'Carne': {'Coxão Mole': 107.98,
              'Coxão Duro': 58.95,
              'Porco': 70.00,
              'Galinha': 65.32,
              'Boi': 32.03,
              },
    'Vegetais': {'Cenoura': 3.75,
                 'Cebola': 2.00,
                 'Alface': 3.00,
                 'Tomate': 5.00,
                 'Rucula': 4.00,
                 },
    'Frutas': {'Maça': 1.80,
               'Manga': 1.50,
               'Goiaba': 3.80,
               },
    'Temperos': {'Salsa': 6.90,
                 'Manjericão': 4.40,
                 'Alecrim': 7.70,
                 }
}
variavel = {}  # guarda todos os items do produto
quantidade_produtos_adicionados = 0  # guarda a quantidade de produtos
produtos_adicionados = []  # produtos adicionados na lista
soma_total = 0  # Soma valores total


print('\nSeja bem vindo ao sistema de compras!'.upper())
for categoria, produto in produtos.items():
    print(f'\n\033[35m{categoria}\033[0m')

    for nome, valor in produto.items():
        print(f'{nome}: {valor:.2f}$')
    variavel[categoria] = produto  # adicionando produtos na variavel
print('')
qtd_input = input('Quantos produtos deseja adicionar? ')

while not qtd_input.isnumeric():  # Verificando
    qtd_input = input('Somente números: ')
    print('')
else:
    for x in range(int(qtd_input)):  # Laço de acordo com a quantidade de produtos adicionados
        user_input = input('Produto Desejado: ')

        for chave_contida, valor_contido in variavel.items():  # Itera sobre os valores guardados dentro da Variavel
            for v_key, v_value in valor_contido.items():  # Separando valores novamente
                if str(user_input) == v_key:  # Verificando se o que o usuário é igual a chave
                    quantidade_produtos_adicionados += 1  # Adicionando quantidade de produtos a cada chave igual
                    produtos_adicionados.append(user_input)  # Adicionando na lista os produtos adicionados
                    soma_total += v_value  # Somando valores adicionados

# exibindo informações
print('---------------------------------------------')
print(f'Quantidade de itens adicionados: {quantidade_produtos_adicionados}')
print(f'Produtos adicionados: \033[32m{produtos_adicionados}\033[0m')
print(f'O total que você irá pagar é: \033[31mR${soma_total:.2f}\033[0m')
print('---------------------------------------------')

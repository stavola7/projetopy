nome=input("Insira o nome do Cliente: ")
endereco=input("Insira o endereço do Cliente ")
print("Olá", nome, "Bem vindo a empresa Thomas Turbando!")
# Lista de itens com peças de carros e motos
itens_disponíveis_carros = [
    {"item": "Pneu de Carro", "preço": 200.00},
    {"item": "Pastilha de Freio de Carro", "preço": 50.00},
    {"item": "Óleo de Motor de Carro", "preço": 30.00},
    {"item": "Filtro de Ar de Carro", "preço": 15.00},
    {"item": "Vela de Ignição de Carro", "preço": 8.00},
    {"item": "Amortecedor de Carro", "preço": 150.00},
]
itens_disponíveis_motos = [
    {"item": "Pneu de Moto", "preço": 100.00},
    {"item": "Pastilha de Freio de moto", "preço": 50.00},
    {"item": "Óleo de Motor de Moto", "preço": 30.00},
    {"item": "Filtro de Ar de Moto", "preço": 15.00},
    {"item": "Vela de Ignição de moto", "preço": 8.00},
    {"item": "Corrente de Moto", "preço": 40.00},
]

# Crie uma lista vazia para armazenar os itens do carrinho de compras
carrinho = []

while True:
    # Exibe o menu de opções
    print("\nMenu:")
    print("1. Produtos")
    print("2. Adicionar Item(s) da Lista de Produtos de Carro ao Carrinho")
    print("3. Adicionar Item(s) da Lista de Produtos de Moto ao Carrinho")
    print("4. Total a Pagar")
    print("5. Meio de Pagamento")
    print("6. Sair")

    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção (1/2/3/4/5): ")
    
    if escolha == "1":
        print("1. Produtos de carros")
        print("2. Produtos de motos")
        escolha_categoria = input("Escolha quais produtos disponiveis voce quer ver (1 para de carros, 2 para de motos): ")
        if escolha_categoria == "1":
            for idx, item in enumerate(itens_disponíveis_carros, start=1):
                print(f"{idx}. {item['item']} - R${item['preço']}")
        elif escolha_categoria == "2":
            for idx, item in enumerate(itens_disponíveis_motos, start=1):
                print(f"{idx}. {item['item']} - R${item['preço']}")

    if escolha == "2":
        # Adicionar Item(s) de moto ao Carrinho
        if len(itens_disponíveis_carros,) == 0:
            print("Não há itens disponíveis.")
        else:
            print("\nItens disponíveis para adicionar ao carrinho:")
            for idx, item in enumerate(itens_disponíveis_carros, start=1):
                print(f"{idx}. {item['item']} - R${item['preço']}")

            while True:
                escolha_item = input("Escolha o número do item que deseja adicionar ao carrinho (ou '0' para sair): ")
                if escolha_item == '0':
                    break
                try:
                    escolha_item = int(escolha_item)
                    if 1 <= escolha_item <= len(itens_disponíveis_carros,):
                        item_selecionado = itens_disponíveis_carros[escolha_item - 1]
                        carrinho.append(item_selecionado)
                        print(f"{item_selecionado['item']} adicionado ao carrinho.")
                    else:
                        print("Opção inválida. Tente novamente.")
                except ValueError:
                    print("Opção inválida. Tente novamente.")

    elif escolha == "3": 
        # Adicionar Item(s) de moto ao Carrinho
        if len(itens_disponíveis_motos,) == 0:
            print("Não há itens disponíveis.")
        else:
            print("\nItens disponíveis para adicionar ao carrinho:")
            for idx, item in enumerate(itens_disponíveis_motos, start=1):
                print(f"{idx}. {item['item']} - R${item['preço']}")

            while True:
                escolha_item = input("Escolha o número do item que deseja adicionar ao carrinho (ou '0' para sair): ")
                if escolha_item == '0':
                    break
                try:
                    escolha_item = int(escolha_item)
                    if 1 <= escolha_item <= len(itens_disponíveis_motos,):
                        item_selecionado = itens_disponíveis_motos[escolha_item - 1]
                        carrinho.append(item_selecionado)
                        print(f"{item_selecionado['item']} adicionado ao carrinho.")
                    else:
                        print("Opção inválida. Tente novamente.")
                except ValueError:
                    print("Opção inválida. Tente novamente.")
    
    elif escolha == "4":
        # Total a Pagar
        total = sum(item['preço'] for item in carrinho)
        print(f"Total a pagar: R${total:.2f}")
    
    elif escolha == "5":
        # Meio de Pagamento
        print("\nMeio de Pagamento:")
        print("1. Dinheiro")
        print("2. Cartão")
        escolha_pagamento = input("Escolha o meio de pagamento (1 para dinheiro, 2 para cartão): ")

        if escolha_pagamento == "1":
            print("Tudo certo ",nome,"seu pagamento em dinheiro foi recebido. Troco a ser calculado, caso precise. Embalando produtos para entregar em ",endereco)
            break
        elif escolha_pagamento == "2":
            cartao = input("Escolha a forma de pagamento (C para crédito, D para débito): ").upper()
            if cartao == "C":
                print("Pagamento com cartão de crédito aprovado. Embalando produtos para serem entregues em ",endereco)
                break
            elif cartao == "D":
                print("Pagamento com cartão de débito aprovado. Embalando produtos para serem entregues em ",endereco)
                break
            else:
                print("Opção de pagamento inválida.")
        else:
            print("Opção de meio de pagamento inválida.")

    elif escolha == "6":
        # Sair do programa
        print("Obrigado por comprar conosco! Tenha um bom dia.")
        break

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome

from pprint import pprint

def func_cadastro_usuario() -> list:
    
    salario_valido = False
    bonus_valido = False

    usuarios : list= []


    while True:

        nome_valido = False
        while not nome_valido:
            try:
                nome = input("Digite seu nome: ")

                # Verifica se o nome está vazio
                if len(nome) == 0:
                    raise ValueError("O nome não pode estar vazio.")
                # Verifica se há números no nome
                elif any(char.isdigit() for char in nome):
                    raise ValueError("O nome não deve conter números.")
                else:
                    print("Nome válido:", nome)
                    nome_valido = True
            except ValueError as e:
                print(e)


        try:
            salario = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")
            exit()

        # Solicita ao usuário que digite o valor do bônus recebido e converte para float
        try:
            bonus = float(input("Digite o valor do bônus recebido: "))

            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")
            exit()

        bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI


        dicionario_usuario :dict = {"nome":nome,"salario":salario,"bonus":bonus_recebido}

        usuarios.append(dicionario_usuario)


        # Imprime as informações para o usuário
        #print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

        continuar = input("Deseja continuar S/N")
        if continuar!="S":
            break
    return usuarios
    


usuarios =func_cadastro_usuario()

usuarios_agregados = [usuario['nome'] for usuario in usuarios ]
print(usuarios_agregados)
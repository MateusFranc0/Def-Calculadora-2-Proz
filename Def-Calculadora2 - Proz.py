"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema 
deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""

menu="""
        Selecione a operação desejada:
        [1] Soma
        [2] Subtração
        [3] Multiplicação
        [4] Divisão
        [0] Sair
        ==>"""

def calculadora():
    while True:
        opcao = input(menu)
        
        if opcao == "0":
            break
        elif opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe")
            continue

        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))

        if opcao == "1":
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("Não é possível dividir por zero")
            else:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")

calculadora()

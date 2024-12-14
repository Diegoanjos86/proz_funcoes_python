def calculadora():
    while True:
        print("\nBem-vindo à Calculadora!")
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == "5":
            print("Encerrando a calculadora. Até mais!")
            break
        
        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Certifique-se de inserir números.")
                continue
            
            if opcao == "1":
                resultado = num1 + num2
                operacao = "Soma"
            elif opcao == "2":
                resultado = num1 - num2
                operacao = "Subtração"
            elif opcao == "3":
                resultado = num1 * num2
                operacao = "Multiplicação"
            elif opcao == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    operacao = "Divisão"
                else:
                    print("Erro: Divisão por zero!")
                    continue
            
            print(f"Operação: {operacao}")
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida! Escolha entre 1 e 5.")


calculadora()

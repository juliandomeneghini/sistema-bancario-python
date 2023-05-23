def exibir_menu():
    print("===== Sistema de Banco =====")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    exibir_menu()
    opcao = input("Entre com a opção desejada: ")
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "2":
        
        valor = float(input("Informe o valor do depósito: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato == f"Saque: R$ {valor:.2f}\n"
            
        else:
            print("Operação inválida! O valor informado é inválido.")
            
    elif opcao == "3":
        print("\n ======================== EXTRATO ========================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=============================================================")
    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        
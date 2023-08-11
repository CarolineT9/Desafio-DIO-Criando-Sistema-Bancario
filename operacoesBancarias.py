menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3



while True:
    
    print(menu)
    opcao=input("Opção: ")


    if opcao == "d":
        
        deposito = float(input("Valor do depósito: "))
        
        if deposito > 0:
           saldo += deposito
           extrato += f"Depósito: R${deposito:.2f}\n"
           
        else:
            print("Operação inválida, valor negativo deposito informado...")
        
    elif opcao == "s":
       saque=float(input("Valor a sacar: "))
       
       excedeu_saldo = saque > saldo
       excedeu_limite = saque > limite
       excedeu_saques = numero_saques > LIMITE_SAQUE
       
       if excedeu_saldo:
           print("Saldo insuficiente")
           
       elif excedeu_limite:
           print("Limite  diário de 500 reais ")
           
       elif excedeu_saques:
           print("Número de saques diários excedidos.")
                       
       elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
    elif opcao == "e":
        print("\n ================================ EXTRATO ================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================================================")
        
    elif opcao == "q":    
        break
        
    else:
        print("Operação inválida, tente umas das opções disponíveis no menu")

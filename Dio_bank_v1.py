# Sistema Bancario desafio Dio Pro Bootcamp Python Developer
# 03 saques diários limitados a R$500,00, por dia
# Caso o usuário não tenha saldo deverá exibir uma mensagem
# Só poderá ter entradas positivas
# Todos os saques e depósitos deverão aparecer no extrato, formatados no modelo R$xxx.xx


saldo = 0
limite = 500
extrato = ""
menu = """""
[D] Depositar
[S] Sacar
[E] Exibir extrato
[F] Finalizar a Operacao
"""
quantidade_saque = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Qual valor deseja depositar?"))
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao nao concluida, tente novamente")
                
    elif opcao == "S":
        valor = float(input("Insira o valor desejado"))
        excedeu_valor = valor > saldo   
        excedeu_limite = valor > limite
        excedeu_saques = quantidade_saque > limite_saque
        if excedeu_valor:
            print("Saldo insuficiente, tente novamente")
        elif excedeu_limite:
            print("Limite insuficiente, tente novamente")
        elif excedeu_saques:
            print("Limite de saque diario atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saque += 1
        else:
            print("Falha na operacao, o valor informado e invalido")

    elif opcao == "E":
        print("\n============EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
        
    elif opcao == "F":
        print("Nos do banco GQ agradecemos pela confianca")
        break    
    else:
        print("Operacao invalida, tente novamente")
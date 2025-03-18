#Códigos feitos por mim e modificados pelo 
#Github Copilot para funcionarem em conjunto
#%Votos Válidos
def calcular_salario_mensal():
    Rm = float(input("Renda Mensal (Salário Mensal): "))
    H = float(input("Horas de trabalho semanal: "))
    emH = (Rm * 12) / (H * 52)
    print("Salário por hora:", emH)

#%Abstenção
def calcular_salario_anual():
    Ra = float(input( "Renda Anual (Salario Anual): " ))
    H = float(input( "Horas trabalho semanal: " ))
    eaH = (Ra / 14) * 12 / (H *52)
    print( "Salario por hora:", eaH)

#%Menu criado com ajuda do Github Copilot
def menu():
    print("Selecione uma opção:")
    print("1. Renda Mensal")
    print("2. Renda Anual")
    print("0. Sair")
    
    escolha = int(input("Digite o número da opção desejada: "))
    return escolha

while True:
    opcao = menu()
    
    if opcao == 1:
        calcular_salario_mensal()
    elif opcao == 2:
        calcular_salario_anual()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
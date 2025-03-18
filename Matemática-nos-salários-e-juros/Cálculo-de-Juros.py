#Códigos feitos por mim e modificados pelo 
#Github Copilot para funcionarem em conjunto
#Juros Simples
def juro_simples():
    Ci = float(input("Capital Inicial: "))
    r = float(input("Taxa de Juro (%): "))
    n = float(input("N° de anos: "))
    Js = Ci * ( r / 100 ) * n
    Cfs = Ci + Js
    print("Juro ao fim de", n, "anos: ", Js)
    print("Capital acumulado ao fim de", n, "anos: ", Cfs)

#Juros Compostos
def juros_compostos():
    Ci = float(input("Capital Inicial: "))
    r = float(input("Taxa de Juro (%): "))
    n = float(input("N° de anos: "))
    Jc = Ci * ( 1 + ( r / 100 )) ** n - Ci
    Cfc = Ci + Jc
    print("Juro ao fim de", n, "anos: ", Jc)
    print("Capital acumulado ao fim de", n, "anos: ", Cfc)

#Juros Capital Mensal
def juros_capital_mensal():
    Ci = float(input("Capital Inicial: "))
    r = float(input("Taxa de Juro anual(%): "))
    n = float(input("N° de anos: "))
    Jcm = Ci * (1 + (( r / 100)/12)) ** n - Ci
    Cfm = Ci + Jcm
    print("Juro ao fim de", n, "anos: ", Jcm)
    print("Capital acumulado ao fim de", n, "anos: ", Cfm)

#%Menu criado com ajuda do Github Copilot
def menu():
    print("Selecione uma opção:")
    print("1. Juros Simples")
    print("2. Juros Compostos")
    print("3. Juros Capital Mensal")
    print("0. Sair")
    
    escolha = int(input("Digite o número da opção desejada: "))
    return escolha

while True:
    opcao = menu()
    
    if opcao == 1:
        juro_simples()
    elif opcao == 2:
        juros_compostos()
    elif opcao == 3:
        juros_capital_mensal()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
#Códigos feitos por mim e modificados pelo 
#Github Copilot para funcionarem em conjunto
#%Votos Válidos
def votos_validos():
    Vv = float(input("Nº de votos válidos "))
    Tv = float(input("Nº total de votos "))
    P = Vv / Tv * 100
    print("Percentagem de votos válidos ", P)

#%Abstenção
def abstencao():
    N = float(input("Eleitores Inscritos "))
    V = float(input("Nº Total de votos "))
    P = (N - V) / N * 100
    print("Percentagem Abstenção", P)

#%Votos Nulos
def votos_nulos():
    Vn = float(input("Nº de votos nulos "))
    Tv = float(input("Nº total de votos "))
    P = Vn / Tv * 100
    print("Percentagem de votos nulos ", P)

#%Menu criado com ajuda do Github Copilot
def menu():
    print("Selecione uma opção:")
    print("1. Calcular percentagem de votos válidos")
    print("2. Calcular percentagem de abstenção")
    print("3. Calcular percentagem de votos nulos")
    print("0. Sair")
    
    escolha = int(input("Digite o número da opção desejada: "))
    return escolha

while True:
    opcao = menu()
    
    if opcao == 1:
        votos_validos()
    elif opcao == 2:
        abstencao()
    elif opcao == 3:
        votos_nulos()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

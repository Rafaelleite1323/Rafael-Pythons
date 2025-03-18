import math

def determine_axis_of_symmetry(h):
    return "x = {}".format(h)

def determine_vertex(a, h, k):
    return (h, k)

def determine_concavity(a):
    if a > 0:
        return "A concavidade é voltada para cima."
    elif a < 0:
        return "A concavidade é voltada para baixo."
    else:
        return "A função não é uma parábola, pois a = 0."

def determine_codomain(a, k):
    if a > 0:
        return "[{}, +∞[".format(k)
    elif a < 0:
        return "]-∞, {}]".format(k)
    else:
        return "A função não é uma parábola, pois a = 0."

def determine_sign(a, h, k):
    if a > 0:
        return "A função é negativa para x fora do intervalo [{}, +∞) e positiva para x dentro do intervalo [{}, +∞).".format(h, h)
    elif a < 0:
        return "A função é positiva para x fora do intervalo [{}, +∞) e negativa para x dentro do intervalo [{}, +∞).".format(h, h)
    else:
        return "A função não é uma parábola, pois a = 0."

def determine_roots(a, h, k):
    if a == 0:
        return "A função não é uma parábola, pois a = 0."
    
    discriminant = -k / a
    if discriminant < 0:
        return "A função não tem raízes reais (zeros)."
    elif discriminant == 0:
        root = h
        return "A função tem uma raiz dupla: x = {}".format(root)
    else:
        root1 = h + math.sqrt(discriminant)
        root2 = h - math.sqrt(discriminant)
        return "As raízes da função são: x1 = {}, x2 = {}".format(root1, root2)

def determine_monotonicity(a, h):
    if a > 0:
        return "A função é decrescente para x < {} e crescente para x > {}.".format(h, h)
    elif a < 0:
        return "A função é crescente para x < {} e decrescente para x > {}.".format(h, h)
    else:
        return "A função não é uma parábola, pois a = 0."

def determine_extremes(a, h, k):
    if a > 0:
        return "A função tem um mínimo no vértice: ({}, {})".format(h, k)
    elif a < 0:
        return "A função tem um máximo no vértice: ({}, {})".format(h, k)
    else:
        return "A função não é uma parábola, pois a = 0."

# Exemplo de uso
a = float(input("Digite o valor de a: "))
h = float(input("Digite o valor de h: "))
k = float(input("Digite o valor de k: "))

axis_of_symmetry = determine_axis_of_symmetry(h)
vertex = determine_vertex(a, h, k)
concavity = determine_concavity(a)
codomain = determine_codomain(a, k)
sign_info = determine_sign(a, h, k)
roots = determine_roots(a, h, k)
monotonicity = determine_monotonicity(a, h)
extremes = determine_extremes(a, h, k)

print("O eixo de simetria é: {}".format(axis_of_symmetry))
print("As coordenadas do vértice são: {}".format(vertex))
print(concavity)
print("O contradomínio é: {}".format(codomain))
print(sign_info)
print(roots)
print(monotonicity)
print(extremes)
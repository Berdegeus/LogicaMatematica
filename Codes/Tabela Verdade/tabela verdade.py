import itertools

# definir operadores lógicos
def E(*args):
    return all(args)

def OU(*args):
    return any(args)

def NAO(a):
    return not a

def OU_EXCLUSIVO(a, b):
    return (a and not b) or (not a and b)

# obter entrada do usuário
n = int(input("Número de Variáveis: "))
opcoes_operacao = ["E", "OU", "NÃO", "OU_EXCLUSIVO"]
operacao = input("Operação: " + ", ".join(opcoes_operacao) + "\n").upper()

# verificar entrada do usuário
if operacao not in opcoes_operacao:
    print("Operação inválida.")
    exit()

# gerar tabela verdade
print()
for i in range(n):
    print(f"{'A' if i == 0 else chr(65+i)}", end="\t")
print("Resultado")
print("-" * (n*8 + 9))
for values in itertools.product((True, False), repeat=n):
    resultado = None
    if operacao == "E":
        resultado = E(*values)
    elif operacao == "OU":
        resultado = OU(*values)
    elif operacao == "NÃO":
        resultado = NAO(values[0])
    elif operacao == "OU_EXCLUSIVO":
        resultado = OU_EXCLUSIVO(*values)
    for value in values:
        print(str(value), end="\t")
    print(str(resultado))

# obter entrada do usuário
operacao = input("Operação: E, OU, NAO, OU_EXCLUSIVO\n").upper()

# verificar entrada do usuário
if operacao not in ["E", "OU", "NAO", "OU_EXCLUSIVO"]:
    print("Operação inválida.")
    exit()

# gerar tabela verdade
print("A\tB\tResultado")
print("-" * 23)
for A in (True, False):
    for B in (True, False):
        resultado = None
        if operacao == "E":
            resultado = A and B
        elif operacao == "OU":
            resultado = A or B
        elif operacao == "NAO":
            resultado = not A
        elif operacao == "OU_EXCLUSIVO":
            resultado = (A and not B) or (not A and B)
        print(str(A) + "\t" + str(B) + "\t" + str(resultado))

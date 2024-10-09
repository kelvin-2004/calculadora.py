operadores = {"soma", "subtracao", "divisao", "divisao_real", "multiplicacao", "potenciacao"}

print(operadores)

operador = input("Selecione o operador que você deseja: ")
n1 = float(input("Escolha o primeiro número: "))
n2 = float(input("Escolha o segundo número: "))

def operacao(n1, n2, operador):
    if operador == "soma":
        return n1 + n2
    elif operador == "subtracao":
        return n1 - n2
    elif operador == "divisao":
        return n1 / n2
    elif operador == "divisao_real":
        return n1 % n2
    elif operador == "multiplicacao":
        return n1 * n2
    elif operador == "potenciacao":
        return n1 ** n2
    else:
        return "Operador inválido"

resultado = operacao(n1, n2, operador)
print(f"O resultado da {operador} é: {resultado}")

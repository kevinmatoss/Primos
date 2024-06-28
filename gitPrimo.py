def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é primo e exibir a mensagem correspondente
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

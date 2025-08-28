while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n > 0:
        break
    print("Por favor, digite apenas números positivos.")

soma = 0
for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")


# agora para os divisores

while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n > 0:
        break
    print("Por favor, digite apenas números positivos.")

print(f"Divisores positivos de {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
'''for i in range(1, 11):
    for j in range(1, 11):
        multi = i * j

        print(f"{i} x {j} = {multi}")
    print("----------------------------------")

numero = int(input("Digite um numero inteiro positivo "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")'''

x = 1
y = 1

'''while x <= 10:
    while y <= 10:
        multi = x * y

        print(f"{x} x {y} = {multi}")

        y += 1
    print("----------------------------------")

    x += 1
    y = 1'''

acumulador_notas = 0
voltas = 0

while True:
    nota = input("Digite a nota: ")

    if nota not in "012345678910":
        print("Numero não encontrado")
    else: 
        nota = float(nota)

        if nota >= 0 and nota <= 10:
            acumulador_notas += nota
            voltas += 1

            escolha = input("Quer adicionar mais uma nota?(s/n) ")

            if escolha.lower() == 'n' or escolha.lower() == 'não':
                break
        else: 
            print("Notas apenas entre 0 e 10")

media = acumulador_notas / voltas

print(media)
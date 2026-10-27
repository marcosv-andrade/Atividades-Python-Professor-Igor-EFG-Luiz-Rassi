# 12. Comparando Dois Números: Peça ao usuário dois números (n1 e n2). O
# programa deve dizer qual deles é o maior ou se são iguais.

n1 = int(input("Diga o primeiro numero"))
n2 = int(input("Diga o segundo numero"))
if n1 > n2:
    print(f"O primeiro numero é maior que o segundo")
elif n1 < n2:
    print(f" O segundo numero é maior que o primeiro")
elif n1 == n2:
    print(f"Os dois são iguais")


         
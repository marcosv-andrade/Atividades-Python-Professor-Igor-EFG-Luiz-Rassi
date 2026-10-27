# 18. Diálogo de RPG: Crie um menu onde o jogador escolhe entre 1 (Falar), 2 (Atacar)
# ou 3 (Fugir). Use if/elif/else para exibir uma resposta diferente para cada
# escolha.
falar = 1
atacar = 2
fugir = 3
int(input("Digite 1 para falar, 2 para atacar e 3 para fugir"))
if falar:
    print(f"voce atacou")
elif atacar:
    print(f"voce atacou")
else:
    print(f"fugiu")


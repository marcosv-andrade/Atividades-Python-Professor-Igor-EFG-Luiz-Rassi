# 17. Evolução de Nível: Se os pontos do jogador forem maiores que 1000, mude a
# variável nivel para 2 e dê um bônus de 100 de vida.

pontos = int(input("Quantos pontos de vida"))
if pontos > 1000:
    pontos = pontos + 100
    print(pontos)
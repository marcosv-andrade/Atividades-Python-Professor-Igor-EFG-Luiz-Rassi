# 19. Limite de Inventário: O jogador quer pegar um item de peso 5. Verifique se o
# peso_atual + 5 ultrapassa o limite_maximo de 50. Se ultrapassar, imprima
# "Inventário Cheio!".
peso_atual = int(input("Qual peso do seu inventario? "))
if peso_atual + 5 >= 50: 
    print(f"seu inventario ta cheio")
# 20. Desafio de Coordenadas: No Godot, queremos evitar que o personagem saia da
# tela. Se a posicao_x for menor que 0 ou maior que 1024, imprima "Atenção: Saindo
# da tela!".
posicao_x = int(input("Qual sua posicao"))
if posicao_x < 0 or posicao_x >= 1024:
    print(f"Atenção: Saindo da tela!")
# 19. Simulador de Compra: -  Use o  print()  para mostrar o preço de uma poção (10  moedas). -Use o  input()  para perguntar quantas poções o jogador  quer. -Calcule o total e use o  print()  para mostrar o valor  da fatura. 
pocao_preco = 10

print(f"a pocao custa {pocao_preco} moedas")

pocao_quant = int(input("Quantas poções você quer?" ))

total = pocao_preco * pocao_quant

print(f"O total foi {total}")

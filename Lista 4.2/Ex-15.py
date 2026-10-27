# 15. A Chave e a Porta: Crie duas variáveis: tem_chave (booleana) e
# distancia_porta (inteiro). O código só deve imprimir "Porta Aberta!" se o jogador
# tiver a chave E a distância for menor que 2.

tem_chave = input("Possui a chave: ") 
if tem_chave == "sim" or tem_chave== True:
    print(f"acesso permitido")
else:
    print(f"ACESSO NEGADO")

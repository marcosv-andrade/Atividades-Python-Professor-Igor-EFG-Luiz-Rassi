# 16. Verificação de Inventário: O limite de peso de um inventário é 50kg. O jogador
# está carregando 48kg e tenta pegar um item de 3kg. Use operadores para verificar se
# o novo peso será menor ou igual ao limite.

limite_peso = 50
jogador_peso = 48
item_pegado = 3
peso_novo = jogador_peso + item_pegado
mochila_cheia = peso_novo <= limite_peso

print(mochila_cheia)

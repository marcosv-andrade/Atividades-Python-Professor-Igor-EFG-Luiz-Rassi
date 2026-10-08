""" 8. Primeiro Comando:  Escreva um codigo em Python que  utilize a função de saída para exibir a mensagem: "Sistema de Jogo Iniciado..."."""
print("Sistema de jogo iniciado")

""" 9. Entrada de Dados:  Escreva uma linha de codigo que  peca ao usuário para digitar o 
nome do seu personagem e armazene isso em uma variavel chamada  heroi """
heroi = input("Escolha o  nome do seu heroi: ")


"""10. Processamento Simples:  Crie um script que receba  um número (Entrada), 
multiplique esse número por 2 (Processo) e mostre o resultado (Saída). """
numero = int(input("digite seu numero: "))
soma = numero * 2
print(f"A soma é: {soma}")

""" 11. Fluxo Completo de Soma:  Escreva um programa que  peça dois números ao 
jogador, some-os e exiba: "A pontuação total é: [resultado]"."""
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo Numero: "))
resultado = numero1 + numero2
print(f"A pontuação total é: {resultado}")

"""12. Comentários de Organização:  Pegue o código abaixo  e adicione comentários 
explicando o que é a  Entrada  , o  Processo  e a  Saída  :"""
v1 = int(input("Vida atual: ")) #Entrada pois aqui se colocam os dados
v2 = v1 - 10  #Processo pois aqui que oe processador processa esses dados
print("Nova vida:", v2) # Aqui é a saida pois é que é mostrado na tela para o usuario

"""13. Manipulação de Texto:  Crie um algoritmo em Python  que receba o nome de um 
reino e exiba: "Bem-vindo ao Reino de [Nome do Reino]!"""
nome_do_reino = input("Qual será  o nome do seu reino: ")
print(f"Bem vindo ao Reino: {nome_do_reino}")       

"""14. Lógica de Dano:  Um inimigo tem 50 pontos de vida.  O jogador causou 15 pontos 
de dano. Escreva a lógica (os passos) que o computador deve seguir para atualizar a 
vida do inimigo."""
#O inimigo tem 50 pontos de vida
#jogador = 15
#vida_final =  inimigo - jogador 
#jogador causou 15 pontos ou seja: print(f"A vida restante é de: {vida_final}")

"""15. O Problema da Sequência:  O código abaixo apresenta  um erro de lógica na 
estrutura básica. O que está errado? 
Python 
print("O resultado da soma é:", total) 
n1 = 5 
n2 = 10 
total = n1 + n2 """

#O erro é que a variavel total esta depois do comando print("O resultado da soma é:", total) , ou seja o ocmputador nao vai saber qual a  variavel total.

"""16. Algoritmo de Movimento:  Se o personagem está na  posição  X = 0  e o jogador 
aperta a "Seta Direita", o personagem deve andar 5 passos. Desenhe ou escreva o 
algo
ritmo para essa ação."""
#jogador = x = 0#
#jogador = x + 5#

"""18. Pensamento Estruturado:  Como você explicaria para  um robô (que só entende 
ordens exatas) o algoritmo para "Abrir uma porta que está trancada"?""" 

#Passo a Passo: Veirificar se a porta esta aberta, senão destrancar a porta, se a porta foi destrancada entre na porta, senão procure a chave e tente destrancar a porta novamente.


"""19. Variáveis na Lógica:  Por que a etapa de  Processamento  geralmente depende de 
Variáveis  criadas na etapa de  Entrada  ? """
 #Resposta: Para a estapa de processamentos ter dados para processar.#

"""20. Desafio Final:  Crie um algoritmo completo em Python  que: 
1.  Peça o nome do jogador. 
2.  Peça o nível atual do jogador. 
3.  Calcule o próximo nível (Nível + 1). 
4.  Exiba uma mensagem motivadora: "Parabéns [Nome], seu próximo objetivo é o 
nível [Nível + 1]!"."""

nome = input("Qual seu nickname?")
nivel = int(input("Qual seu nivel de jogador"))
proximo_nivel = nivel + 1
print(f"Parabéns {nome} seu próximo objetivo é o nível {proximo_nivel}")
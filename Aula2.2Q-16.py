#Operacao e Saida : Peca ao jogador quanto de "Dano" ele recebeu e quanto de "Defesa" ele tem. Subtraia um do outro e mostre o resultado final do dano real#

dano = int(input("Quanto de dano voce  recebeu? "))

defesa = int(input("Qual de DEFESA voce tem? "))

resultado_final_dano = dano - defesa

print(f"O dano real foi de {resultado_final_dano}")

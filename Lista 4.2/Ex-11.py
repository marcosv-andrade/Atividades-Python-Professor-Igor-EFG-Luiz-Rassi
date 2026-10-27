# 11. Sistema de Notas: Crie um programa que receba a nota de um aluno:
# ● Se for 7 ou mais: "Aprovado".
# ● Se for entre 5 e 6.9: "Recuperação".
# ● Se for menor que 5: "Reprovado".

nota_aluno = float(input("qual sua nota"))
if nota_aluno >= 7:
    print("aprovado")
elif nota_aluno >= 5 and nota_aluno <= 6.9:
    print ("Recuperação")
else:
    print(f"reprovado")    
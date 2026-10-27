# 9. Teste de Maioridade: Crie um script que peça a idade do usuário. Se for 18 ou
# mais, exiba "Acesso Liberado ao Jogo". Caso contrário, exiba "Acesso Negado".

usuario_idade = int(input("Qual sua idade"))
if usuario_idade > 18: 
    print(f"Acesso Liberado ao jogo")
else:
    print(f"Acesso Negado")    

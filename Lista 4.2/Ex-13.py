# 13. Validação de Login: Crie uma variável senha_mestra = "python123". Peça
# ao usuário para digitar uma senha e use um if para verificar se ele acertou.

senha_mestra = "python123"

usuario = input("Tente acertar  a senha")
if usuario == senha_mestra:
    print(f"Voce acertou a senha")
else:
    print(f"Você errou a senha")



#15 Ficha RPG: peça tres informacoes ao usuario: Nome, Nivel(int) e se tem Magia (bool). Depois, use o print() para mostrar tudo formatado em uma unica linha)
nome = input("Qual seu nome")
nivel  = int(input("Qual seu nivel"))
magia = bool(input("Tem magia"))

print(f"Você tem os seguintes atributos: {nome} {nivel} {magia}")
# Criando uma lista
animais = ["cavalo", "galo", 1, 2, 3]

# Sobrepor
animais = ["cachorro", "gato", 12345, 6.5]
print(animais)

# Imprimindo um elemento da lista
print(animais[0])

# Substituindo um elemento da lista
animais[0] = "papagaio"
print(animais)

# Removendo item da lista
animais.remove("gato")
print(animais)

# Tamanho da lista
print(len(animais))

# Verificando se existe na lista
print("gato" in animais)

numericos = [500, 30, 300, 80, 10]  # nova lista

# Pegar o maior elemento da lista
print(max(numericos))

# Pegar o menor elemento da lista
print(min(numericos))

# adicionar elemento na lista
animais.append("Leao")
print(animais)

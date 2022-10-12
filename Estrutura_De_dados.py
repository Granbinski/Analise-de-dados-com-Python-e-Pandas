# LISTAS
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

numericos = [1.5, 500, 30, 300, 80, 10]  # nova lista

# Pegar o maior elemento da lista
print(max(numericos))

# Pegar o menor elemento da lista
print(min(numericos))

# adicionar um elemento na lista ou outra lista
animais.append("Leao")  # append adiciona um unico elemento na lista
print(animais)
animais.append(["Grilo", 14])  # append adiciona uma lista dentro de outra
print(animais)

# Adicionar mais de um elemento na lista
animais.extend(["Cavalo", 10, "Carrapato"])
print(animais)

# Contando quantas vezes o elemento aprece na lista //count
print(animais.count("Cavalo"))

# Ordenar lista de numeros
numericos.sort()
print(numericos)

# TUPLAS
# As tuplas usam parenteses como sintaxe
tuplazinha = ("Banana", "Maca", 10, 50)

# Retornando o primeiro elemento
print(tuplazinha[0])

# Diferente das listas as tuplas sao imutaveis

# count e slice funcionam com tuplas

# DICIONARIOS

# Criando dicionarios
dicio = {"Maca": 20, "Banana": 10, "Laranja": 15, "Uva": 5}

# Podemos acessar os valores dos dicionarios atraves da chave
print(dicio["Maca"])

# Podemos atualizar o valor de usando a chave
dicio["Maca"] = 24

# Retornamdo todas as chaves do dicionario
print(dicio.keys())


# Retornamdo todas os chaves do dicionario
print(dicio.values())

# Verificando se ja existe uma chave no dicionario e caso nao exista inserir
dicio.setdefault("Limao", 22)
print(dicio)

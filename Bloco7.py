# 1. Criar e aceder a um dicionario
# Perguntar os dados
nome = input("Como te chamas? ")
idade = int(input("Quantos anos tens? "))
cidade = input("Onde moras? ")

# Criar o dicionário
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

# Aceder e imprimir cada valor pela sua chave
print("\nInformações disponíveis:")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")

# 2. Adicionar e remover entradas
# Dado um dicionário de frutas e os seus preços,constroi um ciclo while para adicionar e remover frutas.

frutas = {
    "maçã":  1.20,
    "banana": 0.80,
    "laranja": 0.95
}

while True:
    acao = input("Adicionar, remover ou sair? ").strip().lower()

    if acao == "adicionar":
        nome  = input("Nome da fruta: ")
        preco = float(input("Preço (€/Kg): "))
        frutas[nome] = preco
        print(f"✓ '{nome}' adicionada.")

    elif acao == "remover":
        nome = input("Nome da fruta: ")
        if nome in frutas:
            del frutas[nome]
            print(f"✓ '{nome}' removida.")
        else:
            print(f"✗ '{nome}' não existe.")

    elif acao == "sair":
        break

print("Dicionário final:", frutas)

# 3. Contar ocorrências de palavras Pede uma frase ao utilizador e conta quantas
# vezes cada palavra aparece, guardando o resultado num dicionário.
frase = input("Diz-me uma frase:").lower().strip().split()
frequencia = {}

for palavra in frase:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Frequência de palavras:", frequencia)

# 4. Turma e notas Dado um dicionário com nomes de alunos e as suas notas, calcula
# a média da turma, o aluno com melhor nota e o aluno com pior nota.
alunos = {"ana": 15, "joão": 12, "mariana": 17, "pedro": 10}

media = sum(alunos.values()) / len(alunos)
melhor = max(alunos.items(), key=lambda x: x[1])
pior = min(alunos.items(), key=lambda x: x[1])

print("Média da turma:", media)
print("Melhor aluno:", melhor[0], "com nota", melhor[1])
print("Pior aluno:", pior[0], "com nota", pior[1])

# 5. Inventário de loja 
# Cria um inventário de produtos com nome e quantidade.
# Permite adicionar stock, vender unidades e avisar quando um produto tiver menos
# de 5 unidades.
produtos = {
    "pão": 12,
    "leite": 32,
    "queijo": 45
}
STOCK_MINIMO = 5

while True:
    acao = input("\nadicionar, vender, remover, inventário ou sair: ").strip().lower()
    if acao == "adicionar":
        nome = input("Nome do produto: ").strip().lower()
        quantidade = int(input("Quantidade a adicionar: "))
        if nome in produtos:
            produtos[nome] += quantidade          # soma ao stock existente
        else:
            produtos[nome] = quantidade           # cria novo produto
        print(f"{nome} → stock atual: {produtos[nome]} unidades.")

    elif acao == "vender":
        nome = input("Nome do produto: ").strip().lower()
        if nome not in produtos:
            print(f"{nome} não existe no inventário.")
        else:
            quantidade = int(input("Quantidade a vender: "))
            if quantidade > produtos[nome]:
                print(f"Stock insuficiente. Apenas {produtos[nome]} unidades disponíveis.")
            else:
                produtos[nome] -= quantidade          # subtrai do stock
                print(f"Vendidas {quantidade} unidades de {nome}.")
                if produtos[nome] < STOCK_MINIMO:
                    print(f"AVISO: {nome} tem apenas {produtos[nome]} unidades (mínimo: {STOCK_MINIMO})!")

    elif acao == "remover":
        nome = input("Nome do produto: ").strip().lower()
        if nome in produtos:
            del produtos[nome]
            print(f"{nome} removido do inventário.")
        else:
            print(f"{nome} não existe.")

    elif acao == "inventário":
        print("\nInventário atual")
        for nome, qtd in produtos.items():
            aviso = " ⚠ STOCK BAIXO" if qtd < STOCK_MINIMO else ""
            print(f"{nome}: {qtd} unidades{aviso}")

    elif acao == "sair":
        break
    else:
        print("Ação inválida.")

print("\nInventário final:", produtos)

# 6. Ficha de alunos 
# Cria um dicionário de dicionários com informação de 3 alunos.
# Cada aluno tem nome, idade e nota. Escreve um programa que mostre a
# informação de cada aluno e no final diz qual tem a melhor nota. 

alunos = {
    "aluno1": {"nome": "Ana", "idade": 16, "nota": 18},
    "aluno2": {"nome": "Bruno", "idade": 17, "nota": 14},
    "aluno3": {"nome": "Carla", "idade": 15, "nota": 19}
}

# Mostrar informação de cada aluno
for aluno, dados in alunos.items():
    print(f"{aluno}")
    print(f"Nome:  {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"Nota:  {dados['nota']}/20")
    print("")

# Encontrar o aluno com melhor nota
melhor = max(alunos.values(), key=lambda d: d["nota"])
print(f"Melhor nota: {melhor['nome']} com {melhor['nota']}/20")

# 7. Agenda de contactos
agenda = {"Maria": "912 345 678", "João": "963 111 222"}

while True:
    acao = input("Ação (adicionar/procurar/remover/sair): ").strip().lower()

    if acao == "adicionar":
        nome = input("Nome: ").strip().title()
        tel  = input("Telefone: ").strip()
        agenda[nome] = tel
        print(f"{nome} adicionado.")

    elif acao == "procurar":
        nome = input("Nome: ").strip().title()
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print(f"{nome} não encontrado.")

    elif acao == "remover":
        nome = input("Nome: ").strip().title()
        if nome in agenda:
            del agenda[nome]
            print(f"{nome} removido.")
        else:
            print(f"{nome} não existe.")

    elif acao == "sair":
        break

# 8. Tradutor PT → EN
dicionario = {
    "gato": "cat", "cão": "dog", "casa": "house",
    "carro": "car", "livro": "book", "água": "water"
    # ...
}

while True:
    palavra = input("Palavra PT (ou 'sair'): ").strip().lower()
    if palavra == "sair":
        break
    if palavra in dicionario:
        print(f"→ {dicionario[palavra]}")
    else:
        print("Tradução não encontrada.")
        nova = input("Indicar tradução? (Enter para saltar): ").strip().lower()
        if nova:
            dicionario[palavra] = nova
            print(f"{palavra} → {nova} guardado.")

# EXTRA
# Usar tradutor online

# ! pip install deep-translator
try:
    from deep_translator import GoogleTranslator
    tradutor = GoogleTranslator(source="pt", target="en")
except ImportError:
    print("Módulo deep-translator não instalado. Corre: pip install deep-translator")
    tradutor = None

if tradutor:
    while True:
        palavra = input("Palavra PT (ou 'sair'): ").strip()
        if palavra == "sair":
            break
        traducao = tradutor.translate(palavra)
        print(f"→ {traducao}")

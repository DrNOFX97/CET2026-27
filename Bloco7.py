# 1. Criar e aceder a um dicionario
def dados_pessoais():
    nome = input("Como te chamas? ")
    idade = int(input("Quantos anos tens? "))
    cidade = input("Onde moras? ")

    # Criar o dicionário
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    print("\nInformações disponíveis:")
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade: {pessoa['cidade']}")

    return pessoa

# 2. Adicionar e remover entradas
def adicionar_remover_frutas():
    frutas = {
        "maçã":  1.20,
        "banana": 0.80,
        "laranja": 0.95
    }

    while True:
        acao = input("1. Adicionar, 2. Remover, 3. Sair")    

        if acao == "1":
            nome  = input("Nome da fruta: ")
            preco = float(input("Preço (€/Kg): "))
            frutas[nome] = preco
            print(f"'{nome}' adicionada.")

        elif acao == "2":
            nome = input("Nome da fruta: ")
            if nome in frutas:
                del frutas[nome]
                print(f"'{nome}' removida.")
            else:
                print(f"'{nome}' não existe.")

        elif acao == "3":
            break

    return frutas

# 3. Contar ocorrências de palavras
def contar_ocorrencias_palavras():
    frase = input("Diz-me uma frase: ").lower().strip().split()
    frequencia = {}

    for palavra in frase:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    print("Frequência de palavras:", frequencia)
    return frequencia

# 4. Turma e notas
def turma_e_notas():
    alunos = {"ana": 15, "joão": 12, "mariana": 17, "pedro": 10}

    media = sum(alunos.values()) / len(alunos)
    melhor = max(alunos.items(), key=lambda x: x[1])
    pior = min(alunos.items(), key=lambda x: x[1])

    print("Média da turma:", media)
    print("Melhor aluno:", melhor[0], "com nota", melhor[1])
    print("Pior aluno:", pior[0], "com nota", pior[1])

    return media, melhor, pior

# 5. Inventário de loja
def inventario_loja():
    produtos = {
        "pão": 12,
        "leite": 32,
        "queijo": 45
    }
    STOCK_MINIMO = 5

    while True:
        acao = input("\nadicionar, vender, remover, inventário ou sair: ")

        if acao == "adicionar":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            if nome in produtos:
                produtos[nome] += quantidade
            else:
                produtos[nome] = quantidade
            print(f"{nome} - stock atual: {produtos[nome]} unidades.")

        elif acao == "vender":
            nome = input("Nome do produto: ")
            if nome not in produtos:
                print(f"{nome} não existe no inventário.")
            else:
                quantidade = int(input("Quantidade a vender: "))
                if quantidade > produtos[nome]:
                    print(f"Stock insuficiente. Apenas {produtos[nome]} unidades disponíveis.")
                else:
                    produtos[nome] -= quantidade
                    print(f"Vendidas {quantidade} unidades de {nome}.")
                    if produtos[nome] < STOCK_MINIMO:
                        print(f"AVISO: {nome} tem apenas {produtos[nome]} unidades (mínimo: {STOCK_MINIMO})!")

        elif acao == "remover":
            nome = input("Nome do produto: ")
            if nome in produtos:
                del produtos[nome]
                print(f"{nome} removido do inventário.")
            else:
                print(f"{nome} não existe.")

        elif acao == "inventário":
            print("\nInventário atual")
            for nome, qtd in produtos.items():
                aviso = "STOCK BAIXO" if qtd < STOCK_MINIMO else ""
                print(f"{nome}: {qtd} unidades{aviso}")

        elif acao == "sair":
            break
        else:
            print("Ação inválida.")

    print("\nInventário final:", produtos)
    return produtos

# 6. Ficha de alunos
def ficha_de_alunos():
    alunos = {
        "aluno1": {"nome": "Ana", "idade": 16, "nota": 18},
        "aluno2": {"nome": "Bruno", "idade": 17, "nota": 14},
        "aluno3": {"nome": "Carla", "idade": 15, "nota": 19}
    }

    for aluno, dados in alunos.items():
        print(f"{aluno}")
        print(f"Nome:  {dados['nome']}")
        print(f"Idade: {dados['idade']} anos")
        print(f"Nota:  {dados['nota']}/20")
        print("")

    melhor = max(alunos.values(), key=lambda d: d["nota"])
    print(f"Melhor nota: {melhor['nome']} com {melhor['nota']}/20")

# 7. Agenda de contactos
contactos = {}

def remover_contactos():
    print("Contactos: ", contactos)
    nome = input("Nome: ")
    removido = contactos.pop(nome, None)
    if removido:
        print(f"{nome} removido.")
    else:
        print(f"{nome} não existe.")
    return contactos

def procurar_contactos():
    print("Contactos: ", contactos)
    nome = input("Nome: ")
    resultado = contactos.get(nome, "Não encontrado.")
    print(f"{nome}: {resultado}")
    return contactos

def adicionar_contactos():
    print("Contactos: ", contactos)
    nome = input("Nome: ")
    tel  = input("Telefone: ")
    contactos[nome] = tel
    print(f"{nome} adicionado.")
    return contactos

def agenda_de_contactos():
    while True:
        acao = input("Ação (1. Adicionar/2. Procurar/3. Remover/4. Sair): ").strip().lower()

        if acao == "1":
            adicionar_contactos()
        elif acao == "2":
            procurar_contactos()
        elif acao == "3":
            remover_contactos()
        elif acao == "4":
            break
        else:
            print("Ação inválida.")

    return contactos

# 8. Tradutor PT-EN
def tradutor_local():
    dicionario = {
        "gato": "cat", "cão": "dog", "casa": "house",
        "carro": "car", "livro": "book", "água": "water"
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

    return dicionario

# EXTRA - Tradutor online (Google)
# ! pip install deep-translator
def tradutor_online():
    try:
        from deep_translator import GoogleTranslator
        tradutor = GoogleTranslator(source="pt", target="en")
    except ImportError:
        print("Módulo não instalado. Corre: pip install deep-translator")
        return

    while True:
        palavra = input("Palavra PT (ou 'sair'): ").strip()
        if palavra == "sair":
            break
        traducao = tradutor.translate(palavra)
        print(f"→ {traducao}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Contar ocorrências de palavras")
        print("2. Turma e notas")
        print("3. Inventário de loja")
        print("4. Ficha de alunos")
        print("5. Agenda de contactos")
        print("6. Tradutor PT-EN")
        print("7. Tradutor Online (Google)")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            contar_ocorrencias_palavras()
        elif opcao == "2":
            turma_e_notas()
        elif opcao == "3":
            inventario_loja()
        elif opcao == "4":
            ficha_de_alunos()
        elif opcao == "5":
            agenda_de_contactos()
        elif opcao == "6":
            tradutor_local()
        elif opcao == "7":
            tradutor_online()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

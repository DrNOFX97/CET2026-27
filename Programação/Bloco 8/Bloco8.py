# 1. Ler ficheiro de texto
def ler_ficheiro():
    ficheiro = input("Nome do ficheiro: ").strip()
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            conteudo = f.read()
        print("\n--- Conteúdo ---")
        print(conteudo)
        print("--- Maiúsculas ---")
        print(conteudo.upper())
        print("--- Minúsculas ---")
        print(conteudo.lower())
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# 2. Escrever em ficheiro (cria ou sobrescreve)
def escrever_ficheiro():
    ficheiro = input("Nome do ficheiro: ").strip()
    print("Escreve o texto (linha vazia para terminar):")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    with open(ficheiro, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))
    print(f"Guardado em '{ficheiro}'.")


# 3. Acrescentar ao ficheiro
def acrescentar_ficheiro():
    ficheiro = input("Nome do ficheiro: ").strip()
    texto = input("Texto a acrescentar: ")
    with open(ficheiro, "a", encoding="utf-8") as f:
        f.write("\n" + texto)
    print(f"Texto acrescentado a '{ficheiro}'.")


# 4. Contar linhas, palavras e caracteres
def contar_ficheiro():
    ficheiro = input("Nome do ficheiro: ").strip()
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            conteudo = f.read()
        linhas = conteudo.splitlines()
        palavras = conteudo.split()
        print(f"Linhas:     {len(linhas)}")
        print(f"Palavras:   {len(palavras)}")
        print(f"Caracteres: {len(conteudo)}")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")


# 5. Procurar palavra num ficheiro
def procurar_palavra():
    ficheiro = input("Nome do ficheiro: ").strip()
    palavra = input("Palavra a procurar: ").strip().lower()
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        encontradas = [
            (i + 1, linha.strip())
            for i, linha in enumerate(linhas)
            if palavra in linha.lower()
        ]
        if encontradas:
            print(f"'{palavra}' encontrada em {len(encontradas)} linha(s):")
            for num, linha in encontradas:
                print(f"  Linha {num}: {linha}")
        else:
            print(f"'{palavra}' não encontrada.")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")


# 6. Calcular IRS e guardar resultado em ficheiro
def calcular_irs():
    escaloes = {
        8342: 12.5,
        12587: 15.7,
        17838: 21.2,
        23089: 24.1,
        29397: 31.1,
        43090: 34.9,
        46566: 43.1,
        86634: 44.6,
    }

    salario = float(input("Salário anual (€): "))
    taxa = next((t for limite, t in escaloes.items() if salario <= limite), 48.0)
    valor_irs = (taxa / 100) * salario
    liquido = salario - valor_irs

    print(f"Escalão IRS: {taxa}%")
    print(f"Valor IRS:   €{valor_irs:.2f}")
    print(f"Salário líquido: €{liquido:.2f}")

    guardar = input("Guardar resultado em ficheiro? (s/n): ").strip().lower()
    if guardar == "s":
        ficheiro = input("Nome do ficheiro: ").strip()
        with open(ficheiro, "w", encoding="utf-8") as f:
            f.write(f"Salário bruto:   €{salario:.2f}\n")
            f.write(f"Escalão IRS:     {taxa}%\n")
            f.write(f"Valor IRS:       €{valor_irs:.2f}\n")
            f.write(f"Salário líquido: €{liquido:.2f}\n")
        print(f"Resultado guardado em '{ficheiro}'.")


# 7. Agenda de contactos em ficheiro
def agenda_ficheiro():
    FICHEIRO_AGENDA = "agenda.txt"

    def carregar():
        contactos = {}
        try:
            with open(FICHEIRO_AGENDA, "r", encoding="utf-8") as f:
                for linha in f:
                    if ":" in linha:
                        nome, tel = linha.strip().split(":", 1)
                        contactos[nome] = tel
        except FileNotFoundError:
            pass
        return contactos

    def guardar(contactos):
        with open(FICHEIRO_AGENDA, "w", encoding="utf-8") as f:
            for nome, tel in contactos.items():
                f.write(f"{nome}:{tel}\n")

    contactos = carregar()

    while True:
        print("\n1. Adicionar / 2. Listar / 3. Procurar / 4. Remover / 5. Sair")
        acao = input("Ação: ").strip()

        if acao == "1":
            nome = input("Nome: ").strip()
            tel  = input("Telefone: ").strip()
            contactos[nome] = tel
            guardar(contactos)
            print(f"'{nome}' guardado.")

        elif acao == "2":
            if contactos:
                for nome, tel in contactos.items():
                    print(f"  {nome}: {tel}")
            else:
                print("Agenda vazia.")

        elif acao == "3":
            nome = input("Nome: ").strip()
            print(f"{nome}: {contactos.get(nome, 'Não encontrado.')}")

        elif acao == "4":
            nome = input("Nome: ").strip()
            if nome in contactos:
                del contactos[nome]
                guardar(contactos)
                print(f"'{nome}' removido.")
            else:
                print("Não encontrado.")

        elif acao == "5":
            break
        else:
            print("Opção inválida.")


def menu():
    while True:
        print("\nMenu - Bloco 8 (Ficheiros):")
        print("1. Ler ficheiro")
        print("2. Escrever em ficheiro")
        print("3. Acrescentar ao ficheiro")
        print("4. Contar linhas, palavras e caracteres")
        print("5. Procurar palavra num ficheiro")
        print("6. Calcular IRS (com opção de guardar)")
        print("7. Agenda de contactos em ficheiro")
        print("8. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ler_ficheiro()
        elif opcao == "2":
            escrever_ficheiro()
        elif opcao == "3":
            acrescentar_ficheiro()
        elif opcao == "4":
            contar_ficheiro()
        elif opcao == "5":
            procurar_palavra()
        elif opcao == "6":
            calcular_irs()
        elif opcao == "7":
            agenda_ficheiro()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

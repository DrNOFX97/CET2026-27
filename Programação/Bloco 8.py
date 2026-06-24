# 1. Soma de argumentos variáveis
def somar(*args):
    return sum(args)

# 2. Criar e ler ficheiro mensagem.txt
def criar_ficheiro():
    with open("mensagem.txt", "w", encoding="utf-8") as f:
        f.write("Olá mundo!\nBem-vindo ao CET!\nEu gosto de Python")
    print("Ficheiro 'mensagem.txt' criado com sucesso.")

# 2.a Ler o ficheiro e dar print do texto em maiúscula
# 2.b Ler o ficheiro e dar print do texto em minúscula
def ler_ficheiro(ficheiro):
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for linha in linhas:
                print(linha, end="")
            print(f"\nNúmero de linhas: {len(linhas)}")
            conteudo = "".join(linhas)
            print()
            print(conteudo.upper())
            print()
            print(conteudo.lower())
            return conteudo
    except FileNotFoundError:
        print("Não encontro o ficheiro")
    except Exception as e:
        print(f"Erro: {e}")

# 3. Escrever e exportar
def escrever_e_exportar():
    frase = input("Escreve as tuas notas: ")
    with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print("Frase guardada em 'notas.txt'.")

    with open("notas.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    with open("maiusculas.txt", "w", encoding="utf-8") as f:
        f.write(conteudo.upper())
    with open("minusculas.txt", "w", encoding="utf-8") as f:
        f.write(conteudo.lower())
    with open("revertido.txt", "w", encoding="utf-8") as f:
        f.write(reverter_palavras(conteudo))
    print("Ficheiros atualizados.")

def reverter_palavras(conteudo):
    linhas = conteudo.splitlines()
    resultado = []
    for linha in linhas:
        palavras = linha.split()
        palavras_revertidas = [palavra[::-1] for palavra in palavras]
        resultado.append(" ".join(palavras_revertidas))
    return "\n".join(resultado)

def menu():

    while True:
        print("\nMenu - Ficheiros:")
        print("1. Soma de argumentos variáveis")
        print("2. Criar ficheiro mensagem.txt")
        print("3. Ler ficheiro")
        print("4. Escrever e exportar")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            numeros = input("Introduz números separados por espaço: ").split()
            numeros = list(map(int, numeros))
            print(f"Soma: {somar(*numeros)}")
        elif opcao == "2":
            criar_ficheiro()
        elif opcao == "3":
            ler_ficheiro("mensagem.txt")
        elif opcao == "4":
            escrever_e_exportar()
        elif opcao == "5":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

def somar(*args):
    return sum(args)


def reverter_palavras(conteudo):
    linhas = conteudo.splitlines()
    resultado = []
    for linha in linhas:
        palavras = linha.split()
        palavras_revertidas = [palavra[::-1] for palavra in palavras]
        resultado.append(" ".join(palavras_revertidas))
    return "\n".join(resultado)


def ler_ficheiro(ficheiro):
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for linha in linhas:
                print(linha, end="")
            print(f"\nNúmero de linhas: {len(linhas)}")
            conteudo = "".join(linhas)
            print(conteudo.upper())
            print(conteudo.lower())
            return conteudo
    except FileNotFoundError:
        print("Não encontro o ficheiro")
    except Exception as e:
        print(f"Erro: {e}")


def criar_ficheiro():
    with open("mensagem.txt", "w", encoding="utf-8") as f:
        f.write("Olá mundo!\nBem-vindo ao CET!\nEu gosto de Python")
    print("Ficheiro 'mensagem.txt' criado com sucesso.")


def escrever_num_ficheiro():
    frase = input("Escreve as tuas notas: ")
    with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print("Frase guardada em 'notas.txt'.")


def escrever_noutro_ficheiro(conteudo, modo):
    destino = input("Nome do ficheiro destino: ").strip()
    with open(destino, "w", encoding="utf-8") as f:
        if modo == "upper":
            f.write(conteudo.upper())
        elif modo == "lower":
            f.write(conteudo.lower())
        elif modo == "reverter":
            f.write(reverter_palavras(conteudo))
    print(f"Ficheiro '{destino}' criado com sucesso.")


def menu():
    conteudo = ler_ficheiro("mensagem.txt")

    while True:
        print("\nMenu - Ficheiros:")
        print("1. Soma de argumentos variáveis")
        print("2. Ler ficheiro")
        print("3. Criar ficheiro mensagem.txt")
        print("4. Reverter palavras")
        print("5. Escrever nota em notas.txt")
        print("6. Copiar para outro ficheiro em maiúsculas")
        print("7. Copiar para outro ficheiro em minúsculas")
        print("8. Copiar para outro ficheiro com palavras revertidas")
        print("9. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            numeros = input("Introduz números separados por espaço: ").split()
            numeros = list(map(int, numeros))
            print(f"Soma: {somar(*numeros)}")
        elif opcao == "2":
            ler_ficheiro("mensagem.txt")
        elif opcao == "3":
            criar_ficheiro()
            conteudo = ler_ficheiro("mensagem.txt")  # atualiza após criar
        elif opcao == "4":
            if conteudo:
                print(reverter_palavras(conteudo))
        elif opcao == "5":
            escrever_num_ficheiro()
        elif opcao == "6":
            if conteudo:
                escrever_noutro_ficheiro(conteudo, "upper")
        elif opcao == "7":
            if conteudo:
                escrever_noutro_ficheiro(conteudo, "lower")
        elif opcao == "8":
            if conteudo:
                escrever_noutro_ficheiro(conteudo, "reverter")
        elif opcao == "9":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

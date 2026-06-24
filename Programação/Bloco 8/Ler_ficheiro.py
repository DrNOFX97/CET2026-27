def ler_ficheiro(ficheiro):
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Não encontro o ficheiro")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    ficheiro = r"teste.txt"
    conteudo = ler_ficheiro(ficheiro)
    if conteudo:
        print(conteudo)
        print(conteudo.upper())
        print(conteudo.lower())
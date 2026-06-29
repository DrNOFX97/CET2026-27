import re
import csv
from datetime import datetime, timedelta


# Ex. 1 — Soma de argumentos variáveis
def somar(*args):
    return sum(args)


# Ex. 2 — Criar e ler ficheiro
def criar_ler_ficheiro():
    with open("mensagem.txt", "w", encoding="utf-8") as f:
        f.write("Olá mundo!\nBem-vindo ao CET!\nEu gosto de Python\n")
    print("'mensagem.txt' criado.\n")

    try:
        with open("mensagem.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        conteudo = "".join(linhas)

        print("- Normal -")
        for linha in linhas:
            print(linha, end="")
        print(f"\nNúmero de linhas: {len(linhas)}")

        print("- Maiúsculas -")
        print(conteudo.upper())

        print("- Minúsculas -")
        print(conteudo.lower())

    except FileNotFoundError:
        print("Ficheiro não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Ex. 3 — Escrever num ficheiro
def escrever_nota():
    nota = input("Escreve uma nota: ").strip()
    with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(nota + "\n")
    print("Nota guardada em 'notas.txt'.")


# Ex. 4 — Transformar ficheiro
def reverter_palavras(conteudo):
    linhas = conteudo.splitlines()
    return "\n".join(
        " ".join(p[::-1] for p in linha.split())
        for linha in linhas
    )

def transformar_ficheiro():
    entrada = input("Ficheiro de entrada: ").strip()
    saida   = input("Ficheiro de saída: ").strip()

    try:
        with open(entrada, "r", encoding="utf-8") as f:
            conteudo = f.read()

        resultado  = "- Maiúsculas -\n"
        resultado += conteudo.upper() + "\n"
        resultado += "- Minúsculas -\n"
        resultado += conteudo.lower() + "\n"
        resultado += "- Palavras Revertidas -\n"
        resultado += reverter_palavras(conteudo) + "\n"

        with open(saida, "w", encoding="utf-8") as f:
            f.write(resultado)

        print(f"'{saida}' criado.\n")
        print(resultado)

    except FileNotFoundError:
        print(f"'{entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Ex. 5 — Tabela de alunos
def guardar_turma():
    alunos = []

    while True:
        nome = input("Nome (ou 'sair'): ")
        if nome.lower() == "sair":
            break
        nota = input("Nota: ")
        alunos.append((nome, nota))

    with open("turma.txt", "w", encoding="utf-8") as f:
        f.write("Nome           | Nota\n")
        f.write("-" * 30 + "\n")
        for nome, nota in alunos:
            f.write(f"{nome:<15}| {nota}\n")

    print("Guardado em 'turma.txt'.")


# Ex. 6 — Converter data em formato ISO e por extenso
import locale
from datetime import datetime, date

locale.setlocale(locale.LC_TIME, "Portuguese")

def converter_data():
    data = input("Introduz a data (DD MM YYYY): ").strip()
    dt = date.strptime(data, "%d %m %Y")
    hoje = date.today()
    diferenca = (dt - hoje).days

    print(dt.strftime("Formato ISO 8601: %Y-%m-%d"))
    print(dt.strftime("Data: %A, %d de %B de %Y"))
# Extra
    if diferenca == 0:
        print("→ É hoje!")
    elif diferenca < 0:
        print(f"→ Foi há {abs(diferenca)} dias.")
    else:
        print(f"→ Vai ser daqui a {diferenca} dias.")

# Ex. 7 — Subtrair uma semana
def subtrair_semana():
    data = input("Introduz a data (DD/MM/YYYY): ").strip()
    dt = datetime.strptime(data, "%d/%m/%Y")
    resultado = dt - timedelta(weeks=1)
    print(resultado.strftime("%d/%m/%Y"))


# Ex. 8 — Diferença em dias
def diferenca_datas():
    data1 = input("Primeira data (DD/MM/YYYY): ").strip()
    data2 = input("Segunda data (DD/MM/YYYY): ").strip()
    dt1 = datetime.strptime(data1, "%d/%m/%Y")
    dt2 = datetime.strptime(data2, "%d/%m/%Y")
    diferenca = abs((dt1 - dt2).days)
    print(f"Diferença: {diferenca} dias")


# Ex. 9 — Validar email
def validar_email():
    email = input("Introduz o email: ").strip()
    padrao = r"[^@]+@[^@]+\.[a-zA-Z]{2,3}"
    if re.match(padrao, email):
        print("Email válido")
    else:
        print("Email inválido")


# Ex. 10 — CSV vendas
def criar_csv():
    vendas = [
        ("2026-01-05", "Pao",      "Alimentacao", 10, 0.50),
        ("2026-01-08", "Leite",    "Alimentacao",  5, 0.80),
        ("2026-01-10", "Caneta",   "Papelaria",   20, 0.30),
        ("2026-01-12", "Caderno",  "Papelaria",    8, 2.50),
        ("2026-01-15", "Cafe",     "Alimentacao", 15, 0.90),
        ("2026-01-18", "Borracha", "Papelaria",   12, 0.20),
        ("2026-01-20", "Sumo",     "Alimentacao",  6, 1.20),
        ("2026-01-22", "Marcador", "Papelaria",   10, 1.50),
        ("2026-01-25", "Agua",     "Alimentacao", 30, 0.50),
        ("2026-01-28", "Pasta",    "Papelaria",    4, 5.00),
    ]
    with open("vendas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["data", "produto", "categoria", "quantidade", "preco_unit_s_iva"])
        writer.writerows(vendas)
    print("'vendas.csv' criado.")


def adicionar_iva():
    IVA = 1.23
    with open("vendas.csv", "r", encoding="utf-8") as f:
        linhas = list(csv.reader(f))
    linhas[0].append("preco_unit_c_iva")
    for linha in linhas[1:]:
        preco_com_iva = round(float(linha[4]) * IVA, 2)
        linha.append(str(preco_com_iva))
    with open("vendas.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(linhas)
    print("Preço com IVA adicionado em vendas.csv.")


# Menu
def menu():
    while True:
        print("\nBloco 8")
        print(" 1. Soma de argumentos variáveis")
        print(" 2. Criar e ler ficheiro mensagem.txt")
        print(" 3. Escrever nota em notas.txt")
        print(" 4. Transformar ficheiro")
        print(" 5. Tabela de alunos - turma.txt")
        print(" 6. Converter data DD MM YYYY - YYYY/MM/DD")
        print(" 7. Subtrair uma semana a uma data")
        print(" 8. Diferença em dias entre duas datas")
        print(" 9. Validar email")
        print("10. Criar vendas.csv")
        print("11. Adicionar coluna IVA ao vendas.csv")
        print(" 0. Sair")

        opcao = input("\nOpção: ")

        if opcao == "1":
            try:
                nums = list(map(int, input("Números: ").split()))
                print(f"Soma: {somar(*nums)}")
            except ValueError:
                print("Introduz apenas números.")
        elif opcao == "2":
            criar_ler_ficheiro()
        elif opcao == "3":
            escrever_nota()
        elif opcao == "4":
            transformar_ficheiro()
        elif opcao == "5":
            guardar_turma()
        elif opcao == "6":
            converter_data()
        elif opcao == "7":
            subtrair_semana()
        elif opcao == "8":
            diferenca_datas()
        elif opcao == "9":
            validar_email()
        elif opcao == "10":
            criar_csv()
        elif opcao == "11":
            adicionar_iva()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

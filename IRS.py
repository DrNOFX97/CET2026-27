def calcular_irs(salario):
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
    
    for limite, taxa in escaloes.items():
        if salario <= limite:
            return taxa
    return 48.0

salario = float(input("Qual é o teu salário anual? "))
taxa = calcular_irs(salario)
valor_irs = (taxa / 100) * salario

print(f"O teu escalão de IRS é: {taxa}%")
print(f"Vais pagar em IRS: €{valor_irs:.2f}")
print(f"O teu salário líquido é: €{salario - valor_irs:.2f}")
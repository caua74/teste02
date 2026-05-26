#analise de juros
# Programa de análise de juros

valor = float(input("Digite o valor inicial (R$): "))
juros = float(input("Digite a taxa de juros (%): "))
periodos = int(input("Digite o número de períodos (meses): "))

# Verificação das taxas
if juros == 15:
    resultado_simples = valor * (1 + 0.15)
    resultado_composto = valor * ((1 + 0.15) ** periodos)
    print(f"\nTaxa de 15% aplicada.")
    print(f"➡ Valor final com juros simples: R$ {resultado_simples:.2f}")
    print(f"➡ Valor final com juros compostos em {periodos} meses: R$ {resultado_composto:.2f}")

elif juros == 20:
    resultado_simples = valor * (1 + 0.20)
    resultado_composto = valor * ((1 + 0.20) ** periodos)
    print(f"\nTaxa de 20% aplicada.")
    print(f"➡ Valor final com juros simples: R$ {resultado_simples:.2f}")
    print(f"➡ Valor final com juros compostos em {periodos} meses: R$ {resultado_composto:.2f}")

elif juros == 60:
    resultado_simples = valor * (1 + 0.60)
    resultado_composto = valor * ((1 + 0.60) ** periodos)
    print(f"\nTaxa de 60% aplicada.")
    print(f"➡ Valor final com juros simples: R$ {resultado_simples:.2f}")
    print(f"➡ Valor final com juros compostos em {periodos} meses: R$ {resultado_composto:.2f}")

else:
    print("\nTaxa de juros não reconhecida. Use apenas 15, 20 ou 60%.")

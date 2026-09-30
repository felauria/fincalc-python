# ============================================
# CÁLCULO DE LUCRO E MARGENS
# Trabalho de Faculdade - Python
# ============================================

print("======================================")
print("     CALCULADORA DE LUCRO EMPRESARIAL")
print("======================================")

receita = float(input("Digite a receita total da empresa: R$ "))
custos = float(input("Digite o total de custos: R$ "))
despesas_operacionais = float(input("Digite as despesas operacionais: R$ "))
impostos = float(input("Digite o valor dos impostos: R$ "))

lucro_bruto = receita - custos

lucro_operacional = lucro_bruto - despesas_operacionais

lucro_liquido = lucro_operacional - impostos

margem_operacional = (lucro_operacional / receita) * 100

margem_liquida = (lucro_liquido / receita) * 100

print("\n======================================")
print("             RESULTADOS")
print("======================================")

print(f"Receita total: R$ {receita:,.2f}")
print(f"Lucro bruto: R$ {lucro_bruto:,.2f}")
print(f"Lucro operacional: R$ {lucro_operacional:,.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:,.2f}")
print(f"Margem operacional: {margem_operacional:.2f}%")
print(f"Margem de lucro líquido: {margem_liquida:.2f}%")

print("======================================")

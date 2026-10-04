# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_irrf(salario_base):
    """Calcula o Imposto de Renda Retido na Fonte (IRRF)."""
    if not isinstance(salario_base, (int, float)) or isinstance(
        salario_base, bool
    ):
        raise TypeError("O salário base deve ser um número numérico.")

    if salario_base < 0:
        raise ValueError("O salário base não pode ser negativo.")

    if salario_base <= 2259.20:
        imposto = 0.0
    elif salario_base <= 2826.65:
        imposto = (salario_base * 0.075) - 169.44
    elif salario_base <= 3751.05:
        imposto = (salario_base * 0.15) - 381.44
    elif salario_base <= 4664.68:
        imposto = (salario_base * 0.225) - 662.77
    else:
        imposto = (salario_base * 0.275) - 896.00

    return round(imposto, 2)


def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(
    patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}\n")

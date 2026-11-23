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
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if anos < 0:
        raise ValueError("O prazo não pode ser negativo.")
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_margem_liquida(
    receita_total: float,
    custos_totais: float,
) -> float:
    """Calcula a margem líquida com base na receita e nos custos."""

    if receita_total <= 0:
        raise ValueError("A receita total deve ser maior que zero.")

    if custos_totais < 0:
        raise ValueError("Os custos totais não podem ser negativos.")

    margem = ((receita_total - custos_totais) / receita_total) * 100

    return margem


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""

    if aporte_mensal < 0:
        raise ValueError("O aporte mensal não pode ser negativo.")

    if meses < 0:
        raise ValueError("O número de meses não pode ser negativo.")

    if taxa_mensal == 0:
        return aporte_mensal * meses

    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)

    return vf


def calcular_depreciacao_linear(
    valor_inicial: float,
    valor_residual: float,
    vida_util_anos: int,
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""

    if vida_util_anos <= 0:
        raise ValueError("A vida útil deve ser maior que zero.")

    if valor_residual > valor_inicial:
        raise ValueError("O valor residual não pode ser maior que o inicial.")

    return (valor_inicial - valor_residual) / vida_util_anos


def calcular_parcela_price(
    valor_emprestimo: float,
    taxa_mensal: float,
    meses: int,
) -> float:
    """Calcula a prestação mensal de um financiamento pela Tabela Price."""

    if valor_emprestimo < 0:
        raise ValueError("O valor do empréstimo não pode ser negativo.")

    if meses <= 0:
        raise ValueError("A quantidade de meses deve ser maior que zero.")

    if taxa_mensal == 0:
        return valor_emprestimo / meses

    taxa = taxa_mensal / 100
    fator = (1 + taxa) ** meses

    parcela = valor_emprestimo * (taxa * fator) / (fator - 1)

    return parcela


def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    if taxa_anual < -100:
        raise ValueError("A taxa anual não pode ser inferior a -100%.")

    return (((1 + (taxa_anual / 100)) ** (1 / 12)) - 1) * 100


def calcular_rendimento_real(
    ganho_nominal: float,
    inflacao: float
) -> float:
    """Calcula a taxa de retorno real descontando a inflação."""

    if ganho_nominal < -100:
        raise ValueError(
            "O ganho nominal não pode ser inferior a -100%."
        )

    if inflacao <= -100:
        raise ValueError(
            "A inflação deve ser superior a -100%."
        )

    retorno_real = (
        (1 + ganho_nominal / 100)
        / (1 + inflacao / 100)
    ) - 1

    return retorno_real * 100


def calcular_rendimento_real_ajustado(
    capital_inicial: float,
    taxa_nominal: float,
    taxa_inflacao: float,
    anos: int,
) -> float:
    """
    Calcula o rendimento acumulado em reais,
    descontando os efeitos da inflação.
    """

    if capital_inicial < 0:
        raise ValueError("O capital inicial não pode ser negativo.")

    if anos < 0:
        raise ValueError("O prazo não pode ser negativo.")

    if taxa_nominal < -100:
        raise ValueError(
            "O ganho nominal não pode ser inferior a -100%."
        )

    if taxa_inflacao <= -100:
        raise ValueError(
            "A inflação deve ser superior a -100%."
        )

    taxa_real = calcular_rendimento_real(
        taxa_nominal,
        taxa_inflacao
    ) / 100

    valor_final_real = capital_inicial * (
        (1 + taxa_real) ** anos
    )

    rendimento_real = valor_final_real - capital_inicial

    return rendimento_real

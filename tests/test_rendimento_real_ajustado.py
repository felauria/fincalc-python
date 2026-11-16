import pytest

from fincalc import calcular_rendimento_real_ajustado


def test_rendimento_real_ajustado_desconta_inflacao():
    rendimento = calcular_rendimento_real_ajustado(1000.0, 10.0, 4.0, 3)
    assert round(rendimento, 2) == 183.25


def test_rendimento_real_ajustado_com_prazo_zero():
    rendimento = calcular_rendimento_real_ajustado(1000.0, 10.0, 4.0, 0)
    assert rendimento == 0.0


def test_rendimento_real_ajustado_rejeita_capital_negativo():
    with pytest.raises(ValueError):
        calcular_rendimento_real_ajustado(-1000.0, 10.0, 4.0, 3)


def test_rendimento_real_ajustado_rejeita_prazo_negativo():
    with pytest.raises(ValueError):
        calcular_rendimento_real_ajustado(1000.0, 10.0, 4.0, -1)


def test_rendimento_real_ajustado_rejeita_inflacao_de_menos_cem_porcento():
    with pytest.raises(ValueError):
        calcular_rendimento_real_ajustado(1000.0, 10.0, -100.0, 3)

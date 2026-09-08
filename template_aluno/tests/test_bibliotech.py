from src.bibliotech import (
    pode_emprestar,
    calcular_multa,
    classificar_atraso,
)


# RF01 — Permissão para empréstimo

def test_usuario_valido_sem_emprestimos():
    assert pode_emprestar(True, False, 0) is True


def test_usuario_inativo():
    assert pode_emprestar(False, False, 0) is False


def test_usuario_com_pendencia():
    assert pode_emprestar(True, True, 0) is False


def test_usuario_com_tres_emprestimos():
    assert pode_emprestar(True, False, 3) is False


def test_usuario_com_dois_emprestimos():
    assert pode_emprestar(True, False, 2) is True


def test_usuario_com_quatro_emprestimos():
    assert pode_emprestar(True, False, 4) is False


# RF02 — Multa por atraso

def test_multa_sem_atraso():
    assert calcular_multa(0) == 0.0


def test_multa_atraso_negativo():
    assert calcular_multa(-1) == 0.0


def test_multa_um_dia():
    assert calcular_multa(1) == 2.0


def test_multa_tres_dias():
    assert calcular_multa(3) == 6.0


def test_multa_sete_dias():
    assert calcular_multa(7) == 14.0


def test_multa_oito_dias():
    assert calcular_multa(8) == 17.0


def test_multa_dez_dias():
    assert calcular_multa(10) == 23.0


# RF03 — Classificação de atraso

def test_classificacao_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_classificacao_um_dia():
    assert classificar_atraso(1) == "atraso leve"


def test_classificacao_sete_dias():
    assert classificar_atraso(7) == "atraso leve"


def test_classificacao_oito_dias():
    assert classificar_atraso(8) == "atraso moderado"


def test_classificacao_trinta_dias():
    assert classificar_atraso(30) == "atraso moderado"


def test_classificacao_trinta_e_um_dias():
    assert classificar_atraso(31) == "atraso grave"
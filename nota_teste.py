import pytest
from nota import Aluno


def test_media_correta():
    aluno = Aluno()

    aluno.cadastrar_nota(8)
    aluno.cadastrar_nota(6)

    assert aluno.calcular_media() == 7


def test_nota_invalida():
    aluno = Aluno()

    with pytest.raises(ValueError):
        aluno.cadastrar_nota(11)


def test_aprovacao_correta():
    aluno = Aluno()

    aluno.cadastrar_nota(7)
    aluno.cadastrar_nota(8)

    assert aluno.verificar_situacao() == "Aprovado"


def test_recuperacao():
    aluno = Aluno()

    aluno.cadastrar_nota(5)
    aluno.cadastrar_nota(6)

    assert aluno.verificar_situacao() == "Recuperação"


def test_reprovacao():
    aluno = Aluno()

    aluno.cadastrar_nota(3)
    aluno.cadastrar_nota(4)

    assert aluno.verificar_situacao() == "Reprovado"
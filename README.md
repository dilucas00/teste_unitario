# teste_unitario

## Descrição

Projeto simples de validação de notas usando testes unitários em Python. A solução implementa uma classe `Aluno` que cadastra notas, calcula a média e determina a situação final com base nas regras definidas.

## Objetivo

Aplicar testes unitários para desenvolver uma funcionalidade com validação automática, garantindo que as regras de negócio sejam cumpridas.

## Funcionalidades

- Cadastrar notas entre `0` e `10`
- Validar nota inválida e lançar `ValueError`
- Calcular a média aritmética das notas cadastradas
- Verificar a situação do aluno:
  - `média >= 7` → `Aprovado`
  - `5 <= média < 7` → `Recuperação`
  - `média < 5` → `Reprovado`

## Arquivos do projeto

- `nota.py` — implementação da classe `Aluno`
- `nota_teste.py` — testes unitários com `pytest`
- `report.html` — relatório HTML gerado pelo `pytest` com o resultado dos testes

## Requisitos

- Python 3.8+ instalado
- `pytest`
- `pytest-html` para gerar relatório em HTML

## Instalação

1. (Opcional) crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install pytest pytest-html
```

## Como executar

Para rodar os testes unitários:

```bash
pytest nota_teste.py
```

Para gerar um relatório HTML de teste:

```bash
pytest nota_teste.py --html=report.html --self-contained-html
```

Após a execução, abra `report.html` em um navegador para ver o relatório completo.

## Ciclo de desenvolvimento

1. Escrever um teste que define o comportamento esperado.
2. Executar o teste e verificar que ele falha.
3. Implementar a funcionalidade mínima em `nota.py`.
4. Rodar os testes novamente para confirmar que passam.
5. Repetir até implementar todas as regras e casos esperados.

## Casos testados

- média correta com notas válidas
- cadastro de nota inválida (`nota > 10` ou nota negativa)
- situação de aprovação
- situação de recuperação
- situação de reprovação

## Estrutura do projeto

```
nota.py
nota_teste.py
report.html
README.md
```

## Observações

- Todos os testes atuais passam.
- O relatório HTML `report.html` contém a evidência de execução dos testes.
- O projeto segue a estrutura esperada: código da classe em um arquivo e testes unitários em outro.


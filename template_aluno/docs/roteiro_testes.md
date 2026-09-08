# Roteiro de Testes — BiblioTech

## Objetivo

Verificar se as funções do BiblioTech atendem aos requisitos RF01, RF02 e RF03, incluindo cenários válidos, inválidos e valores de fronteira.

## Pré-condições gerais

- Python e pytest instalados;
- sistema disponível;
- requisitos definidos;
- testes executados na pasta `template_aluno`.

## Casos de teste — RF01: Permissão para empréstimo

| ID | Cenário | Dados de teste | Resultado esperado | Prioridade |
|---|---|---|---|---|
| CT-01 | Usuário válido sem empréstimos | `True, False, 0` | `True` | Alta |
| CT-02 | Usuário inativo | `False, False, 0` | `False` | Alta |
| CT-03 | Usuário com pendência | `True, True, 0` | `False` | Alta |
| CT-04 | Usuário no limite de três empréstimos | `True, False, 3` | `False` | Alta |
| CT-05 | Usuário com dois empréstimos | `True, False, 2` | `True` | Alta |
| CT-06 | Usuário acima do limite | `True, False, 4` | `False` | Alta |

## Casos de teste — RF02: Multa por atraso

| ID | Cenário | Dias de atraso | Resultado esperado | Prioridade |
|---|---|---:|---:|---|
| CT-07 | Sem atraso | 0 | R$ 0,00 | Alta |
| CT-08 | Atraso negativo | -1 | R$ 0,00 | Média |
| CT-09 | Primeiro dia de atraso | 1 | R$ 2,00 | Alta |
| CT-10 | Três dias de atraso | 3 | R$ 6,00 | Média |
| CT-11 | Limite de sete dias | 7 | R$ 14,00 | Alta |
| CT-12 | Primeiro dia acima do limite | 8 | R$ 17,00 | Alta |
| CT-13 | Dez dias de atraso | 10 | R$ 23,00 | Média |

## Casos de teste — RF03: Classificação de atraso

| ID | Cenário | Dias de atraso | Resultado esperado | Prioridade |
|---|---|---:|---|---|
| CT-14 | Sem atraso | 0 | `sem atraso` | Alta |
| CT-15 | Primeiro dia de atraso | 1 | `atraso leve` | Alta |
| CT-16 | Limite do atraso leve | 7 | `atraso leve` | Alta |
| CT-17 | Início do atraso moderado | 8 | `atraso moderado` | Alta |
| CT-18 | Limite do atraso moderado | 30 | `atraso moderado` | Alta |
| CT-19 | Início do atraso grave | 31 | `atraso grave` | Alta |

## Procedimento de execução

1. Preparar os dados definidos em cada caso.
2. Executar a função correspondente por meio do pytest.
3. Comparar o resultado obtido com o resultado esperado.
4. Registrar se o caso passou ou falhou.
5. Documentar qualquer comportamento diferente do requisito.

## Pós-condição

Os resultados ficam registrados como evidência para a decisão final de QA.

## Resultado da execução

- Total de testes executados: 20
- Testes aprovados: 19
- Testes reprovados: 1
- Cobertura de linhas e branches: 100%
- Requisito com defeito: RF01
- Caso que encontrou o defeito: CT-04

### Defeito encontrado

O sistema permitiu um novo empréstimo para um usuário ativo, sem pendências e com exatamente três empréstimos ativos.

O resultado esperado era `False`, pois o RF01 determina que o usuário deve possuir menos de três empréstimos ativos. Entretanto, o resultado obtido foi `True`.

### Status

Reprovado. O defeito deve ser corrigido antes da liberação para produção.
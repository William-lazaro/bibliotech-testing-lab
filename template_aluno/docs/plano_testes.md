# Mini Plano de Testes — BiblioTech

## Responsável

William Lázaro

## Escopo

Testar os requisitos RF01, RF02 e RF03 do módulo de empréstimos do BiblioTech.

## Fora do escopo

Interface gráfica, banco de dados, segurança, integração e desempenho.

## Estratégia

- Testes de caixa preta baseados nos requisitos.
- Testes de caixa branca baseados na estrutura do código.
- Testes unitários automatizados com pytest.
- Análise de valores de fronteira e partições de equivalência.

## Ambiente

- Python
- pytest
- pytest-cov
- Visual Studio Code
- GitHub e GitHub Actions

## Critério de entrada

Código-fonte disponível, requisitos definidos e ambiente de testes configurado.

## Critérios de saída

- RF01, RF02 e RF03 testados;
- cenários positivos e negativos executados;
- defeitos encontrados registrados;
- cobertura de linhas e branches igual ou superior a 90%;
- Pull Request criado com as evidências.

## Riscos

- Tempo limitado para executar a atividade;
- cobertura incompleta;
- requisitos interpretados incorretamente;
- defeitos em valores de fronteira.

## Entregáveis

- plano de testes;
- casos e roteiros de teste;
- matriz de rastreabilidade;
- testes automatizados;
- relatório de cobertura;
- Pull Request;
- parecer final de QA.
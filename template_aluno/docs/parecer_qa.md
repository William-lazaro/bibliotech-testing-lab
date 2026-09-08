# Parecer Final de QA — BiblioTech

## Responsável

William Lázaro

## Requisitos avaliados

- RF01 — Permissão para empréstimo
- RF02 — Multa por atraso
- RF03 — Classificação de atraso

## Evidências

- 20 testes automatizados executados;
- 19 testes aprovados;
- 1 teste reprovado;
- cobertura de linhas e branches: 100%;
- cenários positivos, negativos e valores de fronteira testados.

## Defeito identificado

O RF01 determina que somente usuários com menos de três empréstimos ativos podem realizar um novo empréstimo.

Durante o teste com um usuário ativo, sem pendências e com exatamente três empréstimos, o sistema retornou `True`. O resultado esperado era `False`.

O defeito está relacionado à verificação do limite de empréstimos.

## Parecer

- [ ] Recomendamos a aprovação
- [x] Não recomendamos a aprovação

## Justificativa

A versão atual do BiblioTech não deve ser liberada para produção porque permite que um usuário com três empréstimos ativos realize um novo empréstimo, contrariando o RF01.

A equipe recomenda corrigir a condição de limite e executar novamente todos os testes antes da aprovação.
# Macro RP ↔ R$ — LibreOffice Calc

## Objetivo

- Converter automaticamente Riot Points (RP) em Reais (R$) e vice-versa no LibreOffice Calc, com foco em usabilidade
- Segurança dos dados e geração de relatório automático.

## Funcionalidades

- Conversão RP → R$ e R$ → RP
- Preservação dos dados de entrada (não sobrescreve RP)
- Mensagens claras de sucesso ou erro
- Relatório automático da conversão, exibindo total de RP e Reais
- Compatível com células selecionadas na planilha

## Melhorias Implementadas

- Evita sobrescrever os dados originais (RP fica na coluna A, resultado na B)
- Mensagens explicativas ao usuário em caso de erro ou sucesso
- Relatório automático com total de RP, total de Reais, quantidade de células processadas e taxa de conversão
- Conversão reversa (R$ → RP) implementada
- Base de taxas atualizada com valores reais do site oficial
- Código comentado e organizado para facilitar manutenção

## Como usar
[Tutorial](./ComoUsar.txt)

## Arquivo
[Macro](./macroRP.py)

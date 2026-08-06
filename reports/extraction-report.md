# Relatório de extração

## Fonte de origem

O dataset foi gerado a partir do arquivo `BIL26-0526.pdf`, que não está incluído neste repositório.

- SHA-256: `1fc341da29f5d723817c0b21670ccacdb8cd8f9c635b5d8a1d0149769525682a`
- Página: 1 de 1
- Formato: A1 paisagem
- Atualização indicada no mapa: 26/05/2026
- Revisão indicada no mapa: 12

## Resultado

- Estandes e módulos: **295**
- Expositores e ocupantes: **216**
- Categorias: **6**
- Pontos de interesse: **102**
- Estandes validados: **244**
- Estandes que precisam de revisão: **51**

## Método

1. Extração dos textos e vetores posicionados no PDF;
2. Identificação dos códigos de estandes;
3. Associação dos códigos aos menores contornos compatíveis;
4. Reconstrução dos nomes presentes em cada área;
5. Classificação pelas cores da legenda;
6. Registro separado dos itens que não puderam ser confirmados com segurança.

Os códigos `IFxx` foram tratados como infraestrutura e os módulos `TI01` a `TI25` foram preservados sem inventar ocupantes ausentes.

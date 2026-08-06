# Dicionário de dados

## Estandes

Arquivo: `data/stands.json`

- `id`: identificador estável usado nos JSONs e no SVG;
- `code`: código exibido no mapa;
- `normalizedCode`: código normalizado para pesquisa;
- `exhibitorIds`: expositores associados;
- `categoryIds`: categorias associadas;
- `streetId`: rua ou setor relacionado;
- `svgElementId`: elemento correspondente no SVG;
- `geometry`: polígono, caixa delimitadora, centro e ponto de foco;
- `validation`: status, confiança, evidências e observações.

## Expositores

Arquivo: `data/exhibitors.json`

- `id`: identificador estável;
- `name`: nome preservado do mapa;
- `normalizedName`: nome normalizado para pesquisa;
- `slug`: identificador textual;
- `standIds`: estandes associados;
- `categoryIds`: categorias associadas;
- `validation`: status, confiança e observações.

## Pontos de interesse

Arquivo: `data/points-of-interest.json`

- `id`: identificador estável;
- `name`: nome preservado do mapa;
- `type`: tipo normalizado;
- `standId`: estande relacionado, quando aplicável;
- `svgElementId`: elemento correspondente no SVG;
- `geometry`: ponto ou polígono;
- `validation`: status, confiança, evidências e observações.

## Status de validação

- `validated`: informação confirmada;
- `needs-review`: informação utilizável, mas ainda precisa de revisão;
- `unresolved`: informação não determinada com segurança;
- `not-applicable`: validação não aplicável.

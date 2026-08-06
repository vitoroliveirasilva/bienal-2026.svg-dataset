# Relatório de validação

## Resumo

- Verificações aprovadas: **20**
- Verificações reprovadas: **0**
- Estandes validados: **295**
- Estandes aguardando revisão: **0**
- Pontos de interesse validados: **102**
- Pontos de interesse aguardando revisão: **0**
- Lacunas documentadas da fonte: **46**

## Revisão manual

Os 51 estandes e os 51 pontos de interesse anteriormente marcados para revisão foram comparados com o PDF de origem.

- A categoria do estande `13` da Travessa Literária foi confirmada como `exhibitor`;
- medidas como `2m 2m` e `5m 5m` foram removidas de 12 nomes de expositores;
- um registro formado apenas por medidas foi removido;
- os pontos de interesse foram confirmados como âncoras dos rótulos visíveis;
- as ausências de ocupante que não podem ser resolvidas pela fonte foram registradas como `unresolved`.

## Verificações realizadas

- XML e `viewBox` do SVG;
- IDs únicos no SVG e nos arquivos JSON;
- correspondência entre estandes, pontos de interesse e elementos do SVG;
- integridade das geometrias e caixas delimitadoras;
- referências entre estandes, expositores e categorias;
- validação dos documentos contra os JSON Schemas;
- ausência de recursos externos obrigatórios;
- renderização do SVG pelo Inkscape;
- validade do arquivo `map-full-vector.svgz`;
- comparação visual entre o SVG renderizado e o PDF;
- revisão semântica manual contra a fonte.

## Comparação visual

A comparação original foi realizada em 5960 × 4210 px.

- Erro absoluto médio: **0,0000**
- PSNR: **99,0000 dB**

A correção atual altera apenas metadados semânticos do SVG. Uma nova comparação entre as versões anterior e revisada, renderizadas em 2384 × 1684 px, apresentou erro absoluto médio de **0,0000**, confirmando que a camada visual permaneceu inalterada.

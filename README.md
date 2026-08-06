# Bienal do Livro 2026 — Map Data

Base técnica reutilizável do mapa da Bienal do Livro 2026, gerada a partir do PDF `BIL26-0526.pdf`.

O repositório contém o mapa em SVG, catálogos JSON, schemas de validação, previews e relatórios técnicos.

## Estrutura

- `map/`: SVG otimizado, versão vetorial integral e imagens de preview;
- `data/`: estandes, expositores, categorias, pontos de interesse e relacionamentos;
- `schemas/`: JSON Schemas Draft 2020-12;
- `reports/`: resumo da extração, validação, campos e limitações;
- `source/`: metadados da fonte e manifesto de integridade.

## Arquivos principais

- `map/map-optimized.svg`: mapa indicado para uso em aplicações web;
- `data/stands.json`: estandes e suas geometrias;
- `data/exhibitors.json`: expositores e estandes associados;
- `data/points-of-interest.json`: acessos, serviços e demais pontos de interesse;
- `data/catalog.json`: visão consolidada dos dados;
- `data/unresolved-items.json`: itens que ainda precisam de revisão.

## Coordenadas

O SVG utiliza o `viewBox` `0 0 2384 1684`.

- Origem: canto superior esquerdo;
- Eixo X: cresce para a direita;
- Eixo Y: cresce para baixo;
- Unidade: unidade interna do SVG.

## Exemplo de uso

```js
const data = await fetch("./data/stands.json").then((response) =>
  response.json(),
);

const stand = data.stands.find((item) => item.normalizedCode === "A30");

const svgDocument = document.querySelector("object#event-map").contentDocument;
const element = svgDocument.getElementById(stand.svgElementId);

element?.classList.add("is-selected");
```

## Validação

Os JSONs foram validados contra seus schemas. Também foram verificados o SVG, os IDs, as referências cruzadas, as geometrias e a renderização visual.

Consulte `reports/validation-report.md` e `data/validation-results.json`.

## Licença e uso

Este repositório não é distribuído sob uma licença de código aberto.

Os direitos relacionados ao mapa original, à identidade do evento, às marcas, aos nomes dos expositores e aos materiais visuais pertencem aos seus respectivos titulares.

Consulte [NOTICE.md](NOTICE.md).

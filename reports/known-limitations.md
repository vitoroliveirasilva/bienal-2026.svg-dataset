# Limitações conhecidas

- O SVG principal utiliza um fundo incorporado de alta resolução com camadas semânticas vetoriais (a conversão vetorial integral está em `map/map-full-vector.svgz`);
- Os pontos de interesse usam como âncora o centro do rótulo visível no mapa e não devem ser tratados como coordenadas de navegação passo a passo;
- 46 estandes não exibem um ocupante identificável no mapa de origem;
- Os módulos `TI01` a `TI25` não exibem ocupantes individuais no mapa;
- Os nomes foram preservados como aparecem na fonte, exceto pela remoção de medidas de montagem incorporadas incorretamente durante a extração;
- Os marcadores `IFxx` foram classificados como infraestrutura, não como estandes.

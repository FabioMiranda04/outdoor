# `qr/` — os QR codes que apontam para esta página

Apontam para `https://outdoor-sigma.vercel.app`. **Conferidos**: os três
decodificam de volta na URL exata, testados em 300, 600 e 1200px. E a URL
em maiúsculas responde 200.

| Arquivo | Para quê |
|---|---|
| `qr-outdoor.svg` | **o mestre para impressão.** Vetor: escala para qualquer tamanho sem perder nitidez |
| `qr-outdoor.png` | 2960px, para conferir na tela e mandar por WhatsApp |
| `qr-outdoor-marca.*` | mesmo código nas cores da marca — Walnut sobre Cream Quartz, contraste 12,4:1 |
| `qr-outdoor-longe.*` | 25×25 em vez de 29×29. Módulos maiores, lê de mais longe, menos tolerante a sujeira |

## Duas decisões que valem saber

**A URL está em maiúsculas de propósito.** O QR tem um modo alfanumérico
que só aceita maiúsculas e gasta menos bits. Com ele o código coube em
29×29 módulos com 25% de correção de erro; em minúsculas, os mesmos 29×29
só davam 15%. Robustez de graça. Domínio não diferencia maiúscula de
minúscula, então abre igual — **mas caminho diferencia**. Se um dia a URL
virar `/convite`, esse truque sai.

**A borda branca em volta não é margem de diagramação.** São os 4 módulos
de "zona de silêncio" que a especificação exige. Leitor nenhum acha o
código sem ela. Não recorte, não encoste texto.

## Antes de mandar para a gráfica

- [ ] **Trocar pelo domínio próprio.** `outdoor-sigma.vercel.app` foi a
      Vercel que sorteou. Num outdoor parece link suspeito e não tem nada
      da marca. Registrado o domínio, mude a `URL` no `gerar.py` e rode
      de novo;
- [ ] **Testar impresso, não na tela.** Imprima em papel no tamanho final
      e escaneie de longe, com celular de câmera ruim e pouca luz;
- [ ] **Tamanho:** a regra prática é lado do QR ≥ distância de leitura
      dividida por 10. Quem lê a 3m precisa de 30cm de QR.

## Regerar

```bash
pip install segno && python3 qr/gerar.py
```

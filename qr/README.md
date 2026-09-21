# `qr/` — os QR codes que apontam para esta página

Apontam para `https://outdoor-sigma.vercel.app`. **Conferidos**: os três
decodificam de volta na URL exata, testados em 300, 600 e 1200px. E a URL
em maiúsculas responde 200.

| Arquivo | Para quê |
|---|---|
| `qr-outdoor.pdf` | **é este que vai para a gráfica.** Vetor, formato que impressora entende |
| `qr-outdoor.svg` / `.eps` | o mesmo vetor, para quem preferir abrir no Illustrator ou no Corel |
| `qr-outdoor.png` | 8880px, para conferir na tela e mandar por WhatsApp |
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
- [ ] **Tamanho, para outdoor de avenida.** A regra é: lado do QR ≥
      distância de leitura ÷ 10. Com os 37 módulos de borda a borda deste
      código:

      | QR de | cada módulo | lê a até |
      |---|---|---|
      | 80 cm | 22 mm | ~8 m |
      | 120 cm | 32 mm | ~12 m |
      | 200 cm | 54 mm | ~20 m |

      Num outdoor de 9×3m, 120cm cabe folgado na altura e alcança os ~12m
      de quem está parado no semáforo ou na calçada. **Quem passa de
      carro a 60 km/h não escaneia nada** — não existe tamanho que
      resolva isso, porque falta tempo, não pixel. Por isso o telefone e
      o @ precisam estar legíveis no painel também, para quem não vai
      parar.

## Regerar

```bash
pip install segno && python3 qr/gerar.py
```

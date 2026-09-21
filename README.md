# outdoor — apresentação da Tríade Conecta

Página estática, cópia fiel do site montado no ChatGPT
(`triade-conecta-apresentacao.liviaduartelopes.chatgpt.site`), trazida
para um repositório e um domínio nossos.

Sem build, sem dependência, sem framework. A Vercel publica o repositório
como está: `index.html` na raiz, `styles.css` ao lado, imagens em
`assets/`. Abrir o `index.html` no navegador mostra a página inteira.

## O que mudou em relação ao original

**Uma única coisa:** saiu o `<script>` de challenge da Cloudflare que
ficava antes do `</body>`. Ele não fazia parte da página — era injetado
pelo serviço que a hospedava. Mantê-lo faria um script de terceiro rodar
no nosso domínio sem motivo.

HTML, CSS, textos e imagens são os originais, byte por byte.

## O botão do WhatsApp

Abre um pop-up com as três idealizadoras em ordem alfabética. Escolhida
uma, o WhatsApp abre já com a mensagem escrita:

> Olá, tudo bem? Vi o anúncio da Tríade Conecta e gostaria de saber mais
> sobre a comunidade e os próximos encontros.

É o `<dialog>` nativo do HTML — Esc fecha, o fundo escurece e a página
atrás trava sem nenhuma biblioteca. O script inteiro tem cinco linhas.

## Pendências

- [ ] **Confirmar os números das sócias.** Lia e Lívia estão com 8
      dígitos (`8131-7399`, `8287-0136`) e Cris com 9 (`98165-1103`).
      Celular no Brasil tem 9 desde 2016, então ou falta o 9 nos dois
      primeiros, ou são cadastros antigos que o WhatsApp manteve. Os
      links estão exatamente como você passou — **toque nos três antes
      de imprimir**. Corrigir é mudar o número no `index.html`;
- [ ] **Imagens pesam 3,7 MB.** As fotos vêm em 2240×3360 — resolução de
      câmera, não de web — e a logo é um PNG de 921 KB. Num celular em
      4G isso demora. Redimensionar para 1400px no lado maior derruba o
      total para ~940 KB sem diferença visível;
- [ ] **Não segue o Manual de Marca.** O dourado aqui é `#b79a63`; o
      oficial da Tríade é `#C9A66B`. As fontes são as de sistema (Arial e
      Georgia), não Cormorant SC / Playfair Display / Inter.

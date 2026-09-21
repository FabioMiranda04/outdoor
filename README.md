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

## O botão "Fale conosco!"

Link direto para o WhatsApp comercial da Tríade — **+55 62 9913-7662**,
a conta Business com o nome "Tríade Conecta". Já abre com a mensagem
escrita:

> Olá, tudo bem? Vi o anúncio da Tríade Conecta e gostaria de saber mais
> sobre a comunidade e os próximos encontros.

A logo do WhatsApp é SVG inline: sem arquivo de imagem, sem biblioteca,
e a cor sai do CSS, então acompanha o estado do botão. Como o texto não
diz mais "WhatsApp", é o ícone que carrega essa informação.

**Bug corrigido de passagem:** no original, passar o mouse escurecia o
fundo do botão mas deixava o texto verde-escuro — 1,2:1 de contraste, ou
seja, o texto sumia. Agora clareia junto: 12,2:1.

Chegou a existir aqui um pop-up para escolher entre as três sócias.
Saiu: com um número comercial, um toque a menos até a conversa, e a
página voltou a ter **zero JavaScript**.

## Pendências

- [ ] **Testar o link do WhatsApp.** O número aparece com 8 dígitos
      (`9913-7662`) e celular no Brasil tem 9 desde 2016 — o WhatsApp
      mantém o formato antigo para contas antigas, então provavelmente
      está certo assim. Mas é um toque para confirmar, e um botão morto
      num outdoor impresso custa caro. Corrigir é trocar o número no
      `index.html`;
- [ ] **Imagens pesam 3,7 MB.** As fotos vêm em 2240×3360 — resolução de
      câmera, não de web — e a logo é um PNG de 921 KB. Num celular em
      4G isso demora. Redimensionar para 1400px no lado maior derruba o
      total para ~940 KB sem diferença visível;
- [ ] **Não segue o Manual de Marca.** O dourado aqui é `#b79a63`; o
      oficial da Tríade é `#C9A66B`. As fontes são as de sistema (Arial e
      Georgia), não Cormorant SC / Playfair Display / Inter.

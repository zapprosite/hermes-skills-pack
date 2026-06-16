# Camofox em background e validação da 1ª imagem

- O navegador não precisa estar visível para o workflow funcionar; o que precisa estar vivo é o backend/sessão persistente do Camofox e o `CAMOFOX_URL` correto apontando para essa sessão.
- Para validação mínima do fluxo, peça explicitamente para gerar apenas a primeira imagem do carrossel e parar em seguida.
- Durante a geração, a UI do ChatGPT pode continuar exibindo estado de "Thinking" mesmo com a imagem já renderizada. Confirme o resultado pela presença do card/imagem gerada, não só pelo estado do botão.
- Se a sessão já estiver autenticada, evite reabrir ou reinicializar o navegador só para teste; use a sessão persistida.
- Esse padrão é útil para smoke tests do carrossel: validar login persistido, acesso ao chat isolado e geração da primeira slide antes de expandir para o carrossel inteiro.

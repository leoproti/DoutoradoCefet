# Guia Rápido de Notas para LaTeX

## Caracteres especiais
- Sempre escape _ (\_) e ^ (\^{}) em textos, tabelas e legendas.
- Não escape underscores em labels (\label{tab:meu_label_com_underscore}).

## Tabelas grandes
- Use o pacote `pdflscape` e o ambiente `landscape` para tabelas largas.
- Use `\resizebox{\textwidth}{!}{...}` para ajustar tabelas grandes à página.
- Divida tabelas muito longas em partes menores.

## Avisos comuns
- "Missing $ inserted": caractere especial não escapado.
- "Float too large for page": tabela ou figura muito grande para a página.
- "Overfull \hbox": texto ou tabela ultrapassando a margem.

## Dicas gerais
- Use `\small` ou `\footnotesize` para tabelas extensas.
- Compile o documento mais de uma vez para atualizar referências.
- Limpe arquivos temporários (.aux, .log, .toc) se erros persistirem.

---

# Exemplo de tabela segura
```latex
\begin{table}
\caption{Exemplo de tabela com cabeçalho seguro}
\label{tab:exemplo_tabela}
\begin{tabular}{lll}
\toprule
coluna\_1 & coluna\_2 & valor\^{2} \\
\midrule
1 & 2 & 3 \\
\bottomrule
\end{tabular}
\end{table}
```

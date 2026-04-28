# Guia Rápido de Notas para Python (Geração de LaTeX)

## Exportando tabelas para LaTeX
- Sempre escape _ (\_) e ^ (\^{}) em cabeçalhos, valores e legendas.
- Não escape underscores em labels de tabelas.

## Função de escape recomendada
```python
def escapar_latex(texto):
    return str(texto).replace('_', '\\_').replace('^', '\\^{}')
```

## Exemplo de exportação segura
```python
caption = f'Tabela gerada a partir do arquivo {escapar_latex(arquivo.name)}'
label = f'tab:{arquivo.stem}'  # Não escapar aqui!
df.columns = [escapar_latex(col) for col in df.columns]
for col in df.columns:
    df[col] = df[col].astype(str).apply(escapar_latex)
tabela_latex = df.to_latex(index=False, caption=caption, label=label, escape=False)
```

## Dicas gerais
- Use pandas para gerar tabelas: `df.to_latex()`
- Para tabelas grandes, considere dividir ou usar `\resizebox` no LaTeX.
- Sempre teste a compilação após gerar novos arquivos .tex.

---

# Erros comuns
- "Missing $ inserted": caractere especial não escapado.
- "Double subscript": uso de ^ ou _ não escapado.
- "Float too large for page": tabela muito grande para a página.

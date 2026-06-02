# Pratica de Automatos de Wolfram

Este projeto foi criado para o trabalho sobre automatos celulares elementares de Wolfram.

## Objetivo

Aplicar o conteudo sobre automatos de Wolfram, implementando um programa que:

1. Recebe o numero da regra (0 a 255) e mostra a evolucao espaco-temporal.
2. Permite escolher estado inicial:
   - um sitio ocupado (single)
   - aleatorio (random)
3. Permite escolher densidade inicial de sitios ocupados e se os sitios ficam:
   - agrupados (grouped)
   - espalhados (spread)

## Estrutura

- `src/wolfram_automato.py`: implementacao principal (CLI)
- `src/automatos_wolfram.ipynb`: notebook para exploracao e relatorio
- `relatorioCefet/`: estrutura do relatorio em LaTeX

## Como executar

No PowerShell, dentro desta pasta:

```powershell
python -m pip install -r requirements.txt
python src/wolfram_automato.py --rule 30 --width 151 --steps 120 --initial random --density 0.35 --spread
```

Para estado inicial com um unico sitio ocupado:

```powershell
python src/wolfram_automato.py --rule 110 --width 151 --steps 120 --initial single
```

Para salvar figura:

```powershell
python src/wolfram_automato.py --rule 90 --width 151 --steps 120 --initial random --density 0.4 --grouped --save-fig src/graficos/regra90.png
```

## Entrega

- PDF do relatorio (em `relatorioCefet`)
- Executavel do codigo (sugestao: gerar com PyInstaller)


python -m PyInstaller --onefile --windowed --name automatos_wolfram_gui .\automatos_wolfram_gui.py
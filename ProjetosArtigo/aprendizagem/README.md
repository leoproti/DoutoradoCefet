# Projetos de Artigo com Dados do Setor Agropecuario

Este projeto foi estruturado para ajudar na criacao de estudos quantitativos com foco em publicacao de artigos sobre o setor agropecuario.

O objetivo e permitir que voce:

- organize bases de dados do agro em um fluxo reproduzivel;
- rode analises exploratorias rapidamente;
- gere tabelas e graficos iniciais para apoiar hipoteses;
- transforme a analise em um manuscrito com pergunta de pesquisa clara.

## Estrutura

```text
data/
  raw/              # bases originais
  processed/        # bases tratadas
docs/
  ideias-artigos.md # sugestoes de temas publicaveis
  roteiro-artigo.md # estrutura pratica do manuscrito
outputs/
  figures/          # graficos gerados
  tables/           # tabelas geradas
paper/
  main.tex          # arquivo principal do artigo
  sections/         # secoes separadas do manuscrito
  refs/             # bibliografia em BibTeX
  figures/          # figuras finais selecionadas para o paper
  tables/           # tabelas finais selecionadas para o paper
  build/            # artefatos de compilacao
src/
  agro_artigo/
    analysis.py     # funcoes de analise
    cli.py          # interface de linha de comando
requirements.txt
```

## Como usar

1. Coloque um arquivo CSV em `data/raw/`.
2. Instale as dependencias:

```powershell
python -m pip install -r requirements.txt
```

3. Rode a analise:

```powershell
python -m src.agro_artigo.cli --input data/raw/seu_arquivo.csv --target producao
```

4. Consulte os resultados em `outputs/tables/` e `outputs/figures/`.
5. Escreva o manuscrito em `paper/`, usando `paper/main.tex` como ponto de entrada.

## Fluxo recomendado

1. Analise e trate os dados em `data/`, `src/` e `outputs/`.
2. Selecione apenas as figuras e tabelas finais para `paper/figures/` e `paper/tables/`.
3. Escreva o artigo por secoes em `paper/sections/`.
4. Mantenha as referencias em `paper/refs/references.bib`.
5. Compile o artigo a partir de `paper/main.tex`.

Exemplo com `pdflatex`:

```powershell
Set-Location paper
pdflatex -output-directory build main.tex
```

Exemplo com `latexmk`:

```powershell
Set-Location paper
latexmk -pdf -output-directory=build main.tex
```

Atalho recomendado no Windows:

```powershell
./paper/compile.ps1
```

## Tipos de estudos que este projeto suporta

- produtividade agricola por cultura, regiao e periodo;
- relacao entre credito rural e producao;
- impacto de clima sobre rendimento;
- comparacao entre municipios ou estados;
- associacao entre tecnologia, area plantada e valor da producao.
- deteccao de anomalias e suspeitas de fraude em GTAs.

## Analise de fraude em GTAs

O projeto tambem suporta uma trilha inicial de investigacao de fraude com dados de Guias de Transito Animal.

Abordagem estatistica inicial:

- identificacao de registros duplicados;
- deteccao de outliers por IQR em variaveis numericas;
- concentracao anomala por emitente, produtor, propriedade ou municipio;
- padroes temporais incomuns, como emissao noturna, em fim de semana ou picos abruptos.

Abordagem de IA inicial:

- deteccao nao supervisionada de anomalias com Isolation Forest;
- ranking de registros mais suspeitos para auditoria;
- combinacao de sinais estatisticos e score de anomalia.

Exemplo de uso para GTAs:

```powershell
python -m src.agro_artigo.fraud_cli \
  --input data/raw/gtas.csv \
  --output outputs/fraud \
  --date-column data_emissao \
  --id-columns numero_gta \
  --entity-columns emitente_id produtor_id municipio_origem municipio_destino \
  --numeric-columns quantidade_animais distancia_km valor_declarado
```

Detalhamento metodologico: ver `docs/fraude-gta.md`.

## Fontes de dados recomendadas

- IBGE SIDRA
- CONAB
- MAPA
- CEPEA
- INMET
- Banco Central do Brasil
- IPEA Data

## Onde publicar

### Periodicos com foco em tecnologia aplicada ao agro

- Computers and Electronics in Agriculture: forte aderencia para IA, machine learning, sensores, visao computacional, automacao e agricultura de precisao. Pagina oficial: https://www.sciencedirect.com/journal/computers-and-electronics-in-agriculture
- Smart Agricultural Technology: adequado para sistemas inteligentes, analytics, IoT, apoio a decisao e aplicacoes praticas em ambiente produtivo. Pagina oficial: https://www.sciencedirect.com/journal/smart-agricultural-technology
- Agricultural Systems: melhor quando o artigo usa dados para explicar desempenho, sustentabilidade, sistemas produtivos e transformacao digital no agro. Pagina oficial: https://www.sciencedirect.com/journal/agricultural-systems

### Periodicos com foco em agronegocio, economia e cadeias produtivas

- Journal of Agribusiness in Developing and Emerging Economies: muito aderente para temas empiricos sobre agronegocio em economias emergentes, incluindo tecnologia da informacao, cadeias de valor, eficiencia, mercado e politica. Pagina oficial: https://www.emeraldgrouppublishing.com/journal/jadee
- Revista de Economia e Sociologia Rural: opcao forte para estudos com base brasileira sobre economia rural, inovacao, produtividade e politica publica. Pagina oficial: https://www.scielo.br/j/resr/

### Eventos para testar o trabalho antes da submissao

- IFAMA: evento e rede internacional com foco em food and agribusiness. Pagina oficial: https://www.ifama.org/
- SOBER: principal trilha brasileira para economia, administracao e sociologia rural. Pagina oficial: https://sober.org.br/

### Regra pratica de escolha

- Se o artigo for centrado no metodo ou algoritmo, priorize Computers and Electronics in Agriculture ou Smart Agricultural Technology.
- Se o artigo enfatizar impacto em sistemas agropecuarios, produtividade ou sustentabilidade, priorize Agricultural Systems.
- Se o artigo enfatizar agronegocio, mercado, cadeias, credito, eficiencia ou politica publica, priorize JADEE ou Revista de Economia e Sociologia Rural.

## Observacoes metodologicas

- Comece com uma pergunta estreita e mensuravel.
- Priorize dados com recorte temporal ou regional consistente.
- Evite artigo puramente descritivo; tente sempre introduzir uma comparacao, associacao ou avaliacao de impacto.
- Registre definicoes de variaveis, filtros e transformacoes para garantir reproducibilidade.
# Analise de Fraude em GTAs

## Objetivo

Construir uma trilha inicial para detectar comportamentos atipicos e possiveis indicios de fraude em Guias de Transito Animal do Instituto Mineiro de Agropecuaria.

## Perguntas de pesquisa

- Quais emissores, propriedades ou rotas apresentam comportamento estatisticamente incomum?
- Existem picos de emissao ou volumes de animais incompatíveis com o padrao historico?
- Ha combinacoes atipicas de origem, destino, especie, finalidade ou quantidade transportada?
- Um algoritmo de deteccao de anomalias consegue priorizar registros suspeitos para auditoria?

## Trilhas recomendadas

### 1. Estatistica descritiva e investigativa

- frequencia de emissao por dia, semana, mes e horario;
- distribuicao por municipio de origem e destino;
- ranking de emissores e produtores por volume e frequencia;
- identificacao de duplicidades ou inconsistencias documentais;
- outliers em quantidade de animais, distancia, valor e intervalo entre emissoes.

### 2. Regras de negocio e red flags

- GTA emitida em horario improvavel;
- alta frequencia de emissao em janela curta;
- mesma origem com destinos incomuns em sequencia curta;
- volumes muito acima do perfil historico do emitente;
- divergencia entre especie, finalidade e quantidade declarada.

### 3. IA para deteccao de anomalias

- Isolation Forest para score de anomalia sem rotulo;
- clusterizacao para identificar perfis operacionais e desvios;
- classificacao supervisionada apenas se houver historico confiavel de fraude confirmada.

## Variaveis potencialmente uteis

- numero da GTA;
- data e hora de emissao;
- emitente, produtor, propriedade e responsavel tecnico;
- municipio e UF de origem e destino;
- especie, finalidade e quantidade de animais;
- distancia estimada, valor declarado e historico do agente emissor.

## Resultado esperado para artigo

Um artigo inicial pode comparar o desempenho de metodos estatisticos e de IA na priorizacao de GTAs suspeitas, discutindo aplicabilidade regulatoria e ganho operacional para auditoria.
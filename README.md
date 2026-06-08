# ✈️ Predição de Satisfação de Passageiros em Aeroportos Brasileiros

> Uma abordagem com **LightGBM** e **SHAP Values** para prever e explicar a satisfação de passageiros, utilizando dados reais da Secretaria Nacional de Aviação Civil (SNAC).

**Instituição:** Universidade Federal de Alagoas (UFAL) — Instituto de Computação  
**Disciplina:** Ciência de Dados  
**Equipe:** Helio José, Ludson Lira, Raul Alves, Walber Luis, Kaue Patricius

---

## 🚀 Destaques do Projeto

| Aspecto | Detalhe |
|---|---|
| **Dataset** | 57.514 registros reais × 145 variáveis (Dados Abertos — SNAC) |
| **Modelo Final** | LightGBM — **81,72% de acurácia** · **AUC-ROC 0,8957** |
| **Explicabilidade** | Análise SHAP com insights acionáveis por variável |
| **Hipóteses Validadas** | 3/3 hipóteses de negócio confirmadas estatisticamente |
| **Artigo Científico** | Formato SBC (Sociedade Brasileira de Computação), 10–12 páginas |

### Principais Descobertas

- **"O básico é o diferencial"** — Limpeza geral e facilidade de locomoção são os maiores detratores da satisfação, superando fatores comerciais.
- **Conforto compensa fricção** — Investir em conforto na sala de embarque (climatização, mobiliário) possui retorno direto e linear na retenção do passageiro.
- **Desembarque é o gargalo** — O processo pós-voo (bagagem, saída) concentra os piores índices de avaliação (média 3,73 vs. 4,07 no embarque).

---

## 📂 Estrutura do Repositório

```
brazilian-airport-satisfaction/
│
├── data/
│   ├── raw/                          # Dataset original (passenger_survey_balanced.csv)
│   └── processed/                    # Dataset limpo e codificado (df_model.csv)
│
├── src/                              # Pipeline modularizado em Python
│   ├── explorer.py                   # DataExplorer — EDA e visualizações exploratórias
│   ├── preprocessor.py               # DataPreprocessor — Limpeza, imputação e encoding
│   ├── modeler.py                    # ModelTrainer — Arena de algoritmos, SHAP e exportação
│   └── utils.py                      # Funções utilitárias
│
├── notebooks/                        # Fluxo interativo de experimentação
│   ├── 01_exploracao.ipynb           # Análise Exploratória de Dados (EDA)
│   ├── 02_pre_process.ipynb          # Pré-processamento e engenharia de atributos
│   └── 03_modelagem.ipynb            # Modelagem, validação cruzada e SHAP
│
├── outputs/
│   ├── figures/                      # Gráficos gerados pelo pipeline
│   │   ├── distribuicao_alvo.png     # Distribuição da variável alvo (liked)
│   │   ├── heatmap_correlacao.png    # Matriz de correlação (Top 15 vs Liked)
│   │   ├── atrasos_vs_satisfacao.png # Boxplot: Arrival Lead Time × Satisfação
│   │   ├── satisfacao_por_tipo_voo.png # Taxa de aprovação por tipo de voo
│   │   ├── model_benchmarking.png    # Comparativo dos 5 algoritmos (CV K=5)
│   │   ├── matriz_confusao.png       # Matriz de confusão do LightGBM
│   │   ├── feature_importance.png    # Importância das features (Top 15)
│   │   └── shap_summary.png         # SHAP Summary Plot (beeswarm)
│   └── models/
│       └── melhor_modelo_lightgbm.pkl # Modelo treinado serializado (joblib)
│
├── docs/                             # Documentação completa do projeto
│   ├── ANALYSIS_OVERVIEW.md          # Relatório técnico consolidado
│   ├── PROJECT_DESCRIPTION.md        # Especificações da disciplina
│   ├── INICIAL_PROPOSITION.md        # Proposta inicial (Parte 1 da entrega)
│   ├── PITCH_SCRIPT.md              # Roteiro do pitch gerencial (5 min)
│   ├── MONITORS_SUGESTION.md        # Diretrizes e sugestões do docente
│   ├── TEX_PLAN.md                  # Plano de seções do artigo SBC
│   ├── TEX_BACKLOG.md               # Backlog de tarefas do artigo
│   └── tex/                          # Artigo científico em LaTeX (template SBC)
│       ├── main.tex                  # Texto completo do artigo
│       ├── sbc-template.bib          # Referências bibliográficas
│       ├── sbc-template.sty          # Estilo SBC
│       └── fig[1-5].*               # Figuras do artigo
│
├── entregas_finais/                  # PDFs finais (Pitch + Relatório SBC)
├── main.py                          # Ponto de entrada — executa o pipeline completo
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Este arquivo
```

---

## 🛠️ Como Executar

### Pré-requisitos

- Python 3.8+
- pip

### 1. Instalação das dependências

```bash
pip install -r requirements.txt
```

As bibliotecas utilizadas são:

| Biblioteca | Função |
|---|---|
| `pandas` | Manipulação e análise de dados |
| `scikit-learn` | Modelos de ML, métricas e validação cruzada |
| `matplotlib` / `seaborn` | Visualização de dados |
| `xgboost` | Algoritmo de gradient boosting |
| `lightgbm` | Modelo final de alta performance |
| `shap` | Explicabilidade do modelo (SHAP values) |

### 2. Execução via Script (Pipeline Automático)

```bash
python main.py
```

O script executa sequencialmente as três fases do pipeline:

1. **Exploração (EDA)** — Carrega os dados brutos, gera estatísticas descritivas e salva os gráficos exploratórios em `outputs/figures/`.
2. **Pré-processamento** — Trata nulos estruturais (flags `_is_applicable`), imputa resíduos (mediana/moda), aplica One-Hot Encoding e exporta o dataset limpo para `data/processed/`.
3. **Modelagem** — Executa a "Arena de Algoritmos" (5 modelos com CV K=5), treina o campeão, gera relatórios de classificação, matriz de confusão, SHAP values e salva o modelo em `outputs/models/`.

### 3. Execução via Notebooks

Siga a ordem numérica na pasta `notebooks/` para acompanhar a evolução da análise com comentários detalhados:

```
01_exploracao.ipynb → 02_pre_process.ipynb → 03_modelagem.ipynb
```

---

## 📊 Resultados

### Arena de Algoritmos (Validação Cruzada K=5)

| Algoritmo | Acurácia Média | Desvio Padrão (±) |
|---|:---:|:---:|
| Regressão Logística | 79,71% | 0,59% |
| Árvore de Decisão | 79,30% | 0,92% |
| Random Forest | 80,24% | 0,48% |
| XGBoost | 81,61% | 0,74% |
| **LightGBM** 🏆 | **81,72%** | **0,66%** |

### Relatório de Classificação (LightGBM — Conjunto de Teste)

| Classe | Precision | Recall | F1-Score | Suporte |
|---|:---:|:---:|:---:|:---:|
| 0 (Insatisfeito) | 0,85 | 0,77 | 0,81 | 5.752 |
| 1 (Satisfeito) | 0,79 | 0,86 | 0,82 | 5.751 |
| **Acurácia Global** | | | **0,82** | **11.503** |

**AUC-ROC: 0,8957**

### Validação de Hipóteses

| Hipótese | Status | Evidência |
|---|:---:|---|
| H1: Fatores operacionais > comerciais | ✅ Válida | SHAP: limpeza e locomoção no topo da importância |
| H2: Voos internacionais mais exigentes | ✅ Válida | Maior criticidade em conforto físico e tempos de espera |
| H3: Desembarque como gargalo crônico | ✅ Válida | Média 3,73 (desembarque) vs. 4,07 (embarque) |

---

## 📝 Documentação

| Documento | Descrição |
|---|---|
| [Relatório Técnico](docs/ANALYSIS_OVERVIEW.md) | Visão completa do projeto: problema, dados, métodos, resultados e conclusões |
| [Proposta Inicial](docs/INICIAL_PROPOSITION.md) | Definição da base e hipóteses (Parte 1 da entrega) |
| [Roteiro do Pitch](docs/PITCH_SCRIPT.md) | Script para o pitch gerencial de 5 minutos |
| [Plano do Artigo](docs/TEX_PLAN.md) | Estrutura de seções do artigo SBC com estimativas de páginas |
| [Artigo LaTeX](docs/tex/main.tex) | Artigo científico completo no formato SBC |

---

## 🏛️ Contexto Acadêmico

Este projeto é o trabalho final da disciplina de **Ciência de Dados** do Instituto de Computação da UFAL. A entrega contempla:

- **Parte 1** (2,0 pts) — Proposta inicial com definição da base e hipóteses
- **Parte 2** (8,0 pts) — Entrega final com:
  - Apresentação: Pitch gerencial (5 min) + Técnica (15 min) = 5,0 pts
  - Documento final em formato SBC (máx. 12 páginas) = 3,0 pts
- **Pontuação Extra** (1,0–2,0 pts) — Pipeline automatizado, explicabilidade SHAP e código modularizado

---

## 📚 Referências

1. BRASIL. Secretaria Nacional de Aviação Civil. *Dados Abertos: Pesquisa de Satisfação do Passageiro*.
2. LUNDBERG, S. M.; LEE, S. I. *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems, 2017.
3. KE, G. et al. *LightGBM: A Highly Efficient Gradient Boosting Decision Tree*. NIPS, 2017.

---

## 📄 Licença

Projeto acadêmico — Universidade Federal de Alagoas (UFAL), 2026.
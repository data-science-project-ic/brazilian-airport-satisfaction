Aqui está o modelo completo de seções para o seu artigo SBC:

---

## Modelo de Seções — Artigo SBC (10–12 páginas)

### Estimativa de espaço por seção

| Seção | Páginas estimadas |
|---|---|
| Título, Autores, Abstract, Resumo | ~0.5 |
| 1. Introdução | ~1.0 |
| 2. Trabalhos Relacionados | ~1.0 |
| 3. Base de Dados e Pré-processamento | ~1.5 |
| 4. Metodologia | ~1.5 |
| 5. Experimentos e Resultados | ~2.5 |
| 6. Discussão | ~1.0 |
| 7. Conclusão e Trabalhos Futuros | ~0.5 |
| Referências | ~0.5 |
| **Total** | **~10–11 páginas** |

> Ajuste o volume de texto e figuras para atingir 10–12 páginas. Tabelas e figuras costumam "esticar" bem o conteúdo sem comprometer a qualidade.

---

### Cabeçalho (fora das seções numeradas)

**Conteúdo obrigatório pelo template SBC:**
- Título centrado, 16pt bold: *"Predição de Satisfação de Passageiros em Aeroportos Brasileiros: Uma Abordagem com LightGBM e SHAP Values"* (ou variação)
- Nomes dos 5 autores, afiliação (UFAL — Instituto de Computação), e-mails no formato Courier
- **Abstract** em inglês (máx. 10 linhas): síntese do problema, método, resultado principal (AUC-ROC 0.8957, acurácia 81.72%) e contribuição
- **Resumo** em português (máx. 10 linhas): idem em PT-BR

---

### Seção 1 — Introdução (~1 página)

**Objetivo:** Contextualizar o problema, motivar o leitor e declarar as contribuições do trabalho.

**O que incluir:**
- Parágrafo 1: A experiência do passageiro como fator estratégico para companhias e aeroportos; gestão reativa vs. proativa
- Parágrafo 2: Lacuna existente — ausência de modelos preditivos baseados em dados reais brasileiros (Dados Abertos da SNAC)
- Parágrafo 3: O que o trabalho faz — pipeline completo de ML com 57.514 registros, 145 variáveis, comparação de 5 algoritmos, explicabilidade via SHAP
- Parágrafo 4 (contribuições, em lista curta ou prosa): (i) validação empírica de hipóteses sobre satisfação em aeroportos BR; (ii) modelo LightGBM com AUC-ROC de 0.8957; (iii) análise SHAP com recomendações acionáveis
- Último parágrafo: Estrutura do artigo — *"O restante do artigo está organizado da seguinte forma: ..."*

**Nenhuma figura necessária aqui.**

---

### Seção 2 — Trabalhos Relacionados (~1 página)

**Objetivo:** Posicionar o trabalho na literatura; mostrar o que existe e o que este trabalho adiciona.

**O que incluir:**
- Subgrupo 1: Modelos de predição de satisfação de passageiros em aviação (ex: NPS, pesquisas de serviços aéreos)
- Subgrupo 2: Uso de *gradient boosting* (XGBoost, LightGBM) em problemas de classificação tabulares com alta dimensionalidade
- Subgrupo 3: Explicabilidade em ML — SHAP values (citar Lundberg & Lee, 2017 — já está na sua bibliografia)
- Parágrafo final de diferenciação: *"Diferente dos trabalhos anteriores, este utiliza dados abertos do governo brasileiro, abrange 57 mil registros reais e combina modelagem preditiva com análise de explicabilidade para geração de insights operacionais."*

**Nenhuma figura obrigatória, mas você pode incluir uma tabela comparativa** de trabalhos relacionados (Trabalho | Dataset | Método | Métrica principal) — ocupa ~meia página e demonstra maturidade acadêmica.

---

### Seção 3 — Base de Dados e Pré-processamento (~1.5 páginas)

**Objetivo:** Descrever os dados e o pipeline de preparação com rigor reprodutível.

**O que incluir:**

**3.1 Origem e Caracterização**
- Fonte: Dados Abertos da Secretaria Nacional de Aviação Civil
- Dimensões: 57.514 registros × 145 variáveis originais
- Variável alvo `liked`: binária, distribuição ~50/50 (mencione que não exige SMOTE)

**3.2 Desafios e Tratamento de Nulos**
- Total de valores nulos: 3.323.783
- Estratégia estrutural: flags `_is_applicable` → imputação como `-1` para serviços inaplicáveis
- Imputação de resíduos: mediana (numéricas), moda (categóricas)

**3.3 Engenharia de Atributos**
- One-Hot Encoding em 23 variáveis categóricas → expansão para 252 atributos
- Limpeza de caracteres especiais nos nomes de colunas (compatibilidade com Gradient Boosting)

**Figuras/Tabelas recomendadas:**
- **Figura 1:** Diagrama do pipeline de pré-processamento (fluxograma: dados brutos → tratamento nulos → encoding → dataset final). Use `\includegraphics` com figura gerada em Python/draw.io
- **Tabela 1:** Resumo estatístico das principais variáveis (média, mediana, % nulos antes do tratamento) — 5 a 8 variáveis mais relevantes

---

### Seção 4 — Metodologia (~1.5 páginas)

**Objetivo:** Descrever a "Arena de Algoritmos", os critérios de seleção do modelo final e a estratégia de validação.

**O que incluir:**

**4.1 Algoritmos Avaliados**
- Apresente os 5 modelos em tabela ou prosa estruturada: Regressão Logística (baseline), Árvore de Decisão, Random Forest, XGBoost, LightGBM
- Justificativa de cada escolha em 1–2 linhas

**4.2 Estratégia de Validação**
- Hold-out 80/20 com estratificação pela variável alvo
- K-Fold Cross-Validation (K=5) no conjunto de treino
- Justifique: *"A estratificação garante a proporção ~50/50 da variável alvo em treino e teste"*

**4.3 Métricas de Avaliação**
- Acurácia, Precision, Recall, F1-Score, AUC-ROC
- Explique brevemente por que AUC-ROC é especialmente relevante para o contexto (custo assimétrico de classificar erroneamente insatisfeitos como satisfeitos)

**4.4 Explicabilidade com SHAP**
- Introduza SHAP values em 1 parágrafo: o que são, por que foram escolhidos, referência a Lundberg & Lee (2017)

**Figuras/Tabelas recomendadas:**
- **Tabela 2:** Comparação dos 5 algoritmos (Algoritmo | Acurácia | F1 | AUC-ROC | Tempo de treino) — esta é uma das tabelas mais importantes do artigo

---

### Seção 5 — Experimentos e Resultados (~2.5 páginas)

**Objetivo:** Apresentar e analisar os resultados de forma objetiva, com suporte visual.

**O que incluir:**

**5.1 Análise Descritiva da Base**
- Distribuição da variável alvo (gráfico de barras ou pizza)
- Correlações mais altas com `liked` (heatmap parcial ou barras horizontais com top-10 variáveis correlacionadas)
- Validação das hipóteses levantadas no overview (atrasos, voos internacionais, desembarque)

**5.2 Performance Comparativa dos Modelos**
- Discuta a Tabela 2 (definida na seção 4): por que LightGBM venceu
- Acurácia final do LightGBM: **81.72%** na validação cruzada, estável no teste

**5.3 Análise de Explicabilidade (SHAP)**
- SHAP Summary Plot: importância global das variáveis — **indispensável como figura**
- SHAP Beeswarm ou Bar Plot: top-15 features e direção do impacto
- Destaque para `location_and_movement` e limpeza como principais drivers negativos; conforto da sala de embarque como driver positivo

**5.4 Validação das Hipóteses**
Apresente as 3 hipóteses validadas (tabela ou lista estruturada):

| Hipótese | Status | Evidência principal |
|---|---|---|
| H1: Fatores operacionais > comerciais | Válida | SHAP: limpeza e locomoção no topo |
| H2: Voos internacionais mais exigentes | Válida | Correlação conforto × insatisfação mais forte |
| H3: Desembarque como gargalo | Válida | Média 3.73 (desembarque) vs. 4.07 (embarque) |

**Figuras recomendadas:**
- **Figura 2:** Distribuição da variável alvo `liked`
- **Figura 3:** Heatmap de correlação (top variáveis com `liked`)
- **Figura 4:** SHAP Summary Plot (beeswarm) — top 15 features
- **Figura 5:** Curva ROC do LightGBM (AUC = 0.8957)
- **Tabela 3:** Matriz de confusão do LightGBM no conjunto de teste

> Esta seção concentra a maioria das figuras — planeje para ~2 a 2.5 colunas de conteúdo visual.

---

### Seção 6 — Discussão (~1 página)

**Objetivo:** Interpretar os resultados além dos números; conectar com implicações práticas.

**O que incluir:**
- O que a performance do LightGBM (81.72%, AUC 0.8957) significa no contexto real: um gestor aeroportuário pode confiar nesse modelo para triagem de risco?
- Por que "o básico é o diferencial": limpeza e locomoção superam bônus e comodidades premium na predição — implicação contra-intuitiva importante
- Ação tática recomendada: reforço de equipes em horários de pico identificados pelo modelo
- Ação estratégica recomendada: investimento em salas VIP e conforto térmico como compensadores de fricção logística
- Limitações do trabalho: dados históricos (sem tempo real), ausência de variáveis externas (clima, tráfego aéreo), possível viés de resposta nas pesquisas de satisfação

---

### Seção 7 — Conclusão e Trabalhos Futuros (~0.5 página)

**Objetivo:** Síntese do trabalho e direções futuras.

**O que incluir:**
- Parágrafo 1 (conclusão): Reafirme o problema, o método e os principais resultados em 4–5 linhas. Não repita seções — sintetize.
- Parágrafo 2 (trabalhos futuros): 
  - Integração de dados meteorológicos e de tráfego aéreo em tempo real
  - Expansão do modelo para predição contínua (sistema de alerta)
  - Análise por aeroporto específico (modelo hierárquico ou por cluster)
  - Deploy como API para uso pelos gestores da SNAC

---

### Referências

Use o estilo `\bibliographystyle{sbc}` já definido no template. Adicione além das 3 já listadas:

- Artigos de trabalhos relacionados que você citar na Seção 2
- Documentação do scikit-learn / LightGBM se citar hiperparâmetros específicos
- A base de dados: *BRASIL. Secretaria Nacional de Aviação Civil. Dados Abertos: Pesquisa de Satisfação do Passageiro* — já está no overview

---

### Dicas finais para bater as 10–12 páginas

Se ficar curto, expanda nestas direções sem perder qualidade:

- **Seção 3:** Adicione uma tabela de estatísticas descritivas com mais variáveis
- **Seção 4:** Descreva os hiperparâmetros finais do LightGBM em uma tabela
- **Seção 5.3:** Adicione um SHAP Force Plot ou Waterfall Plot para um passageiro satisfeito e um insatisfeito (análise individual)
- **Seção 2:** Expanda para 1.5 páginas com tabela comparativa de literatura

Se ficar longo demais, corte em: Seção 2 (reduza literatura), Seção 6 (una com Conclusão).
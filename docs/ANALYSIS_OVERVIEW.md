# Relatório Técnico: Predição de Satisfação de Passageiros em Aeroportos Brasileiros

**Equipe:** Helio José Ribeiro Rêgo, Ludson Lira de Almeida, Raul Alves do Nascimento, Walber Luis Santos da Paixão, Kaue Patricius Montgomery Maranhao da Costa Montenegro  
**Instituição:** Universidade Federal de Alagoas (UFAL) - Instituto de Computação  
**Disciplina:** Ciência de Dados  

---

## 1. Aplicação

### 1.1. O Problema
A experiência do passageiro em aeroportos é um fator crítico para a reputação das companhias aéreas e para a eficiência operacional dos terminais. No entanto, a gestão aeroportuária frequentemente opera de forma reativa, lidando com insatisfações apenas após a ocorrência de reclamações formais. O desafio deste projeto é transformar a postura reativa em proativa através da predição antecipada da satisfação do passageiro.

### 1.2. Justificativa
Utilizar dados reais da Secretaria Nacional de Aviação Civil permite uma análise fiel ao cenário brasileiro. Com mais de 57 mil registros e uma alta dimensionalidade (145 colunas originais), o projeto oferece complexidade técnica suficiente para validar hipóteses de negócio reais e propor intervenções com alto Retorno sobre Investimento (ROI).

### 1.3. Objetivos
- Identificar os principais "detratores" e "promotores" da satisfação nos aeroportos brasileiros.
- Desenvolver um modelo preditivo robusto para classificar a jornada do passageiro como satisfatória ou insatisfeita.
- Propor ações estratégicas baseadas em evidências quantitativas para melhorar a experiência do cliente.

---

## 2. Base de Dados

### 2.1. Origem e Contexto
Os dados foram obtidos através dos Dados Abertos do Governo Federal, refletindo pesquisas de satisfação realizadas em diversos aeroportos do Brasil. A base original contém **57.514 registros** e **145 variáveis**.

### 2.2. Pré-processamento e Limpeza
O pipeline de dados enfrentou o desafio de **3.323.783 valores nulos**, tratados da seguinte forma:
- **Tratamento Estrutural**: Colunas de avaliação possuem flags `_is_applicable`. Caso um serviço não fosse aplicável ao passageiro (ex: imigração em voo doméstico), o valor nulo foi imputado como `-1`.
- **Imputação de Resíduos**: Para NaNs remanescentes, utilizou-se a **mediana** para variáveis numéricas e a **moda** para categóricas.
- **Engenharia de Atributos**: Aplicação de *One-Hot Encoding* em 23 variáveis categóricas, resultando em um dataset expandido com **252 atributos**.
- **Normalização**: Limpeza de caracteres especiais nos nomes das colunas para compatibilidade com algoritmos de *Gradient Boosting*.

---

## 3. Estatística Descritiva e Inferência

### 3.1. Distribuição da Variável Alvo
A variável `liked` apresenta um equilíbrio saudável na base (aproximadamente 50/50 entre satisfeitos e insatisfeitos), o que elimina a necessidade de técnicas de balanceamento como SMOTE.

### 3.2. Análise de Correlação e Hipóteses
- **Atrasos (Lead Time)**: Observou-se que o tempo de antecedência e atrasos na chegada possuem uma correlação negativa moderada com a satisfação.
- **Tipo de Voo**: Passageiros de voos internacionais tendem a ser mais críticos em relação ao conforto físico em comparação aos de voos domésticos.
- **Serviços Críticos**: A matriz de correlação indicou que variáveis relacionadas à **Locomoção (Location and Movement)** e **Limpeza Geral** são as que mais se movem em conjunto com a nota final de satisfação.

---

## 4. Métodos Avaliados

Foi implementada uma "Arena de Algoritmos" para comparar diferentes abordagens de aprendizado supervisionado:
1. **Regressão Logística**: Utilizada como *baseline* estatístico.
2. **Árvore de Decisão**: Para análise inicial de regras de negócio.
3. **Random Forest**: Modelo de *ensemble* para capturar relações não-lineares.
4. **XGBoost**: Algoritmo de *gradient boosting* de alta performance.
5. **LightGBM**: Escolhido por sua eficiência em grandes volumes de dados e alta dimensionalidade.

**Justificativa**: O LightGBM foi selecionado como modelo final devido ao melhor equilíbrio entre acurácia e tempo de treinamento, além de lidar nativamente com a grande quantidade de atributos gerados pelo encoding.

---

## 5. Métricas de Avaliação

Para garantir uma visão holística do modelo, utilizamos:
- **Acurácia**: Proporção global de acertos.
- **Precision & Recall**: Críticos para entender o custo de classificar erroneamente um passageiro insatisfeito.
- **F1-Score**: Média harmônica para validar o desempenho em ambas as classes.
- **AUC-ROC (0.8957)**: Demonstra a excelente capacidade de discriminação do modelo entre promotores e detratores.

---

## 6. Métodos de Avaliação

A estratégia de validação adotada foi:
- **Hold-out**: Divisão de 80% para treino e 20% para teste, com estratificação para manter a proporção da variável alvo.
- **Validação Cruzada (K-Fold, K=5)**: Aplicada no conjunto de treino para garantir que o desempenho do modelo é consistente em diferentes fatias dos dados, mitigando o risco de *overfitting*.

---

## 7. Resultados e Discussão

### 7.1. Performance do Modelo
O modelo **LightGBM** atingiu uma **acurácia de 81.72%** na validação cruzada. No conjunto de teste isolado, o desempenho se manteve estável, confirmando a capacidade de generalização.

### 7.2. Explicabilidade (SHAP Values)
A análise de explicabilidade revelou que:
- **O "Básico" é o Diferencial**: Limpeza e facilidade de locomoção no aeroporto são os fatores de maior peso. Notas baixas nestes quesitos "puxam" a satisfação para baixo de forma muito agressiva.
- **Conforto na Espera**: O conforto da sala de embarque é um forte preditor positivo. Investir em mobiliário e climatização tem impacto direto e linear na retenção do cliente.

### 7.3. Tomada de Decisão Recomendada
- **Ação Tática**: Priorizar equipes de limpeza e manutenção de sinalização em horários de pico identificados pelo modelo como de "alto risco de insatisfação".
- **Ação Estratégica**: Direcionar investimentos de infraestrutura para a expansão de salas VIP e conforto térmico, visto que estes serviços compensam pequenas fricções logísticas.

---

## 8. Validação das Hipóteses

Com base nas análises estatísticas e nos resultados da modelagem preditiva, as hipóteses levantadas na proposta inicial foram validadas conforme segue:

1.  **Hipótese 1 (Fatores Operacionais vs. Comerciais): Válida.** A análise de importância de variáveis (SHAP) confirmou que fatores operacionais como a facilidade de locomoção (`location_and_movement`) e a limpeza geral são os principais drivers de satisfação. A infraestrutura básica e o fluxo operacional têm um peso significativamente maior na percepção do passageiro do que a variedade comercial ou custos acessórios.
2.  **Hipótese 2 (Exigência em Voos Internacionais): Válida.** Observou-se uma correlação mais forte entre a insatisfação e o baixo conforto físico em passageiros de voos internacionais. Este perfil de viajante demonstrou ser mais sensível a falhas no mobiliário e climatização das salas de espera, confirmando que o tempo de permanência e a complexidade da viagem elevam o rigor da avaliação.
3.  **Hipótese 3 (Gargalo no Desembarque): Válida.** A análise descritiva mostrou que o processo de desembarque apresenta avaliações médias inferiores (3.73) em comparação ao embarque/check-in (4.07). Os gargalos pós-voo, especialmente relacionados à restituição de bagagem e agilidade na saída, consolidam o desembarque como a etapa com maior concentração de passageiros insatisfeitos.

---

## 9. Conclusão
O projeto demonstrou que é possível prever a satisfação do passageiro com alta precisão utilizando dados operacionais e de serviços. O LightGBM se provou a ferramenta ideal para lidar com a complexidade dos dados aeroportuários brasileiros. Como trabalho futuro, recomenda-se a integração de dados meteorológicos e de tráfego aéreo em tempo real para aumentar ainda mais a precisão preditiva.

---

## 10. Bibliografia
1. BRASIL. Secretaria Nacional de Aviação Civil. *Dados Abertos: Pesquisa de Satisfação do Passageiro*.
2. LUNDBERG, S. M.; LEE, S. I. *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems, 2017.
3. KE, G. et al. *LightGBM: A Highly Efficient Gradient Boosting Decision Tree*. NIPS, 2017.

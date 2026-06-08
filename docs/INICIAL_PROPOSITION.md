# Projeto Ciência de Dados: Definição da Base e Proposta Inicial

## Equipe

Helio José Ribeiro Rêgo, Ludson Lira de Almeida, Raul Alves do Nascimento, Walber Luis Santos da Paixão, Kaue Patricius Montgomery Maranhao da Costa Montenegro

---

## 1. Nome ou Tema da Base

**Airline Passenger Satisfaction Dataset** (Pesquisa de Satisfação do Passageiro em Aeroportos Brasileiros)

---

## 2. Origem dos Dados

- **Fonte Original**: Dados Abertos do Governo Federal (Secretaria Nacional de Aviação Civil)
- **Repositório ML**: Kaggle (versão estruturada e balanceada via script de limpeza)

---

## 3. Descrição Geral da Base

O dataset possui **57.514 registros** e **145 colunas** sobre a jornada de passageiros no Brasil, composto majoritariamente por avaliações (escala 1 a 5) e dados categóricos.

### Principais Características

- **Variável Alvo (liked)**: Binária
  - 1 para alta satisfação (notas 4 e 5)
  - 0 para baixa/média satisfação (notas 1 a 3)

- **Avaliações do Aeroporto**: Mais de 40 notas de infraestrutura e serviços, com travas de aplicabilidade (_is_applicable)

- **Perfil e Contexto**: Dados demográficos do passageiro e logísticos do voo

- **Métricas de Tempo**: Indicadores contínuos de antecedência (arrival_lead_time) e espera na conexão (connection_wait_time)

---

## 4. Justificativa da Escolha

Supera os critérios mínimos da disciplina (>5.000 linhas e >10 colunas) e traz a complexidade de um cenário real:

- **Dados Reais**: Livre de dados sintéticos ou vazamentos comuns em bases prontas do Kaggle

- **Dados Omissos Estruturais**: Presença de nulos legítimos (ex: voo direto não avalia imigração), exigindo tratamento avançado

- **Alta Dimensionalidade**: 145 colunas que desafiam a engenharia de atributos e evitam o overfitting

---

## 5. Problema Analisado

Prever a probabilidade de um passageiro considerar sua jornada **insatisfatória** (liked = 0) e identificar cientificamente quais **gargalos operacionais e de infraestrutura** são os principais detratores da experiência.

---

## 6. Tipo de Tomada de Decisão Apoiada

Direcionamento estratégico e tático de investimentos para gestores aeroportuários:

- **Otimização de Fluxo**: Decidir onde alocar verba (ex: reestruturação da segurança vs. expansão comercial) com base no peso real na satisfação

- **Dimensionamento de Pessoal**: Alocar equipes (check-in/limpeza) focando em horários e perfis criticados pelo modelo

---

## 7. Hipóteses Iniciais

### Hipótese 1
Fatores operacionais e de tempo (filas, check-in) impactam mais a satisfação do que o custo e a variedade comercial (lojas, restaurantes).

### Hipótese 2
Passageiros de voos internacionais ou conexões são mais exigentes com conforto físico (assentos, clima) do que os de voos domésticos diretos.

### Hipótese 3
O fluxo de desembarque concentra mais passageiros insatisfeitos do que o de embarque devido a gargalos pós-voo (bagagem, saída).

---

## 8. Possíveis Métodos Utilizados

- **Classificação Binária**: Regressão Logística, Random Forest, XGBoost e LightGBM

- **Interpretabilidade (XAI)**: Feature Importance e valores SHAP para isolar o impacto de cada serviço na nota final

- **Redução de Dimensionalidade**: PCA ou Análise Fatorial para agrupar as avaliações em macro-pilares (Conforto, Atendimento, Tempo)
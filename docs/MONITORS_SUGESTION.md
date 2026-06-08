# Ciência de Dados: Projeto Final - Especificações da Disciplina

Universidade Federal de Alagoas | Instituto de Computação | Ciência de Dados
**19 de maio de 2026**

---

## Sumário

1. Diretrizes e Especificações do Projeto
2. Estudo de Caso: O Desafio de Negócio
3. Boas Práticas de Visualização (EDA)
4. Framework de Modelagem Preditiva
5. O Pitch Gerencial

---

## Objetivos do Projeto Final

### Proposta Principal

Aplicar técnicas de Ciência de Dados em uma base de dados escolhida pela equipe, com foco na geração de conhecimento útil para apoiar uma tomada de decisão real ou simulada.

### Três Pilares Fundamentais

O trabalho é avaliado sob três pilares fundamentais:

1. **Conteúdo Técnico**: Domínio das etapas de análise, tratamento, modelagem e avaliação dos dados.

2. **Aplicação Prática**: Como os resultados encontrados podem apoiar uma tomada de decisão em um contexto real.

3. **Comunicação em Formato de Pitch**: Apresentar o problema, os resultados e as recomendações de forma convincente, como se estivesse defendendo a solução para um gestor ou banca avaliadora.

---

## Regras de Formação e Base de Dados

### Formação das Equipes

- **Graduação**: Grupos de até 5 pessoas. Grupos menores são permitidos quando não houver participantes suficientes para formar grupos de 5.
- **Mestrado**: O projeto deve ser realizado **individualmente**.

### Escolha do Conjunto de Dados

**Regra**: A escolha da base é livre, mas **não será permitido** utilizar as bases de dados já usadas nas listas 1 e 2, nem a base **"Hotel Booking Demand"**.

### Requisitos da Base

- **Tamanho**: Mais de 5.000 linhas e pelo menos 10 colunas úteis.
- **Variedade de variáveis**: Deve conter variáveis numéricas e categóricas, com pelo menos uma variável de resultado principal.
- **Preparação necessária**: Deve exigir etapas de preparação (tratamento de nulos, transformação de variáveis, remoção de inconsistências).
- **Potencial de insights**: Deve permitir gerar pelo menos 3 insights acionáveis.

---

## Estrutura do Documento Técnico

### Padrão de Formatação

O documento deve seguir o modelo de artigos da SBC e ter limite máximo de **12 páginas**.

### Seções Obrigatórias

1. **Aplicação**: Proposta, problema, justificativa e objetivos.

2. **Base de Dados**: Origem, contexto, registros, variáveis e pré-processamento.

3. **Estatística Descritiva e Inferência**: Distribuições, medidas de tendência, correlações e testes de hipótese.

4. **Métodos Avaliados**: Descrição dos métodos e justificativa da escolha.

5. **Métricas de Avaliação**: Métricas utilizadas para avaliar os métodos.

6. **Métodos de Avaliação**: Estratégia de avaliação (treino/teste, k-fold, etc.).

7. **Resultados e Discussão**: Resultados, limitações e relação com a tomada de decisão.

8. **Conclusão**: Resumo, descobertas e trabalhos futuros.

9. **Bibliografia**: Obras, artigos, bases de dados e referências consultadas.

---

## Submissão e Critérios de Avaliação

### Parte 1 — Proposta Inicial (2,0 pontos)

- PDF de até 2 páginas: descrição da base, origem, problema, hipóteses e possíveis métodos.
- Entrega via Classroom na atividade da turma virtual.

### Parte 2 — Entrega Final (8,0 pontos)

- **Apresentação** (5,0 pontos): Pitch (5 min) + Apresentação técnica (15 min).
- **Documento Final** (3,0 pontos): Estrutura, estatística, modelagem, resultados e discussão.

### Pontuação Extra (1,0 a 2,0 pontos)

Dashboard interativo, deploy de modelo, uso de LLMs, visualizações avançadas, entre outros.

---

## Introdução ao Estudo de Caso Hoteleiro

### O Problema

Nos últimos anos, um City Hotel e um Resort Hotel experimentaram aumentos significativos em suas taxas de cancelamento. Isso resultou em queda drástica de receita e quartos subutilizados.

- **Dataset**: 119.390 observações (reservas entre Jul/2015 e Ago/2017).
- **Objetivo do Cientista de Dados**: 
  - Entender as variáveis que afetam os cancelamentos.
  - Propor soluções acionáveis para melhorar a taxa de retenção.
  - Auxiliar a gerência em decisões de preços e promoções.

---

## Formulações de Hipóteses

Antes de modelar, um bom projeto define hipóteses claras a serem testadas (fase de experimentação do artigo):

### Hipóteses Iniciais

1. Mais cancelamentos ocorrem quando os preços das diárias são mais altos.

2. Clientes em listas de espera longas desistem e cancelam com mais frequência.

3. A maioria das reservas provém de agentes de viagem offline, o que dificulta o contato direto para retenção.

---

## O Papel Estratégico dos Gráficos

A Análise Exploratória de Dados (EDA) não deve ser apenas uma exibição aleatória de gráficos, mas sim a construção de uma narrativa que suporte suas hipóteses.

### Princípios Fundamentais

- **Não crie gráficos sem propósito**: Cada plot deve responder a uma pergunta de negócio ou justificar uma etapa da modelagem.

- **Apresente a "Dor" do Negócio**: Todo projeto deve começar ilustrando o tamanho do problema.

  - **Exemplo prático** (Hotel Booking): Um gráfico de barras ou pizza mostrando a distribuição da variável alvo (37% das reservas são canceladas). Isso prova que o problema existe e tem impacto financeiro.

---

## Tipos de Gráficos e Suas Aplicações no Projeto

### 1. Análise de Distribuição e Correlação (A Causa Raiz)

Use Boxplots ou Gráficos de Dispersão para encontrar o que aciona o problema.

- **No Estudo de Caso**: Boxplot comparando a Taxa Diária Média (ADR) com o status de cancelamento, provando que preços altos aumentam a evasão.

### 2. Sazonalidade e Tendências Temporais

Use Gráficos de Linhas para dados ao longo do tempo (dias, meses, anos).

- **No Estudo de Caso**: Linha do tempo mostrando o pico de cancelamentos no mês de Janeiro versus o pico de faturamento em Agosto.

---

## Segmentação e Perfis (Identificando Nichos)

Dividir os dados em categorias ajuda a direcionar as soluções e campanhas de marketing propostas na conclusão do artigo.

- **Gráficos de Barras (Top N categorias)**: Úteis para focar nos ofensores principais, ignorando categorias irrelevantes.
  - *Geografia*: Gráfico mostrando os 10 países que mais cancelam (Portugal no topo).
  - *Segmentação*: Gráfico cruzando canais de aquisição (Agências Online vs. Reservas Diretas) com a taxa de retenção.

**Dica para o Projeto**: Utilize paletas de cores consistentes (ex: vermelho para a classe negativa/problema, verde/azul para a positiva).

---

## Preparação de Dados e Engenharia de Atributos

Independentemente da base escolhida (saúde, finanças, turismo), os dados brutos raramente estão prontos para os algoritmos de Aprendizagem de Máquina:

- **Tratamento de Dados Faltantes e Outliers**: Decida se irá imputar dados (média, mediana) ou remover observações inválidas.

- **Engenharia de Atributos (Feature Engineering)**: Crie novas colunas baseadas no comportamento.
  - *Exemplo*: Criar uma variável binária "É final de semana?" a partir de datas, ou somar crianças + bebês para criar a variável "Família".

- **Codificação**: Transformar variáveis de texto (País, Canal de Distribuição) em números via *One-Hot Encoding* ou *Target Encoding*.

---

## Seleção de Algoritmos: Qual modelo usar?

Justifique a escolha do algoritmo no seu relatório técnico:

### Abordagem Recomendada

1. **Baseline (Ponto de Partida)**: Regressão Logística ou Árvore de Decisão simples. Fáceis de interpretar, mas capturam apenas relações lineares.

2. **Modelos Avançados (Ensembles)**: Random Forest, XGBoost ou LightGBM. Lidam bem com dados tabulares complexos, outliers e relações não-lineares (como o impacto conjunto de preço alto e longa antecedência).

**Importante**: Se a sua base for desbalanceada (ex: 90% de transações normais e 10% fraudes), utilize técnicas de balanceamento de classes (SMOTE ou pesos no algoritmo).

---

## Validação e Prevenção de Overfitting

O modelo não pode apenas decorar os dados; ele precisa generalizar para o mundo real. O rigor metodológico aqui vale muitos pontos na avaliação:

- **Separação Treino/Teste**: Nunca avalie o modelo nos mesmos dados em que ele foi treinado.

- **Validação Cruzada (k-fold)**: Dividir a base em K partes e treinar/avaliar iterativamente. Garante que os resultados não foram obra do acaso.

- **Seleção de Métricas (Além da Acurácia)**:
  - *F-measure (F1-Score)*: Ideal para lidar com dados desbalanceados.
  - *AUC-ROC*: Avalia a capacidade geral do modelo de distinguir entre as classes, independente de um limiar de corte rígido.

---

## Explicabilidade: Traduzindo Modelos para Negócios

Um modelo "caixa-preta" não convence gerentes nem investidores. Você precisa explicar o porquê das previsões.

- **Análise de Importância (Feature Importance)**: Quais variáveis mais pesaram nas decisões do algoritmo?

- **Valores SHAP**: Método avançado que mostra como cada característica afeta a previsão final.

  - **Exemplo prático**: O SHAP provará para o diretor do hotel que o fator "exigir vaga de estacionamento" empurra a probabilidade de cancelamento para baixo, enquanto "Lead time alto" empurra para cima.

---

## Estrutura da Apresentação

A apresentação terá tempo total de até **20 minutos**, organizados da seguinte forma:

### Pitch (5 minutos)

Apresentação em formato mais comercial, voltada para cliente, gestor ou banca avaliadora. O foco é o problema, os principais resultados e a recomendação final.

### Apresentação Técnica (15 minutos)

Explicação mais aprofundada da base, metodologia, modelos, métricas, resultados e limitações.

### Linha Lógica da Apresentação

- **Pitch**: Problema identificado → oportunidade → principais evidências → decisão proposta → impacto esperado.

- **Técnica**: Base utilizada → preparação dos dados → métodos/modelos aplicados → métricas utilizadas → resultados obtidos → limitações → justificativa da decisão final.

---

## Formato do Insight Acionável

Um bom insight deve ser claro, justificável e conectado ao problema. Ele deve surgir da combinação entre análise estatística, visualização de dados, modelagem e interpretação dos resultados.

### Estrutura Recomendada

**Percebemos que** [padrão nos dados]. **Isso sugere que** [interpretação do problema]. **Por isso, recomendamos** [ação prática]. **A decisão foi sustentada por** [métrica/evidência]. **Após** [período], **o sucesso pode ser avaliado por** [métrica principal]. **A ação será bem-sucedida se** [critério objetivo].

### Exemplo

"Percebemos que reservas com menos de 7 dias de antecedência têm taxa de cancelamento de 38%, contra 17% para reservas com mais de 30 dias. Isso sugere que reservas de última hora são mais instáveis. Por isso, recomendamos uma campanha de incentivo à reserva antecipada."

---

## Recomendações Estratégicas para o Gerente

(Seção com peso de 6,0 pontos no Projeto Final)

### 1. Precificação Dinâmica (Revenue Management)

Uma vez provada a correlação entre preço alto e desistência, implementar tarifas não-reembolsáveis com desconto ou pacotes promocionais atrativos para retenção, especialmente no Resort aos finais de semana.

### 2. Ataque ao "Vale" de Janeiro

Dado o alto índice de cancelamento proporcional em Janeiro, iniciar campanhas agressivas de marketing focadas neste mês, oferecendo benefícios para confirmação antecipada e pagamento antecipado.

### 3. Ações Direcionadas (Portugal e Online TAs)

Focar esforços de relacionamento e melhoria na qualidade dos serviços nos clientes provenientes de Portugal e reavaliar contratos e regras de tolerância junto às Agências de Viagem Online.

---

## Dicas Finais para a Defesa do seu Projeto

- **Conecte as seções**: Não mostre um gráfico sem um propósito. Se treinou um algoritmo complexo, explique de forma simples como a saída dele melhora o lucro ou corta custos da empresa escolhida.

- **Atenção ao Formato**: Respeitem o limite de 12 páginas, utilizem o template da SBC e documentem bem o código-fonte enviado no .zip.

- **Pratiquem a Apresentação**: Vocês terão um tempo limitado. Foco na claridade do problema, rigor metodológico e genialidade das soluções de negócios.

- **Todos devem participar**: Não é obrigatório que todos falem, mas todos devem estar presentes e aptos a responder perguntas sobre a base, a metodologia, os resultados e a decisão proposta.

---

## Sucesso nos Projetos e Boa Sorte! 🎓
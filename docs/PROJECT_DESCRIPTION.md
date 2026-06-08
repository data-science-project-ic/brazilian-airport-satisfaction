# Projeto Final - Ciência de Dados

## Universidade Federal de Alagoas
### Instituto de Computação
### Ciência de Dados

---

## Proposta

O projeto tem como objetivo aplicar técnicas de Ciência de Dados em uma base escolhida pela equipe, com foco na geração de conhecimento útil para apoiar uma tomada de decisão real ou simulada.

Além da parte técnica, o projeto deverá ser estruturado como um pitch, ou seja, a equipe deve apresentar sua análise de forma clara, objetiva e convincente, mostrando o valor dos dados para resolver um problema, identificar oportunidades ou propor melhorias.

A equipe deverá selecionar uma base de dados, realizar sua análise exploratória, aplicar técnicas estatísticas, métodos de mineração de dados e/ou aprendizagem de máquina, e apresentar conclusões que possam ser utilizadas para propor estratégias ou decisões fundamentadas nos dados.

### Três Aspectos Principais

O trabalho deverá contemplar:

1. **Conteúdo técnico**, demonstrando domínio das etapas de análise, tratamento, modelagem e avaliação dos dados
2. **Aplicação prática**, mostrando como os resultados encontrados podem apoiar uma tomada de decisão em um contexto real
3. **Comunicação em formato de pitch**, apresentando o problema, os resultados e as recomendações de forma convincente, como se a equipe estivesse defendendo sua solução para um gestor, empresa, cliente ou banca avaliadora

---

## Conjunto de Dados

A escolha da base de dados será livre, desde que esteja relacionada a um problema que permita análise, extração de padrões e geração de insights relevantes.

### Restrições

Não será permitido utilizar:
- As bases de dados já utilizadas para as listas 1 e 2
- A base "Hotel Booking" que vinha sendo utilizada na disciplina

É permitido utilizar mais de uma base de dados, desde que o conjunto atenda aos requisitos listados abaixo e produza um conjunto de informações que permita a condução do trabalho. Espera-se que as bases de dados não se repitam entre diferentes grupos, mas casos pontuais podem ser discutidos.

### Origem dos Dados

A base poderá ser obtida em:
- Repositórios públicos
- Bases governamentais
- Plataformas como Kaggle, UCI Machine Learning Repository
- Dados abertos ou outras fontes confiáveis

A origem deve ser clara e devidamente referenciada no trabalho.

### Critérios da Base Escolhida

#### 1. Tamanho Mínimo
- Preferencialmente mais de 5.000 linhas
- Pelo menos 10 colunas úteis para análise, desconsiderando IDs irrelevantes

#### 2. Variedade de Variáveis
- Deve conter variáveis numéricas e categóricas
- Deve ter pelo menos uma variável que possa ser usada como resultado principal da análise
- Deve conter variáveis que possibilitem exploração estatística e visual

#### 3. Problema de Negócio Claro
A base deve estar relacionada a um problema com potencial de tomada de decisão e permitir responder uma pergunta prática, por exemplo:
- Como aumentar reservas?
- Como reduzir cancelamentos?
- Como prever vendas?
- Como identificar clientes com maior chance de churn?
- Como melhorar o desempenho de alunos, campanhas, produtos ou serviços?

#### 4. Potencial para Modelagem
A base deve permitir a aplicação de técnicas de Ciência de Dados, Mineração de Dados ou Aprendizagem de Máquina.

#### 5. Necessidade de Preparação
- A base não deve estar "perfeita"
- Deve exigir pelo menos algumas etapas como: tratamento de nulos, transformação de variáveis, criação de novas colunas, remoção de inconsistências ou análise de outliers

#### 6. Potencial de Insights
A base precisa permitir gerar pelo menos 3 insights acionáveis, ou seja, recomendações que poderiam orientar uma decisão real.

### Justificativa da Escolha

A equipe deverá justificar a escolha da base, explicando o contexto do problema, a origem dos dados e o tipo de decisão que pretende apoiar a partir das análises.

**Observação para mestrandos:** Para alunos de mestrado, recomenda-se que a base utilizada esteja relacionada ao seu tema de pesquisa.

---

## Objetivos

O objetivo principal do projeto é gerar conhecimento a partir dos dados e utilizá-lo para apoiar uma tomada de decisão.

A equipe deverá apresentar uma proposta de aplicação prática dos resultados encontrados, explicando como os insights obtidos podem auxiliar uma organização, gestor, pesquisador ou usuário final.

### Perguntas a Responder

O projeto deve responder a perguntas como:
- Qual problema está sendo analisado?
- Por que esse problema é relevante?
- Que padrões ou relações podem ser identificados nos dados?
- Que decisões podem ser tomadas com base nas análises?
- Como os resultados podem gerar impacto prático?

---

## Tipo de Insight Esperado

Espera-se que os alunos produzam **insights acionáveis** que ultrapassem a simples descrição dos dados. O projeto deve apresentar interpretações capazes de apoiar decisões, identificar oportunidades, apontar riscos ou sugerir melhorias.

Um bom insight deve ser:
- Claro e justificável
- Conectado ao problema analisado
- Resultado da combinação entre análise estatística, visualização de dados, modelagem e interpretação dos resultados
- Capaz de sugerir ações e definir indicadores de desempenho

### Exemplos de Insights Acionáveis com Proposta de Valor

#### Exemplo 1 — Hotel
> Percebemos que reservas feitas com menos de 7 dias de antecedência apresentam taxa de cancelamento de 38%, enquanto reservas feitas com mais de 30 dias de antecedência apresentam taxa de cancelamento de 17%. Isso sugere que reservas de última hora são mais instáveis e aumentam o risco de ocupação não realizada. Por isso, recomendamos criar uma campanha de incentivo à reserva antecipada, oferecendo benefício progressivo para clientes que reservarem com pelo menos 30 dias de antecedência. A decisão foi sustentada pela taxa de cancelamento por antecedência da reserva e pelo ticket médio por grupo de clientes. Após 3 meses, o sucesso da ação pode ser avaliado pela redução da taxa de cancelamento e acompanhado pela variação na taxa de ocupação e no ticket médio. A ação será considerada bem-sucedida se a taxa de cancelamento cair pelo menos 10% no grupo impactado, sem redução relevante no ticket médio.

#### Exemplo 2 — Varejo/e-commerce
> Percebemos que clientes que abandonam o carrinho após visualizar o frete representam uma parcela relevante das perdas de conversão. Isso sugere que o custo ou a percepção de custo da entrega está atuando como barreira na etapa final da compra. Por isso, recomendamos testar uma política de frete subsidiado para compras acima de um valor mínimo, priorizando categorias com maior margem. A decisão foi sustentada pela taxa de abandono de carrinho na etapa de frete, pelo valor médio do pedido e pela margem estimada por categoria. Após 60 dias, o sucesso da ação pode ser avaliado pelo aumento da taxa de conversão e acompanhado pela margem líquida por pedido. A ação será considerada bem-sucedida se houver aumento de conversão sem deterioração da margem total da operação.

#### Exemplo 3 — Educação
> Percebemos que alunos com frequência inferior a 75% têm desempenho médio significativamente* menor nas avaliações finais em comparação aos alunos com frequência regular. Isso sugere que a baixa presença é um indicador antecipado de risco acadêmico e pode ser usada para intervenção antes do fechamento do período letivo. Por isso, recomendamos criar um acompanhamento preventivo para alunos com queda de frequência ao longo do bimestre, com contato ativo, reforço direcionado e acompanhamento pedagógico. A decisão foi sustentada pela comparação entre frequência, nota final e taxa de aprovação. Após um bimestre, o sucesso da ação pode ser avaliado pela recuperação da frequência e acompanhado pela evolução das notas e da taxa de aprovação. Consideraremos a ação bem-sucedida se os alunos acompanhados apresentarem aumento de frequência e melhora média de desempenho em relação ao período anterior ou a um grupo semelhante não acompanhado.

*Cuidado com afirmações como esta; devem ser sustentadas por teste estatístico.*

### Formato Geral de um Bom Insight

Um bom insight tem um formato semelhante a:

> Percebemos que **[padrão nos dados]**. Isso sugere que **[interpretação do problema ou oportunidade]**. Por isso, recomendamos **[ação prática]**. A decisão foi sustentada por **[métrica/evidência usada na análise]**. Após **[período]**, o sucesso da ação pode ser avaliado por **[métrica principal]** e acompanhado por **[métrica auxiliar]**. A ação será considerada bem-sucedida se **[critério objetivo de sucesso]**.

---

## Conteúdo Técnico

O documento do projeto deve apresentar, pelo menos, as seguintes seções:

### 1. Aplicação

Detalhamento da proposta do trabalho, incluindo:
- O problema escolhido
- A justificativa da escolha
- Os objetivos a serem alcançados
- A relação da análise com uma possível tomada de decisão

### 2. Base de Dados

Descrição da origem dos dados, contexto da base, quantidade de registros, variáveis existentes e principais características.

Também devem ser descritas as técnicas de pré-processamento utilizadas, como:
- Limpeza dos dados
- Tratamento de valores ausentes
- Remoção ou tratamento de dados inconsistentes
- Integração de dados, se houver
- Transformação de variáveis
- Redução ou seleção de atributos, se necessário

### 3. Estatística Descritiva e Inferência

Uso de estatísticas, tabelas, gráficos e visualizações para compreender melhor os dados.

Esta seção deve apresentar análises como:
- Distribuição das variáveis
- Medidas de tendência central
- Dispersão
- Correlações
- Comparações entre grupos
- Demais informações relevantes para o problema estudado

Quando adequado, a equipe deve utilizar testes de hipótese para apoiar afirmações feitas a partir dos dados.

### 4. Métodos Avaliados

Descrição dos métodos utilizados no projeto, podendo incluir técnicas de:
- Classificação
- Regressão
- Agrupamento
- Regras de associação
- Análise de séries temporais
- Redução de dimensionalidade
- Outros métodos relacionados à Ciência de Dados

A equipe deve justificar a escolha dos métodos, relacionando-os ao objetivo do projeto.

### 5. Métricas de Avaliação

Descrição das métricas utilizadas para avaliar os métodos aplicados.

Exemplos de métricas incluem:
- Acurácia
- Precisão
- Revocação
- F-measure
- AUC
- Erro médio absoluto
- Erro quadrático médio
- R²
- Matriz de confusão
- Outras métricas adequadas ao problema

### 6. Métodos de Avaliação

Descrição da estratégia utilizada para avaliação dos modelos, como:
- Divisão treino/teste
- k-fold cross-validation
- Leave-one-out
- Bootstrap
- Validação temporal, quando aplicável

A equipe deve explicar por que a estratégia escolhida é adequada para o problema.

### 7. Resultados e Discussão

Apresentação dos principais resultados obtidos.

Esta seção deve demonstrar:
- Como os resultados justificam a proposta da equipe
- Se a solução é válida, funcional e eficiente
- As limitações da análise
- Possíveis problemas encontrados
- Interpretações importantes

Sempre que possível, os resultados devem ser conectados à tomada de decisão proposta no projeto.

Além de apresentar os resultados técnicos, a equipe deverá explicitar qual tomada de decisão está sendo recomendada a partir da análise realizada. Essa decisão deve estar associada a uma métrica ou evidência quantitativa que demonstre seu impacto. Por exemplo, a equipe pode recomendar uma ação porque os dados indicam que ela reduz em X% a taxa de cancelamento de reservas, aumenta em Y% a previsão de vendas, melhora em Z pontos a acurácia do modelo ou reduz determinado risco identificado na base.

### 8. Conclusão

Resumo do que foi realizado no projeto, principais descobertas, limitações e possibilidades de trabalhos futuros.

### 9. Bibliografia

Apresentação das obras, artigos, bases de dados, documentações e demais referências consultadas ou citadas no trabalho.

---

## Estilo do Documento

O documento deve seguir o modelo de confecção de artigos para conferências segundo a Sociedade Brasileira de Computação (SBC).

### Modelos Disponíveis

- [Modelos SBC (Doc e LaTeX)](https://www.sbc.org.br/documentos-da-sbc/summary/169-templates-para-artigos-e-capitulos-de-livros/878-modelosparapublicacaodeartigos)
- [Modelo SBC no Overleaf (LaTeX)](https://pt.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr)

### Limite de Páginas

O documento final deve ter, **no máximo, 12 páginas**.

---

## Apresentação

A apresentação do trabalho terá tempo total de até **20 minutos**, organizados da seguinte maneira:

- **5 minutos** para o **Pitch**: apresentação em formato mais comercial, voltada para cliente, gestor ou banca avaliadora
- **15 minutos** para a **Apresentação Técnica**: explicação mais aprofundada da base, metodologia, modelos, métricas, resultados e limitações

### Conteúdo da Apresentação

A equipe deverá apresentar o trabalho mostrando de forma clara:
- O problema escolhido
- A base utilizada
- A metodologia aplicada
- Os principais resultados encontrados
- A decisão recomendada a partir da análise dos dados

A linguagem deve ser compatível com cada tipo de apresentação.

### Linha Lógica

**Pitch:**
Problema identificado → Oportunidade → Principais evidências → Decisão proposta → Impacto esperado

**Apresentação Técnica:**
Base utilizada → Preparação dos dados → Métodos/modelos aplicados → Métricas utilizadas → Resultados obtidos → Limitações → Justificativa da decisão final

### Justificativa da Decisão

A equipe deve demonstrar que a decisão sugerida não surgiu apenas de uma opinião, mas de evidências encontradas nos dados ou referências consolidadas.

Durante o **pitch**, a equipe deverá apresentar sua solução como se estivesse defendendo a proposta para um gestor, empresa, cliente ou banca avaliadora, destacando o valor prático dos resultados obtidos. 

Na **apresentação técnica**, a equipe deverá aprofundar os aspectos metodológicos, explicando as escolhas realizadas e sustentando tecnicamente os resultados apresentados.

### Participação dos Membros

Não é obrigatório que todos os integrantes falem durante a apresentação, mas todos devem participar efetivamente da construção do trabalho. 

A equipe poderá dividir as falas da forma que considerar mais adequada, incluindo concentrar em um membro, desde que:
- Todos os integrantes estejam presentes
- Todos estejam aptos a responder perguntas sobre a base, a metodologia, os resultados e a decisão proposta

---

## Submissão

A entrega deverá ser realizada em duas partes:

### Parte 1 — Definição da Base e Proposta Inicial

**Valor:** 2,0 pontos

Nesta etapa, a equipe deverá entregar um arquivo **PDF de até 2 páginas** com a descrição inicial da base escolhida e da proposta de análise do projeto.

A entrega deve conter:
- Nome ou tema da base (ou bases)
- Origem dos dados (link)
- Descrição geral da base
- Justificativa da escolha
- Problema que será analisado
- Tipo de tomada de decisão que se pretende apoiar
- Hipóteses iniciais levantadas pela equipe
- Possíveis métodos que poderão ser utilizados (não representa compromisso para a entrega, apenas uma avaliação inicial)

**Prazo:** Uma semana após a proposta do projeto pelo docente da disciplina (via atividade da turma virtual)

### Parte 2 — Entrega Final

**Valor:** 8,0 pontos

A entrega final será composta por um arquivo **.zip ou .rar**, entregue via atividade da turma virtual, conforme cronograma da disciplina, contendo:

- Documento final em PDF
- Código utilizado nos experimentos
- Apresentação
- Arquivos adicionais, caso existam

As apresentações ocorrerão nas datas propostas pelo cronograma da disciplina, em ordem a ser definida.

**Distribuição dos 8,0 pontos:**
- **5,0 pontos** para a apresentação (pitch + técnica)
- **3,0 pontos** para o documento final

---

## Critérios de Avaliação

### Parte 1 — Definição da Base e Proposta Inicial (2,0 pontos)

Serão avaliados:
- Clareza na escolha da base
- Justificativa da escolha
- Relevância do problema e das hipóteses levantadas
- Potencial de geração de insights
- Relação inicial com tomada de decisão

### Parte 2 — Apresentação (5,0 pontos)

Serão avaliados:
- Clareza na explicação do problema
- Domínio da base de dados
- Apresentação da metodologia
- Qualidade das análises e visualizações
- Interpretação dos resultados
- Relação entre os insights, as métricas obtidas e a tomada de decisão proposta
- Clareza na justificativa da decisão recomendada, indicando qual ação deve ser tomada e qual métrica evidencia sua melhoria ou impacto
- Organização e qualidade da comunicação

### Parte 3 — Documento Final (3,0 pontos)

Serão avaliados:
- Estrutura do documento
- Descrição adequada da base
- Uso de estatística, visualização de dados, mineração de dados e/ou aprendizagem de máquina
- Descrição dos métodos e métricas
- Apresentação dos resultados
- Discussão crítica
- Conclusão
- Referências

---

## Pontuação Extra

A equipe poderá receber de **1,0 a 2,0 pontos extras** pela inclusão de recursos adicionais que enriqueçam o projeto.

### Exemplos de Recursos Extras

- Construção de dashboard interativo
- Aplicação web simples para visualização dos resultados
- Deploy de modelo
- Relatório automatizado
- Uso de técnicas avançadas de modelagem
- Integração com APIs
- Visualizações interativas
- Comparação aprofundada entre diferentes abordagens
- Integração e uso de LLMs

A pontuação extra será atribuída conforme a qualidade, relevância e utilidade do recurso desenvolvido para o contexto do projeto.

---

## Observação Final

O projeto deve demonstrar a capacidade da equipe de **transformar dados em conhecimento útil para apoiar decisões**. 

No entanto, é importante lembrar que o foco não deve estar apenas no conteúdo técnico.

A equipe deve se atentar à **comunicação em formato de pitch e técnica**, nos momentos adequados. Durante a apresentação, vocês precisam:

1. Apresentar bem o problema
2. Mostrar como chegaram até ele por meio da análise dos dados
3. Defender a melhor solução encontrada

**Em outras palavras: vendam o seu peixe.**

### Exemplo Prático

Se o problema identificado for uma queda no número de reservas em períodos de baixa temporada, a equipe deve:

- Explicar como chegou a essa conclusão
- Quais gargalos foram encontrados na base
- Quais evidências sustentam essa análise
- Propor soluções práticas, como:
  - Promoções
  - Programas de fidelização
  - Cashback
  - Campanhas direcionadas
  - Outras estratégias capazes de contornar o problema

### Resumo

A apresentação deve deixar claro **não apenas quais técnicas foram utilizadas**, mas principalmente **como os resultados encontrados podem gerar valor e orientar uma tomada de decisão fundamentada em dados**.
# Relatório de Impacto: Análise de Satisfação de Passageiros

## 1. Resumo Executivo
Este relatório apresenta os resultados da implementação da esteira analítica para prever a satisfação de passageiros do aeroporto. O pipeline de dados foi totalmente validado, comprovando que o ambiente de produção reproduz fielmente os resultados da experimentação. Com base na modelagem preditiva, o modelo **LightGBM** obteve um excelente desempenho (**81.72% de acurácia** e **AUC-ROC de 0.8957**), permitindo identificar de forma antecipada passageiros com alta probabilidade de insatisfação.

## 2. Visão Geral dos Dados e Tratamentos
O conjunto de dados inicial contou com **57.514 registros** e 145 variáveis, abordando informações demográficas, detalhes do voo e avaliações de múltiplos serviços aeroportuários.

- **Qualidade dos Dados:** Detectou-se um volume massivo de dados faltantes na origem (**3.323.783 valores nulos**). O tratamento adotado imputou valores pela mediana e moda para garantir a fluidez do algoritmo, resultando em uma base sem furos.
- **Transformação:** As 23 variáveis categóricas (como tipo de voo, motivo da viagem e nível educacional) foram estruturadas (*One-Hot Encoding*), elevando o dataset final a 252 atributos prontos para consumo pelos modelos.

## 3. Desempenho da Modelagem
A base foi dividida em 80% para treino e 20% para teste. Uma bateria robusta de testes com validação cruzada (5 folds) foi executada, comparando os principais algoritmos de mercado:

*   Regressão Logística: ~79.8%
*   Decision Tree: ~79.3%
*   Random Forest: ~80.2%
*   XGBoost: ~81.6%
*   **LightGBM: 81.7% (Vencedor)**

O modelo campeão demonstrou excelente separação entre clientes promotores e detratores, fornecendo uma base sólida para a tomada de decisões em tempo real.

### 3.1. Explicabilidade do Modelo e Principais Ofensores (SHAP)
Graças à implementação do gráfico SHAP (eliminando a "caixa-preta"), pudemos analisar visualmente o impacto direto de cada variável:
* **"O Básico Bem Feito" é Crítico:** Variáveis de Locomoção (`location_and_movement`) e Limpeza (`overall_airport_cleanliness`) são os maiores ofensores. Notas baixas nessas categorias punem a nota de satisfação de forma dramática.
* **Conforto é Acionável:** O Conforto na Sala de Embarque (`boarding_lounge_comfort`) tem comportamento linear: clientes que dão notas altas se inclinam proporcionalmente para uma satisfação geral retida.

---

## 4. Recomendações e Impacto Operacional
Para traduzir a precisão preditiva do LightGBM em ganhos diretos para o aeroporto, foram levantadas e analisadas questões fundamentais para o negócio. As estratégias derivadas são:

### 4.1. Atuação Direcionada a Gargalos Críticos
Baseado na análise SHAP, os esforços das equipes de campo devem focar estritamente na resolução de filas para locomoção e manutenção da limpeza geral, pois possuem um efeito desproporcional na satisfação. Se o modelo apontar alta probabilidade de insatisfação num dado horário, orientar o tráfego e reforçar as equipes de limpeza é a intervenção de maior ROI (Retorno sobre Investimento).

### 4.2. Estratégias de Personalização e Retenção
Com base nos padrões encontrados, perfis diferentes reagem de maneiras distintas a fricções na jornada. O aeroporto deve:
- **Segmentar fluxos:** Direcionar passageiros de "negócios" vs "lazer" para esteiras de raio-x ou áreas de espera adequadas aos seus níveis de tolerância.
- **Investir no ROI do Cliente:** Quando a predição indicar forte chance de nota baixa, o sistema de CRM pode enviar proativamente um *voucher* de café ou desconto nas lojas do aeroporto. O custo desse agrado é substancialmente menor do que o custo de reversão de imagem corporativa.

### 4.3. Captura e Qualidade da Informação
A alta dependência de "valores médios" e "modas" na imputação de mais de 3 milhões de lacunas pode gerar viés nas predições do sistema. Recomenda-se negociar melhorias na ingestão de dados primários através de tótens ou check-in web para obter informações preenchidas de forma ativa pelos clientes.

---

## 5. Próximos Passos (Melhorias Técnicas Recomendadas)
Visando a evolução madura do projeto de Machine Learning, as seguintes ações técnicas são prioridades para o próximo ciclo de desenvolvimento:

1. **Explicabilidade do Modelo (SHAP Values) [IMPLEMENTADO]:** Modelos de *Gradient Boosting* são "caixas-pretas". Para resolver isso, implementamos gráficos SHAP na nossa esteira. Agora a equipe de operações sabe não apenas *quem* estará insatisfeito, mas *o motivo específico* (ex: se foi o atraso, a fila ou a limpeza do banheiro), facilitando a ação corretiva.
2. **Imputação Inteligente de Dados Faltantes:** Substituir o preenchimento global por técnicas agrupadas (ex: inferir idade baseado no grupo familiar ou de voo) ou usando algorítimos como `KNNImputer`, reduzindo o ruído injetado no modelo.
3. **Escalonamento e Otimização:** Corrigir os limites iterativos do otimizador (*solver lbfgs*) na Regressão Logística adicionando `StandardScaler` ao pipeline, garantindo convergência total para servir de *baseline* confiável.

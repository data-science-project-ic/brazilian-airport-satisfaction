# Backlog de Implementação LaTeX — Artigo SBC

Este backlog define as tarefas necessárias para transformar o template SBC no artigo completo conforme o plano em `TEX_PLAN.md`.

## Fase 1: Configuração Inicial e Identidade (Peso: Baixo)
- [x] **Tarefa 1.1: Atualizar Cabeçalho**
    - Alterar título para: *"Predição de Satisfação de Passageiros em Aeroportos Brasileiros: Uma Abordagem com LightGBM e SHAP Values"*
    - Configurar autores: 5 autores, afiliação UFAL (Instituto de Computação), e-mails em Courier.
- [x] **Tarefa 1.2: Redigir Abstract e Resumo**
    - Abstract (Inglês): Máx 10 linhas. Focar no problema, AUC-ROC (0.8957) e acurácia (81.72%).
    - Resumo (Português): Tradução fiel do Abstract.

## Fase 2: Estrutura de Seções e Conteúdo Introdutório (Peso: Médio)
- [x] **Tarefa 2.1: Implementar Seção 1 (Introdução)**
    - Contextualizar experiência do passageiro e lacuna de dados brasileiros.
    - Listar as 3 contribuições principais.
    - Adicionar parágrafo de estrutura do artigo.
- [x] **Tarefa 2.2: Implementar Seção 2 (Trabalhos Relacionados)**
    - Agrupar literatura em: satisfação na aviação, Gradient Boosting e SHAP.
    - Criar Tabela Comparativa de Literatura (Trabalho | Dataset | Método | Métrica).

## Fase 3: Dados, Metodologia e "Arena de Algoritmos" (Peso: Alto)
- [x] **Tarefa 3.1: Implementar Seção 3 (Base de Dados e Pré-processamento)**
    - Descrever origem (SNAC), dimensões e tratamento de 3.3M nulos.
    - Detalhar One-Hot Encoding e limpeza de atributos.
    - **Visual:** Inserir Figura 1 (Fluxograma do Pipeline) e Tabela 1 (Estatísticas Descritivas).
- [x] **Tarefa 3.2: Implementar Seção 4 (Metodologia)**
    - Descrever os 5 modelos avaliados (LogReg, DT, RF, XGBoost, LightGBM).
    - Detalhar validação Hold-out 80/20 e K-Fold (K=5) estratificado.
    - Explicar métricas (AUC-ROC como principal).
    - **Visual:** Inserir Tabela 2 (Comparação de Performance dos 5 modelos).

## Fase 4: Resultados e Discussão (Peso: Alto)
- [x] **Tarefa 4.1: Implementar Seção 5 (Experimentos e Resultados)**
    - Analisar correlações e validação de hipóteses (H1, H2, H3).
    - Detalhar performance do LightGBM.
    - Inserir análise de explicabilidade SHAP.
    - **Visuais:**
        - Figura 2: Distribuição `liked`.
        - Figura 3: Heatmap de correlação (Top features).
        - Figura 4: SHAP Summary Plot (Beeswarm).
        - Figura 5: Curva ROC do LightGBM.
        - Tabela 3: Matriz de Confusão.
- [x] **Tarefa 4.2: Implementar Seção 6 (Discussão)**
    - Interpretar resultados: "Básico vs. Premium".
    - Discutir implicações para gestores e limitações do estudo.

## Fase 5: Finalização e Referências (Peso: Baixo)
- [x] **Tarefa 5.1: Implementar Seção 7 (Conclusão)**
    - Sintetizar resultados e propor 3-4 trabalhos futuros (API, Clima, etc).
- [x] **Tarefa 5.2: Gerenciar Bibliografia**
    - Atualizar arquivo `.bib` com citações de Lundberg & Lee (SHAP), documentação SNAC e referências da Seção 2.
- [x] **Tarefa 5.3: Ajuste de Layout (Checklist Final)**
    - Verificar se o artigo possui entre 10 e 12 páginas.
    - Se curto: Expandir Seção 3 (mais stats) ou 5.3 (SHAP Waterfall).
    - Se longo: Condensar Seção 2 ou 6.

---
**Instruções para o Agente:**
1. Use `pdflatex` para compilar se necessário validar o layout.
2. Certifique-se de que todas as referências cruzadas (`\ref`, `\cite`) estão funcionando.
3. As figuras devem ser referenciadas no texto antes ou logo após sua aparição.

# Projeto Satisfação de Voos

Este repositório contém os dados e o código para o projeto "Real Airline Passenger Satisfaction".

## Estrutura do Repositório
A estrutura foi baseada no modelo proposto para a disciplina:

* `data/`: Armazena os dados originais (em `raw/`) e os dados processados (em `processed/`).
* `notebooks/`: Ambiente de experimentação contendo as análises.
* `src/`: Scripts Python auxiliares e reutilizáveis (como as funções em `utils.py`).
* `outputs/`: Gráficos gerados (em `figures/`) e modelos (em `models/`).

## Como executar

1. Crie e ative um ambiente virtual:
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Coloque a base de dados original na pasta `data/raw/` (exemplo: arquivo `.csv`).
4. Execute os notebooks na pasta `notebooks/` na seguinte ordem:
   - `01_exploracao.ipynb`
   - `02_pre_process.ipynb`
   - `03_modelagem.ipynb`
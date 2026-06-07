import pandas as pd
import numpy as np
import os

class DataPreprocessor:
    def __init__(self, data_path, output_path='data/processed/df_model.csv'):
        """
        Inicializa o pré-processador.
        """
        self.data_path = data_path
        self.output_path = output_path
        self.df = None
        
        # Garante que a pasta de saída existe
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        
    def load_data(self):
        """Carrega a base de dados."""
        print("=" * 40)
        print("Iniciando Fase 2: Pré-processamento e Limpeza")
        self.df = pd.read_csv(self.data_path)
        print(f"Shape inicial: {self.df.shape}")

    def treat_structural_nulls(self):
        """
        Tratamento condicional de nulos baseado em _is_applicable.
        """
        if self.df is None:
            raise ValueError("O DataFrame não está carregado.")
            
        nulos_iniciais = self.df.isnull().sum().sum()
        print(f"Nulos encontrados na entrada: {nulos_iniciais}")

        applicability_cols = [col for col in self.df.columns if str(col).endswith('_is_applicable')]
        
        for app_col in applicability_cols:
            eval_col = app_col.replace('_is_applicable', '')
            if eval_col in self.df.columns:
                # Se is_applicable == 0, preenchemos com -1
                mask_not_applicable = (self.df[app_col] == 0) & (self.df[eval_col].isnull())
                self.df.loc[mask_not_applicable, eval_col] = -1
                
        # Tratamento dos NaNs remanescentes (aplicabilidade == 1 ou sem flag)
        for col in self.df.columns:
            if self.df[col].isnull().any():
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    self.df[col] = self.df[col].fillna(self.df[col].median())
                else:
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        nulos_finais = self.df.isnull().sum().sum()
        print(f"Nulos após o tratamento estrutural: {nulos_finais}")

    def encode_categorical(self):
        """
        Aplica One-Hot Encoding e remove caracteres espaciais.
        """
        if self.df is None:
            return

        cat_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        print(f"Aplicando One-Hot Encoding em {len(cat_cols)} colunas categóricas.")
        
        self.df = pd.get_dummies(self.df, columns=cat_cols, drop_first=True)
        
        # Converter bool para int
        for c in self.df.columns:
            if self.df[c].dtype == 'bool':
                self.df[c] = self.df[c].astype(int)
        
        # Limpar nomes das colunas (Exigência do LightGBM)
        import re
        self.df = self.df.rename(columns=lambda x: re.sub('[^A-Za-z0-9_]+', '', x))

        print(f"Shape após o Encoding: {self.df.shape}")

    def verify_and_save(self):
        """
        Garante as validações finais e exporta.
        """
        if self.df is None:
            return

        assert self.df.isnull().sum().sum() == 0, "Erro: Valores nulos remanescentes!"
        assert self.df.select_dtypes(exclude=[np.number]).shape[1] == 0, "Erro: Colunas não numéricas remanescentes!"
        
        self.df.to_csv(self.output_path, index=False)
        print(f"Base processada, validada e exportada para: {self.output_path}\n")

    def run_all(self):
        self.load_data()
        self.treat_structural_nulls()
        self.encode_categorical()
        self.verify_and_save()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class DataExplorer:
    def __init__(self, data_path, output_dir='outputs/figures'):
        """
        Inicializa o explorador de dados.
        """
        self.data_path = data_path
        self.output_dir = output_dir
        self.df = None
        
        # Garante que a pasta de saída existe
        os.makedirs(self.output_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")
        
    def load_and_inspect(self):
        """
        Carrega a base original e mostra informações descritivas na tela.
        """
        print("=" * 40)
        print("Iniciando Fase 1: Exploração de Dados (EDA)")
        self.df = pd.read_csv(self.data_path)
        print(f"Base carregada com sucesso: {self.df.shape[0]} linhas e {self.df.shape[1]} colunas.")
        print("=" * 40)
        return self.df
        
    def plot_target_distribution(self):
        """
        Plota a distribuição da variável alvo (liked).
        """
        if self.df is None:
            raise ValueError("O DataFrame não está carregado. Rode load_and_inspect() primeiro.")
            
        plt.figure(figsize=(8, 6))
        ax = sns.countplot(data=self.df, x='liked', hue='liked', palette={0: '#e74c3c', 1: '#2ecc71'}, legend=False)
        plt.title('Distribuição da Variável Alvo (Liked)')
        plt.xlabel('Satisfação (0 = Insatisfeito, 1 = Satisfeito)')
        plt.ylabel('Frequência Absoluta')

        total_samples = len(self.df)
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                perc = f'{height / total_samples:.1%}'
                ax.annotate(perc, (p.get_x() + p.get_width() / 2., height),
                            ha='center', va='bottom', fontsize=12, fontweight='bold')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'distribuicao_alvo.png'), dpi=300)
        plt.close()
        print(f"Gráfico salvo: {os.path.join(self.output_dir, 'distribuicao_alvo.png')}")

    def plot_bivariate_analysis(self):
        """
        Plota cruzamentos para explorar hipóteses de negócio.
        """
        if self.df is None:
            return

        # Exemplo 1: Atraso vs Satisfação
        if 'arrival_lead_time' in self.df.columns:
            plt.figure(figsize=(8, 5))
            sns.boxplot(data=self.df, x='liked', y='arrival_lead_time', hue='liked', palette={0: '#e74c3c', 1: '#2ecc71'}, legend=False)
            plt.title('Atraso/Tempo (Arrival Lead Time) vs Satisfação')
            plt.xlabel('Liked')
            plt.ylim(0, self.df['arrival_lead_time'].quantile(0.95)) 
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'atrasos_vs_satisfacao.png'), dpi=300)
            plt.close()
            print(f"Gráfico salvo: {os.path.join(self.output_dir, 'atrasos_vs_satisfacao.png')}")

        # Exemplo 2: Tipo de Voo
        if 'flight_type' in self.df.columns:
            plt.figure(figsize=(8, 5))
            sns.barplot(data=self.df, x='flight_type', y='liked', hue='flight_type', errorbar=None, palette='viridis', legend=False)
            plt.title('Taxa de Satisfação por Tipo de Voo')
            plt.ylabel('Taxa de Aprovação')
            plt.ylim(0, 1)
            plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'satisfacao_por_tipo_voo.png'), dpi=300)
            plt.close()
            print(f"Gráfico salvo: {os.path.join(self.output_dir, 'satisfacao_por_tipo_voo.png')}")

    def plot_correlation_heatmap(self):
        """
        Plota a matriz de correlação das numéricas com o Liked.
        """
        if self.df is None:
            return

        num_cols = [c for c in self.df.columns if pd.api.types.is_numeric_dtype(self.df[c]) and not str(c).endswith('_is_applicable') and c != 'liked']
        corr_with_liked = self.df[num_cols].corrwith(self.df['liked']).abs().sort_values(ascending=False).head(15)
        top_cols = corr_with_liked.index.tolist()

        plt.figure(figsize=(12, 10))
        sns.heatmap(self.df[top_cols + ['liked']].corr(), annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
        plt.title('Matriz de Correlação (Top 15 vs Liked)')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'heatmap_correlacao.png'), dpi=300)
        plt.close()
        print(f"Gráfico salvo: {os.path.join(self.output_dir, 'heatmap_correlacao.png')}")

    def run_all(self):
        self.load_and_inspect()
        self.plot_target_distribution()
        self.plot_bivariate_analysis()
        self.plot_correlation_heatmap()
        print("Exploração de dados finalizada com sucesso.\n")

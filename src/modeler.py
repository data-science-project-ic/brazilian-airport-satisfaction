import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb
import shap
import joblib
import os

class ModelTrainer:
    def __init__(self, data_path='data/processed/df_model.csv', models_dir='outputs/models', figures_dir='outputs/figures'):
        """
        Inicializa o treinador de modelos.
        """
        self.data_path = data_path
        self.models_dir = models_dir
        self.figures_dir = figures_dir
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.best_model = None
        self.best_model_name = ""
        
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.figures_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")

    def load_and_split(self):
        """Carrega os dados processados e separa em Treino e Teste."""
        print("=" * 40)
        print("Iniciando Fase 3: Modelagem e Machine Learning")
        self.df = pd.read_csv(self.data_path)
        
        X = self.df.drop(columns=['liked'])
        y = self.df['liked']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        print(f"Treino: {self.X_train.shape[0]} amostras | Teste: {self.X_test.shape[0]} amostras.")

    def run_benchmarking(self):
        """Executa a Arena de Algoritmos usando Validação Cruzada."""
        print("\nIniciando bateria de testes (Cross-Validation K=5)...")
        models = {
            'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
            'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=8),
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
            'XGBoost': xgb.XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42, n_jobs=-1),
            'LightGBM': lgb.LGBMClassifier(n_estimators=100, learning_rate=0.1, random_state=42, n_jobs=-1, verbose=-1)
        }
        
        results = []
        names = []
        
        for name, model in models.items():
            cv_scores = cross_val_score(model, self.X_train, self.y_train, cv=5, scoring='accuracy', n_jobs=1)
            results.append(cv_scores)
            names.append(name)
            print(f"[{name}] Acurácia Média CV: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
            
        # Plot
        plt.figure(figsize=(10, 6))
        plt.boxplot(results, labels=names, patch_artist=True, boxprops=dict(facecolor="lightblue"))
        plt.title('Comparativo de Desempenho dos Algoritmos (Cross-Validation)')
        plt.ylabel('Acurácia')
        plt.xlabel('Algoritmos')
        plt.tight_layout()
        plt.savefig(os.path.join(self.figures_dir, 'model_benchmarking.png'), dpi=300)
        plt.close()
        
        # Encontrar vencedor
        mean_scores = [scores.mean() for scores in results]
        best_idx = np.argmax(mean_scores)
        self.best_model_name = names[best_idx]
        self.best_model = models[self.best_model_name]
        
        print(f"\n[CAMPEAO] MODELO: {self.best_model_name} com acurácia média de {mean_scores[best_idx]:.4f}!")

    def train_and_evaluate_best(self):
        """Treina o melhor modelo e emite os relatórios finais na base de Teste."""
        print(f"\nTreinando o {self.best_model_name} no dataset completo de treino...")
        self.best_model.fit(self.X_train, self.y_train)
        
        y_pred = self.best_model.predict(self.X_test)
        
        if hasattr(self.best_model, "predict_proba"):
            y_prob = self.best_model.predict_proba(self.X_test)[:, 1]
            roc_auc = roc_auc_score(self.y_test, y_prob)
        else:
            roc_auc = "N/A"
            
        print(f"\n--- Classification Report ({self.best_model_name}) ---")
        print(classification_report(self.y_test, y_pred))
        print(f"AUC-ROC Score: {roc_auc if isinstance(roc_auc, str) else f'{roc_auc:.4f}'}")
        
        cm = confusion_matrix(self.y_test, y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Insatisfeito', 'Satisfeito'], 
                    yticklabels=['Insatisfeito', 'Satisfeito'])
        plt.title(f'Matriz de Confusão - {self.best_model_name}')
        plt.xlabel('Previsto')
        plt.ylabel('Realidade')
        plt.tight_layout()
        plt.savefig(os.path.join(self.figures_dir, 'matriz_confusao.png'), dpi=300)
        plt.close()

    def explain_and_export(self):
        """Plota Feature Importance, gera gráficos SHAP e salva o modelo no Joblib."""
        if hasattr(self.best_model, "feature_importances_"):
            importances = pd.Series(self.best_model.feature_importances_, index=self.X_train.columns)
            top_features = importances.sort_values(ascending=False).head(15)

            plt.figure(figsize=(10, 6))
            top_features.plot(kind='barh', color='#2ecc71')
            plt.title(f'Feature Importance - {self.best_model_name}')
            plt.gca().invert_yaxis()
            plt.xlabel('Peso')
            plt.tight_layout()
            plt.savefig(os.path.join(self.figures_dir, 'feature_importance.png'), dpi=300)
            plt.close()

            # SHAP Values
            print("\nGerando gráfico SHAP para explicabilidade...")
            try:
                explainer = shap.TreeExplainer(self.best_model)
                shap_values = explainer.shap_values(self.X_test)
                
                # Para classificadores binários (como LightGBM), o shap_values pode vir como lista
                if isinstance(shap_values, list) and len(shap_values) == 2:
                    shap_values_to_plot = shap_values[1]
                else:
                    shap_values_to_plot = shap_values
                    
                plt.figure()
                shap.summary_plot(shap_values_to_plot, self.X_test, show=False)
                plt.tight_layout()
                plt.savefig(os.path.join(self.figures_dir, 'shap_summary.png'), dpi=300, bbox_inches='tight')
                plt.close()
                print(f"Gráfico SHAP salvo em: {os.path.join(self.figures_dir, 'shap_summary.png')}")
            except Exception as e:
                print(f"Erro ao gerar gráficos SHAP: {e}")
        
        filename = self.best_model_name.lower().replace(' ', '_')
        model_path = os.path.join(self.models_dir, f'melhor_modelo_{filename}.pkl')
        joblib.dump(self.best_model, model_path)
        print(f"\nModelo salvo em: {model_path}")
        print("=" * 40)

    def run_all(self):
        self.load_and_split()
        self.run_benchmarking()
        self.train_and_evaluate_best()
        self.explain_and_export()

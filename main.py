from src.explorer import DataExplorer
from src.preprocessor import DataPreprocessor
from src.modeler import ModelTrainer

def main():
    print("Iniciando Pipeline de Satisfação de Passageiros do Aeroporto...\n")
    
    raw_data_path = 'data/raw/passenger_survey_balanced.csv'
    processed_data_path = 'data/processed/df_model.csv'
    
    # 1. Fase de Exploração (EDA)
    explorer = DataExplorer(data_path=raw_data_path)
    explorer.run_all()
    
    # 2. Fase de Pré-Processamento
    preprocessor = DataPreprocessor(data_path=raw_data_path, output_path=processed_data_path)
    preprocessor.run_all()
    
    # 3. Fase de Modelagem e IA
    modeler = ModelTrainer(data_path=processed_data_path)
    modeler.run_all()
    
    print("\nPipeline finalizado com sucesso!")

if __name__ == '__main__':
    main()

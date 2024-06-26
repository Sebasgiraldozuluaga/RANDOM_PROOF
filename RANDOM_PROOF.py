import pandas as pd
import numpy as np
from datetime import datetime
import os

class RandomDBGenerator:
    def __init__(self):
        self.db = None
        self.csv_file_path = 'random_db.csv'

    def generate_db(self):
        # Obtener la hora actual como string
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Crear un DataFrame con datos aleatorios
        data = {
            'Columna1': np.random.rand(10),  # 10 datos aleatorios
            'Columna2': np.random.rand(10),
            'Columna3': np.random.rand(10)
        }
        new_data = pd.DataFrame(data)
        
        # Usar la hora actual como índice
        new_data.index = [current_time] * len(new_data)
        
        # Si el archivo ya existe, leer y concatenar
        if os.path.exists(self.csv_file_path):
            existing_data = pd.read_csv(self.csv_file_path, index_col=0)
            self.db = pd.concat([existing_data, new_data])
        else:
            self.db = new_data
        
        # Guardar en CSV
        self.db.to_csv(self.csv_file_path)


if __name__ == '__main__': 
    generator = RandomDBGenerator()

    # Generar el DataFrame y concatenar si es necesario
    generator.generate_db()

    # Acceder al DataFrame actualizado
    df = generator.db
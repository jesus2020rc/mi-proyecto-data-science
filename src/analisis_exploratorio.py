import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def realizar_eda(ruta_csv):
    """
    Realiza una exploracion inicial del dataset:
    dimensiones, tipos de datos, valores nulos y estadisticas descriptivas.
    """
    print(f"=== Cargando datos desde: {ruta_csv} ===")
    try:
        df = pd.read_csv(ruta_csv)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo en {ruta_csv}.")
        print("Generando un dataset de ejemplo para la demostracion...")
        np.random.seed(42)
        df = pd.DataFrame({
            'edad': np.random.randint(20, 65, size=100),
            'ingresos': np.random.normal(3000, 800, size=100).round(2),
            'satisfaccion': np.random.choice(['Baja', 'Media', 'Alta'], size=100)
        })

    # 1. Dimensiones y tipos
    print("\n--- Vista previa de los datos (head) ---")
    print(df.head())

    print(f"\n--- Dimensiones (filas, columnas): {df.shape} ---")
    print("\n--- Tipos de datos e informacion general ---")
    print(df.info())

    # 2. Deteccion de valores nulos
    print("\n--- Conteo de valores nulos por columna ---")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0] if nulos.any() else "No se detectaron valores nulos.")

    # 3. Resumen estadistico de variables numericas
    print("\n--- Estadisticas descriptivas ---")
    print(df.describe().round(2))

    return df

if __name__ == '__main__':
    ruta_datos = 'data/raw/dataset.csv'
    dataset = realizar_eda(ruta_datos)
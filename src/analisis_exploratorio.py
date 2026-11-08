import os
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

def generar_graficos(df, carpeta_salida='reports/figures'):
    """
    Crea y guarda visualizaciones estadisticas en la carpeta de reportes.
    """
    os.makedirs(carpeta_salida, exist_ok=True)
    sns.set_theme(style='whitegrid')

    # 1. Distribucion de edades
    plt.figure(figsize=(8, 5))
    sns.histplot(df['edad'], kde=True, color='skyblue', bins=10)
    plt.title('Distribucion de Edades', fontsize=14)
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    ruta_hist = os.path.join(carpeta_salida, 'distribucion_edad.png')
    plt.savefig(ruta_hist, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\n[Grafico guardado] -> {ruta_hist}")

    # 2. Relacion Ingresos vs Edad segmentado por Satisfaccion
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x='edad',
        y='ingresos',
        hue='satisfaccion',
        palette='viridis',
        s=80
    )
    plt.title('Relacion entre Ingresos y Edad segun Nivel de Satisfaccion', fontsize=14)
    plt.xlabel('Edad')
    plt.ylabel('Ingresos ($)')
    ruta_scatter = os.path.join(carpeta_salida, 'ingresos_vs_edad.png')
    plt.savefig(ruta_scatter, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[Grafico guardado] -> {ruta_scatter}")

if __name__ == '__main__':
    ruta_datos = 'data/raw/dataset.csv'
    dataset = realizar_eda(ruta_datos)
    generar_graficos(dataset)
    

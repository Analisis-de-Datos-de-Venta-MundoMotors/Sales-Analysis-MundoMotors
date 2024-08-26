import subprocess
import sys
from src.database_preprocessing.preprocessing import clean_data
from src.analysis.analysis import calculate_total_revenue, get_top_products
from src.visualization.visualization import plot_revenue_trends
from src.utils.utils import save_to_csv


def main():

    # Paso 1: Cargar y limpiar los datos
    raw_data_path = 'data/raw/CarSales.csv'
    cleaned_data_path = 'data/processed/CleanedCarSales.csv'
    df = clean_data(raw_data_path)

    # Guardar datos limpiados
    save_to_csv(df, cleaned_data_path)

    # Paso 2: Realizar análisis
    total_revenue = calculate_total_revenue(df)
    print(f"Total Revenue: {total_revenue}")

    top_products = get_top_products(df)
    print("Top Products:")
    print(top_products)

    # Paso 3: Visualizar tendencias
    plot_revenue_trends(df)

if __name__ == "__main__":
    main()

def calculate_total_revenue(df):
    return df['Ingresos Totales'].sum()

def get_top_products(df, top_n=10):
    return df.groupby('Producto')['Cantidad Vendida'].sum().nlargest(top_n)
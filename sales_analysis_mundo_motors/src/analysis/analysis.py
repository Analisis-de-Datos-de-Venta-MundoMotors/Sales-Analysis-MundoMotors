def calculate_total_revenue(df):
    return df['Price ($)'].sum()

def get_top_products(df, top_n=10):
    return df.groupby('Model')['Price ($)'].sum().nlargest(top_n)

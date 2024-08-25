import matplotlib.pyplot as plt
import seaborn as sns

def plot_revenue_trends(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Date', y='Price ($)')
    plt.title('Tendencia de Ingresos')
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos Totales')
    plt.show()

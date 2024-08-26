from setuptools import setup, find_packages

setup(
    name='sales_analysis_mundo_motors',
    version='0.1.0', 
    description='Proyecto de Analisis de ventas de la empresa MundoMotors', 
    author='MundoMotors', 
    author_email='contacto@mundomotors.com',
    url='https://github.com/Analisis-de-Datos-de-Venta-MundoMotors',
    install_requires=[
        'pandas>=2.2.2',
        'numpy>=2.1.0',
        'matplotlib>=3.7.2',
        'seaborn>=0.12.2',
        'pyodbc>=4.0.35'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

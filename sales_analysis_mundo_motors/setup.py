from setuptools import setup, find_packages

setup(
    name='sales_analysis_project',  # Nombre del paquete
    version='0.1.0',  # Versión del paquete
    description='A Python project for sales data analysis',  # Breve descripción del proyecto
    author='Tu Nombre',  # Tu nombre o el nombre de la organización
    author_email='tuemail@example.com',  # Tu correo electrónico
    url='https://github.com/tu_usuario/sales_analysis_project',  # URL del repositorio del proyecto (si aplica)
    packages=find_packages(where='src'),  # Encuentra todos los paquetes en la carpeta `src`
    package_dir={'': 'src'},  # Define el directorio base para los paquetes
    include_package_data=True,  # Incluye otros archivos en el paquete
    install_requires=[
        'pandas>=2.2.2',
        'numpy>=2.1.0',
        'matplotlib>=3.7.2',
        'seaborn>=0.12.2',
        'pyodbc>=4.0.35'
    ],  # Lista de dependencias necesarias
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Licencia del proyecto
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # Versión mínima de Python requerida
    entry_points={
        'console_scripts': [
            'run_analysis=src.main:main',  # Ejemplo de un comando de consola personalizado (si aplica)
        ],
    },
)

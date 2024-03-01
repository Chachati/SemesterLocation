import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = 'BASE PARA UBICACIÓN SEMESTRAL REAL.xlsx'
planesInformatica = [
    {'20141': [0,0,18,38,58,78,95,112,130,148,164]},
    {'20152': [0,0,16,34,52,70,87,105,122,140,157,175]}
]

# Read the Excel file into a pandas DataFrame
data = pd.read_excel(excel_file)
ciclos= [0,'2019-1','2019-2','2020-1','2020-2','2021-1','2021-2','2022-1','2022-2','2023-1','2023-2','2024-1','2024-2','2025-1','2025-2']
# Define the function to check the program
def programa(df):
    totalCreditosperfectos = 0
    for indice, fila in df.iterrows():
        print((fila["CICLO DE ADMISION"]))
        semestre = int(ciclos.index('2024-1')) - (ciclos.index(fila["CICLO DE ADMISION"])) + 1
        print('semestre calculado por ciclo de entrada = ',semestre)
        plan = str(fila["PLAN DE ESTUDIOS"])
        print('plan de estudios: ', plan)
        for diccionario in planesInformatica:
            if plan in diccionario:  # Verifica si el plan de estudios está presente en el diccionario actual
                totalCreditosperfectos = diccionario[plan][semestre]
                print('Total de creditos suponiendo el ciclo de entrada = ' , totalCreditosperfectos)
                break  # Termina el bucle una vez que se encuentra el plan de estudios
        else:
            print(f"No se encontraron créditos para el plan de estudios '{plan}'")

programa(data)

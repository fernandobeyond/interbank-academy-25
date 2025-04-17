import pandas as pd

data = "data.csv"

def ReporteTransacciones(ruta):
    data = pd.read_csv(ruta)

    if not {'id', 'tipo', 'monto'}.issubset(data.columns):
        print("No es un formato de tabla válido, ingresar el formato correcto.")
        return
    
    # Cálculo del balance del estado de cuenta comparando el Crédito Total y Débito Total
    credTotal = data[data['tipo'] == 'Crédito']['monto'].sum()       # Cantidad total de consumo hechas por crédito
    debTotal = data[data['tipo'] == 'Débito']['monto'].sum()        # Cantidad total de consumo hechas por debito
    balance = credTotal - debTotal


    # Obtención de la transacción mayor realizada
    transMayor = data.loc[data['monto'].idxmax()]                   # Determina el monto mas alto de todo el dataframe
    id_mayor, monto_mayor = transMayor['id'], transMayor['monto']   # Extrae el ID y Monto de la transMayor              

    # Conteo de la cantidad de veces que se hizo algun tipo de transacción
    conteo = data['tipo'].value_counts()                                        # Realiza el conteo de cada item tipo
    numCredito, numDebito = conteo.get('Crédito', 0), conteo.get('Débito', 0)   # Extrae el valor cantidad de cada tipo

    # Printeo final
    print("Reporte de Transacciones")
    print(50*"-")
    print(f"Balance Final: {round(balance,2)}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {monto_mayor}")
    print(f"Conteo de Transacciones: Crédito: {numCredito} Débito: {numDebito}")

# Llama a la función que determina lo solicitado en la Data
ReporteTransacciones(data)
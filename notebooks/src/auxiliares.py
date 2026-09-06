import pandas as pd

def dataframe_coeficientes(coefs, colunas):
    # transforma em vetor 1D
    coefs = coefs.ravel()
    return pd.DataFrame(
        data=coefs, 
        index=colunas, 
        columns=["coeficiente"]
    ).sort_values(by="coeficiente")

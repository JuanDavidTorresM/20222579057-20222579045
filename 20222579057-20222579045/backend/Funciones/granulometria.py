import pandas as pd

malla = [
    "1 1/2 in",
    "1 in",
    "3/4 in",
    "3/8 in",
    "No 4",
    "No 10",
    "No 20",
    "No 40",
    "No 60",
    "No 100",
    "No 200",
    "fondo",
]

abertura = [
    37.5,
    25,
    19,
    9.5,
    4.75,
    2,
    0.85,
    0.425,
    0.25,
    0.15,
    0.075,
    0,
]

retenido = [
    0,
    0,
    0,
    0,
    5,
    5,
    70,
    70,
    70,
    270,
    10,
    35,
]

granulometria = pd.DataFrame({
    "malla": malla,
    "abertura": abertura,
    "retenido": retenido,
})

granulometria["retenido_acumulado"] = granulometria["retenido"].cumsum()

granulometria["pasa_g"] = granulometria["retenido_acumulado"].iloc[-1] - granulometria["retenido_acumulado"]

granulometria["porcentaje_pasa"] = (granulometria["pasa_g"] / granulometria["retenido_acumulado"].loc[11] * 100).round(3)


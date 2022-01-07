import utils
import pandas as pd

file = "file_download.pdf"

params_create_tables = [
    {
        "table30": {"pages": "114", "areas": (295.625, 137.138, 376.689, 320.088)},
        "table31": {"pages": "115", "areas": (143.167, 131.932, 746.308, 468.085)},
        "table31_1": {"pages": "116", "areas": (97.801, 137.138, 747.795, 500.064)},
        "table31_2": {"pages": "117", "areas": (98.545, 136.395, 741.102, 500.808)},
        "table31_3": {"pages": "118", "areas": (97.058, 137.138, 748.539, 501.551)},
        "table31_4": {"pages": "119", "areas": (97.801, 137.138, 741.845, 501.551)},
        "table31_5": {"pages": "120", "areas": (97.058, 136.395, 316.449, 500.808)},
        "table32": {"pages": "120", "areas": (457.008, 132.676, 512.786, 265.055)},
    }
]

# extraindo tabelas do pdf
table30 = [
    utils.extract_table(file, params["table30"]["pages"], params["table30"]["areas"])
    for params in params_create_tables
]
table31 = [
    utils.extract_table(file, params["table31"]["pages"], params["table31"]["areas"])
    for params in params_create_tables
]
table31_1 = [
    utils.extract_table(
        file, params["table31_1"]["pages"], params["table31_1"]["areas"]
    )
    for params in params_create_tables
]
table31_2 = [
    utils.extract_table(
        file, params["table31_2"]["pages"], params["table31_2"]["areas"]
    )
    for params in params_create_tables
]
table31_3 = [
    utils.extract_table(
        file, params["table31_3"]["pages"], params["table31_3"]["areas"]
    )
    for params in params_create_tables
]
table31_4 = [
    utils.extract_table(
        file, params["table31_4"]["pages"], params["table31_4"]["areas"]
    )
    for params in params_create_tables
]
table31_5 = [
    utils.extract_table(
        file, params["table31_5"]["pages"], params["table31_5"]["areas"]
    )
    for params in params_create_tables
]
table32 = [
    utils.extract_table(file, params["table32"]["pages"], params["table32"]["areas"])
    for params in params_create_tables
]

table31, table31_1, table31_2, table31_3, table31_4, table31_5 = (
    table31[0][0],
    table31_1[0][0],
    table31_2[0][0],
    table31_3[0][0],
    table31_4[0][0],
    table31_5[0][0],
)

# corrigindo a coluna Descrição da categoria da primeira tabela do quadro 31
table31 = table31.drop(columns=["Descrição da categoria"]).rename(
    columns={"Unnamed: 0": "Descrição da categoria"}
)

# # adicionando header as tabelas do quadro 31 para concatenalas corretamente
table31_1.columns = ["Código", "Descrição da categoria"]
table31_2.columns = ["Código", "Descrição da categoria"]
table31_3.columns = ["Código", "Descrição da categoria"]
table31_4.columns = ["Código", "Descrição da categoria"]
table31_5.columns = ["Código", "Descrição da categoria"]

aux = [
    table31,
    table31_2,
    table31_3,
    table31_4,
    table31_2,
    table31_5
]

# todas as tabelas
table30 = table30[0][0]
table31 = pd.concat(aux, axis=0, ignore_index=True, join="inner")
table32 = table32[0][0]

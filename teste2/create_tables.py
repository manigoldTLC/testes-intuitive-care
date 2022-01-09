import utils
import pandas as pd

file = "file_download.pdf"

params_create_tables = [
    {"pages": "114", "areas": (295.625, 137.138, 376.689, 320.088)},
    {"pages": "115", "areas": (143.167, 131.932, 746.308, 468.085)},
    {"pages": "116", "areas": (97.801, 137.138, 747.795, 500.064)},
    {"pages": "117", "areas": (98.545, 136.395, 741.102, 500.808)},
    {"pages": "118", "areas": (97.058, 137.138, 748.539, 501.551)},
    {"pages": "119", "areas": (97.801, 137.138, 741.845, 501.551)},
    {"pages": "120", "areas": (97.058, 136.395, 316.449, 500.808)},
    {"pages": "120", "areas": (457.008, 132.676, 512.786, 265.055)},
]

# extraindo tabelas do pdf
tables_list = []
for params in params_create_tables:
    x, y = params.values()
    tables = utils.extract_table(file, x, y)
    tables_list.append(tables[0])

# separando as tabelas e lhes atribuindo a variáveis
table30, tables31, table32 = tables_list[0], tables_list[1:7], tables_list[-1]

# corrigindo header usando apenas a primeira tabela que compõe a tabela31
t1 = (
    tables31[0]
    .drop(columns=["Descrição da categoria"])
    .rename(columns={"Unnamed: 0": "Descrição da categoria"})
)

# adicionando header para as outras tabelas para concatenar corretamente
aux = []
for table in tables31[1:]:
    table.columns = ["Código", "Descrição da categoria"]
    aux.append(table)

aux.insert(0, t1)

table31 = pd.concat(aux, axis=0, ignore_index=True, join="inner")

# convertendo as tabelas para csv e em seguida criando um arquivo zip com os csvs
tables = [table30, table31, table32]
for index, table in enumerate(tables):
    utils.convert_to_csv(table, f"quadro3{index}")

utils.create_zip("quadro30", "quadro31", "quadro32")

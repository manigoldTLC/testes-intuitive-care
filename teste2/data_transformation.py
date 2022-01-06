import create_tables
from utils import convert_to_csv
from utils import create_zip


table30 = create_tables.table30
table31 = create_tables.table31
table32 = create_tables.table32

# convertendo tabelas para csv
try:
    convert_to_csv(table30, "quadro_30")
    convert_to_csv(table31, "quadro_31")
    convert_to_csv(table32, "quadro_32")

# criando arquivo zip
finally:
    create_zip("quadro_30", "quadro_31", "quadro_32")
    print("Concluído")

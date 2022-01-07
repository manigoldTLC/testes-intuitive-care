import psycopg2
from utils import sql_query
from sql_querys import select1, select2, select3, select4
from tabulate import tabulate


conn = psycopg2.connect(
    database="insira o banco de dados aqui",
    user="insira o usuario aqui",
    password="insira a senha aqui",
    host="insira o host aqui",
    port="insira a porta aqui",
)

conn.autocommit = True
cursor = conn.cursor()

table_names = ["table_2019", "table_2020"]

for table_name in table_names:
    command1 = f"""
            CREATE TABLE {table_name}(
                data                varchar,
                reg_ans             int,
                cd_conta_contabil   int,
                descricao           text,
                vl_saldo_final      float
            )
    """
    cursor.execute(command1)

    command2 = f"""
            alter table {table_name}
                alter data type date using(data::date);
    """
    cursor.execute(command2)

first_consult = sql_query(cursor, select1)
second_consult = sql_query(cursor, select2)
third_consult = sql_query(cursor, select3)
fourth_consult = sql_query(cursor, select4)

print(
    f"10 operadoras que mais tiveram despesas no último trimestre de 2019\n{tabulate(first_consult)}\n"
)
print(
    f"10 operadoras que mais tiveram despesas no último trimestre de 2020\n{tabulate(second_consult)}\n"
)
print(
    f"10 operadoras que mais tiveram despesas no ano de 2019\n{tabulate(third_consult)}\n"
)
print(
    f"10 operadoras que mais tiveram despesas no ano de 2020\n{tabulate(fourth_consult)}\n"
)

conn.close()

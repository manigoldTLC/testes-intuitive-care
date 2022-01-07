select1 = """
        select * from table_2019
        where descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        and data >= '2019-10-01' and data < '2019-12-31'
        and vl_saldo_final < 0
        order by vl_saldo_final asc
        limit 10;
"""

select2 = """
        select * from table_2020
        where descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        and data >= '2020-10-01' and data < '2020-12-31'
        and vl_saldo_final < 0
        order by vl_saldo_final asc
        limit 10;
"""

select3 = """
        select * from table_2019
        where descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        and vl_saldo_final < 0
        order by vl_saldo_final asc
        limit 10;
"""

select4 = """
        select * from table_2020
        where descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        and vl_saldo_final < 0
        order by vl_saldo_final asc
        limit 10;
"""

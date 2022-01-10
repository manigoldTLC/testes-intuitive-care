-- criando tabela de 2019

CREATE TABLE TABLE_2019 (DATA varchar, REG_ANS int, CD_CONTA_CONTABIL int, DESCRICAO text, VL_SALDO_FINAL float);

-- criando tabela de 2020

CREATE TABLE TABLE_2020 (DATA varchar, REG_ANS int, CD_CONTA_CONTABIL int, DESCRICAO text, VL_SALDO_FINAL float);

-- alterando o tipo da coluna data na tabela de 2019 para date

ALTER TABLE TABLE_2019
ALTER DATA TYPE date USING(DATA :: date);

-- alterando o tipo da coluna data na tabela de 2020 para date

ALTER TABLE TABLE_2020
ALTER DATA TYPE date USING(DATA :: date);

-- Os dois comandos a seguir, deverá ser feito no SQL Shell (psql),
-- esses comandos irão salvar o conteúdo do arquivo csv 
-- presente em full_tables/full_table_{ano} nas tabelas criadas no postgresql com os comandos create acima.
-- O caminho até full_tables/full_table_{ano} deve ser adicionado corretamente.

\copy table_2019 from 'inserir_o_caminho_aqui/full_tables/full_table_2019.csv' using delimiters ',' encoding 'utf-8' csv header;
\copy table_2020 from 'inserir_o_caminho_aqui/full_tables/full_table_2020.csv' using delimiters ',' encoding 'utf-8' csv header;
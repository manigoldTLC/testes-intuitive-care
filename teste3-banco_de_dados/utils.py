import pandas as pd


def create_dataframe(files: list) -> list:
    """
    Transforma arquivos csv em dataframe.

    Args:
        files: Lista contendo os arquivos csv.

    Returns:
        Retorna uma lista de dataframes.
    """
    print("Criando dataframe...")
    return [
        pd.read_csv(file, encoding="windows-1252", engine="python", delimiter=";")
        for file in files
    ]


def tranform_dataframe(data_files: list) -> list:
    """
    Fazer algumas alterações em dataframes, como: nomear colunas e transformar algumas
    colunas para o tipo numérico.

    Args:
        data_files: Lista contendo os arquivos a serem transformados.

    Returns:
        Retorna uma lista de dataframes com algumas alterações.
    """
    print("Transformando dataframe...")

    list_clean_dataframes = []
    for data_file in data_files:

        data_file = data_file
        data_file.columns = [
            "data",
            "reg_ans",
            "cd_conta_contabil",
            "descricao",
            "vl_saldo_final",
        ]

        data_file = data_file.replace({",": "."}, regex=True)

        data_file[["reg_ans", "cd_conta_contabil", "vl_saldo_final"]] = data_file[
            ["reg_ans", "cd_conta_contabil", "vl_saldo_final"]
        ].apply(pd.to_numeric)

        list_clean_dataframes.append(data_file)

    return list_clean_dataframes


def convert_to_csv(l: list, name: str) -> None:
    """
    Transformar tabela pandas em um arquivo csv.

    Args:
        l: Lista contendo as tabelas a serem transformadas.
        name: string para nomear o arquivo csv gerado.

    Returns:
        Função sem retorno.
    """
    print("Convertendo dataframe para csv...")
    l.to_csv(f"full_tables/{name}.csv", index=False, encoding="utf-8")

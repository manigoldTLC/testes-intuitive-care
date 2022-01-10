import tabula
from zipfile import ZipFile


def extract_table(file: str, pages: str, area: tuple) -> list:
    """
    Extrair tabela de um documento pdf.

    Args:
        file: String com o caminho do arquivo pdf.
        pages: String com a página do pdf que contém uma tabela.
        area: Tupla contendo 'localização' da tabela.

    Returns: 
        Retorna uma lista contendo um objeto pandas.
    """
    print("Gerando tabela, aguarde...")
    return tabula.read_pdf(file, stream=True, pages=pages, area=area)


def convert_to_csv(l: list, name: str) -> None:
    """
    Transformar tabela pandas em um arquivo csv.

    Args:
        l: Lista contendo as tabelas a serem transformadas.
        name: String para nomear o arquivo csv gerado.

    Returns: 
        Função sem retorno.
    """
    print("Convertendo tabelas para csv...")
    l.to_csv(f"{name}.csv", index=False)


def create_zip(file1: str, file2: str, file3: str) -> None:
    """
    Gerar um arquivo zip contendo arquivos.

    Args:
        file1: Nome ou caminho do arquivo a ser zipado.
        file2: Nome ou caminho do arquivo a ser zipado.
        file3: Nome ou caminho do arquivo a ser zipado.

    Returns: 
        Função sem retorno.
    """
    print("Criando arquivo zip...")
    with ZipFile("Teste_Gabriel_Cardoso.zip", "w") as zip:
        zip.write(f"{file1}.csv")
        zip.write(f"{file2}.csv")
        zip.write(f"{file3}.csv")

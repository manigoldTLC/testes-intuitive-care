import tabula
from zipfile import *


def extract_table(file: str, pages: str, area: tuple) -> list:
    print("Gerando tabela, aguarde...")
    return tabula.read_pdf(file, stream=True, pages=pages, area=area)


def convert_to_csv(l: list, name: str) -> None:
    l[0].to_csv(f"{name}.csv", index=False)


def create_zip(file1: str, file2: str, file3: str) -> None:
    with ZipFile("Teste_Gabriel_Cardoso.zip", "w") as zip:
        zip.write(f"{file1}.csv")
        zip.write(f"{file2}.csv")
        zip.write(f"{file3}.csv")

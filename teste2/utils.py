import tabula


def extract_table(file: str, pages: str, area: tuple) -> list:
    print("Gerando tabela, aguarde...")
    return tabula.read_pdf(file, stream=True, pages=pages, area=area)


def convert_to_csv(l: list, name: str) -> None:
    l[0].to_csv(f"{name}.csv", index=False)
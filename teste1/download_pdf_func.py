from urllib.request import urlopen


def download_pdf(url: str) -> None:
    response = urlopen(url)
    with open("file_download.pdf", "wb") as file:
        file.write(response.read())
        print("\n\nDowload feito com sucesso!")

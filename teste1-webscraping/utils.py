from urllib.request import urlopen


def download_pdf(url: str) -> None:
    """
    Transformar em pdf o conteúdo vindo de uma url.

    Args:
        url: String com uma url contendo pdf.
        
    Returns: 
        Função sem retorno.
    """
    response = urlopen(url)
    with open("file_download.pdf", "wb") as file:
        file.write(response.read())
        print("\n\nDowload feito com sucesso!")

print(download_pdf.__doc__)
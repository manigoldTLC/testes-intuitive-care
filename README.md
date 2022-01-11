# Testes para o processo seletivo Intuitive Care

## Algumas considerações:
* Para o teste 3 ter um funcionamento correto, é necessário baixar e extrair na pasta relativa ao ano, ex.: na pasta 2019 os arquivos 1T2019.csv, ... , 4T2019.csv referentes ao ano de 2019 presentes no link
http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/ 

  * Para carregar o conteúdo dos arquivos csv gerados, na pasta full_tables, é necessário rodar os comandos encontrados no final do arquivo scripts_create_db.sql passando corretamente o caminho do arquivo, como no exemplo lá presente.
  * Todos os comandos, exceto os descritos acima, devem ser utilizados no pgAdmin 4.

* Pode ser que os testes 1 e 2 apresente alguma demora, mas nada anormal, ambos os testes funcionando corretamente.

* Estou importando o chromedriver_binary no teste 1, para utilizar o Chrome como driver, obs.: o chromedriver_binary usa sempre a versão mais recente do Chrome, caso haja necessidade, basta adicionar o chromedriver.exe ao path.

## Mais
* Versão do Python utilizada: Python 3.8.5
* Versão do PostgreSQL utilizada: 12.9
* Provedor de formatação Python: black

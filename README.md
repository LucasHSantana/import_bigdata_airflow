# Import Big Data Airflow

## Projeto
O projeto tem como finalidade demonstrar a utilização e criação de containers docker utilizando docker-compose e a utilização da ferramenta Airflow para inserir grande quantidade de dados num banco de dados postgreSQL.

Serão baixados vários arquivos csv com mais de 71 milhões de linhas e realizado inserção no banco de dados, criando tabelas dinamicamente de acordo com os arquivos baixados.

> **Note**
> Esta operação pode levar alguns minutos dependendo do hardware.

## Tecnologias utilizadas
- [Python 3.8](https://www.python.org/)
- [Airflow](https://airflow.apache.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [pgAdmin](https://www.pgadmin.org/)

## Instalação
### Docker
Seguir as instruções da documentação de acordo com o sistema operacional utilizado. (Recomendado instalar o docker desktop para facilitar a utilização)
* https://docs.docker.com/engine/install/

> **Note**
> No caso de instalação no windows, pode ser necessário configurar o wsl. Se este for o caso, siga as instruções da documentação: https://docs.docker.com/desktop/windows/wsl/ 

## Utilização
### **Docker**
É necessário que a engine do docker esteja em execução, execute o docker desktop caso necessário.

### **Execução do projeto**
Abra o terminal na pasta raíz do projeto e digite:
>  `docker-compose up`

### **Verificar a execução das tasks no airflow**
Abra o navegador e digite:
> `localhost:8080`

### **Login**
- Usuário: `airflow`
- Senha: `airflow`

Na aba dags procure pela dag `sfbike_data`, clique sobre ela, na página aberta, ao lado do nome da DAG, marque o switch como ativado.

### **Verificar inserção dos dados no banco de dados**
> **Note**
> Os dados são gravados de uma única vez no banco de dados, por isso podem demorar alguns minutos para aparecer alguma informação na tabela.

Abra o navegador e digite:
> `localhost:16543`

### **Login**
- Usuário: `postgres@gmail.com`
- Senha: `postgres`

### **Criar novo server**
1. **Aba Geral**
    - Name: Insira qualquer nome que desejar
2. **Aba Connection**
    - Host: `postgis`
    - Port: `5432`
    - Maintenance Database: `postgres`
    - Username: `postgres`
    - Password: `postgres`

- Salvar o server
- Conectar no banco de dados _sfbike_
- Consultar a tabela _status_

---

- *** Conteúdo destinado ao estudo do Python e utilização do docker
- *** Created By: **Lucas Henrique Santana**
- *** LinkedIn: https://www.linkedin.com/in/lucas-hsantana/

import os
from datetime import datetime, timedelta, date
import requests
import shutil
import logging

from airflow import DAG

from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data_files')
DAG_DIR = os.path.join(BASE_DIR, 'dags')
CONFIG_DIR = os.path.join(DAG_DIR, 'data_configs')

URL = 'https://drive.google.com/u/1/uc?id=1fQ_PPxGCN5nFyHa-nwHjhC_hgz1TO8SR&export=download&confirm=t'

#Cria uma pasta com a data corrente, para os arquivos
def create_folder():    
    path = os.path.join(DATA_DIR, str(date.today()))

    if not os.path.exists(path):
        os.mkdir(path)

    return path

with DAG(
    'sfbike_data',
    default_args={
        'depends_on_past': False,
        'email': ['lucas.hesantana16@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)        
    },
    description='Dag utilizada para extrair dados de utilização da SF Bay Area Bike Share e inseri-los no Postgres',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 10, 25),
    catchup=False,
    tags=['Estudo', 'Extracao', 'sfbike'],
) as dag:

    #Dummy operators para separar as etapas
    start = DummyOperator(task_id='start')
    extraction_done = DummyOperator(task_id='extraction_done')
    end = DummyOperator(task_id='end')

    @task(task_id='extract_files')
    # Realiza o download do dataset (.zip) e extrai o mesmo na pasta de dados
    def extract(url, **kwargs):
        response = requests.get(url) # Faz o download    

        path = create_folder()
        file = os.path.join(path, 'archive.zip')

        with open(file, 'wb') as f:
            f.write(response.content) # Grava o arquivo .zip    

        shutil.unpack_archive(file, path) # Extrai os arquivos de dentro do .zip

        os.remove(os.path.join(path, 'archive.zip'))

        logging.info('Files extracted successfully')


    extract_files = extract(URL)

    start >> extract_files >> extraction_done
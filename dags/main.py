# Aqui tentamos rodar um Airflow apenas com o 'poetry add apache-airflow', mas como esperado isso não é possivel.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello World")

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    
          
    task1 = PythonOperator(
            task_id="hello_world",
            python_callable=helloWorld)
    

# Esse código tem como objetivo nos mostrar que com o 'poetry add apache-airflow' apenas, não consiguimos utilizar o Airflow por N motivos.
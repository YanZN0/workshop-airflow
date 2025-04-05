# O Professor ensina 3 maneiras de criar uma DAG. Essa é a segunda sendo com uma instância (variável ), a nossa class DAG está sendo armazenada em uma instância e no final sendo executada por um Operador.

import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id="segunda_dag",
    start_date=datetime.datetime(2025, 4, 4),
    schedule="@daily",
    catchup=False, # Adiciona uma linha
)
EmptyOperator(task_id="tarefa", dag=minha_dag)
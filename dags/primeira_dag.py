# O Professor ensina 3 maneiras de criar uma DAG. Essa é a primeira sendo com um with, com esse with abrimos e fechamos um processo automaticamente, esse processo sendo a class DAG.

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
dag_id="meu_nome_de_dag",
start_date=datetime.datetime(2025, 4, 4),
schedule="@daily",
catchup=False
):
    EmptyOperator(task_id="tarefa")
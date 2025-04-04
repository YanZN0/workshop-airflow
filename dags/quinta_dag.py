# O Professor ensina 3 maneiras de criar uma DAG. Essa é a terceira forma sendo com Decoradores.

from time import sleep
from airflow.decorators import dag,task
from datetime import datetime

@dag(
        dag_id="primeira_dag",
        description="ETL MUITO complexa",
        schedule="* * * * *",       # Agendamento das tarefas, * * * * * significa 1 minuto.
        start_date=datetime(2025, 4, 4),        # Quando irá iniciar.
        catchup=False,      # Essa função funciona como um backfill, caso True, ela vai executar todos os dias passados.
)
def quinta_pipeline_atividades():      # Chamamos nossas atividades no começo, e não no final...

    @task   # Transforma essa função em uma task da DAG
    def primeira_atividade():
        print("Minha primeira atividade")
        sleep(2)

    @task
    def segunda_atividade():
        print("Minha segunda atividade")
        sleep(2)

    @task
    def terceira_atividade():
        print("Minha terceira atividade")
        sleep(2)

    @task
    def quarta_atividade():
        print("Pipeline Finalizada!!")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1.set_downstream([t2, t3])     # t2 e t3, dependem que a t1 seja executada para terem a sua execução, e a t4 depende que a t3 seja executada para ela ter a sua execução.
    t3.set_upstream(t4)

    # Fluxo de atividades a serem executadas. (Modificado para prática)


quinta_pipeline_atividades()
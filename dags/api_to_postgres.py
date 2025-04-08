from airflow.decorators import task, dag
from include.controller import id_aleatorio_pokemon, pegar_pokemon, add_pokemon_data
from datetime import datetime


@dag(
        dag_id="of_api_to_postgres",
        description="Da API para um banco de dados PostgreSQL",
        schedule="* * * * *", 
        start_date=datetime(2025, 4, 8),
        catchup=False
)
def api_to_postgres():
    
    @task(task_id='gerar_numero_aleatorio')
    def task_id_aleatorio_pokemon():
        return id_aleatorio_pokemon()
    
    @task(task_id='pegar_pokemon_api')
    def task_pegar_pokemon_api(numero_aleatorio):
        return pegar_pokemon(numero_aleatorio)
    
    @task(task_id='add_database')
    def task_add_pokemon_data(pokemon_data):
        return add_pokemon_data(pokemon_data)
    
    @task
    def print_sucess(response):
        print(response)
    
    t1 = task_id_aleatorio_pokemon()
    t2 = task_pegar_pokemon_api(t1)
    t3 = task_add_pokemon_data(t2)
    t4 = print_sucess(t3)

    t1 >> t2 >> t3 >> t4

api_to_postgres()
    

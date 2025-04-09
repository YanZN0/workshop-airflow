# Agora adicionando LOGs para termos informações específicas do fluxo de código, como data, hora, podendo nos ajudar em caso de erros, encontrar quando e onde houve um erro no código.

from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", retention="1 day")

def primeira_atividade():
    logger.info("Minha primeira atividade")
    sleep(2)

def segunda_atividade():
    logger.info("Minha segunda atividade")
    sleep(2)

def terceira_atividade():
    logger.info("Minha terceira atividade")
    sleep(2)

def pipeline_atividades():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline Finalizada!!")

if __name__ == "__main__":
    while True:
        pipeline_atividades()
        sleep(10)
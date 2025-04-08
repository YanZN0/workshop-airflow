from pydantic import BaseModel

class PokemonSchame(BaseModel):
    name: str       # o Pydantic que vai garantir que os dados entraram  nessa coluna sejam str.
    type: str       # o Pydantic que vai garantir que os dados entraram  nessa coluna sejam str.

    class Config:
        from_atributtes = True
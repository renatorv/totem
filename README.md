# totem

## Comandos
`source .venv/bin/activate` <br>
deactivate

# Aula 6
## Detalhes JWT, refresh token e troca de senha



# Aula 5
## Autenticação

pip install "passlib[bcrypt]"
pip install pyjwt

OAuth2 usa form data para envio de dados para login do usuário.


## Aula 4
Migrations

### Alembic
pip install alembic
ir src ==> onde está o código de fato
alembic init alembic

env.py <br>
config.set_main_option("sqlalchemy.url", "postgresql://postgres:159753@localhost:5432/postgres") <br>
target_metadata = Base.metadata <br>

Gerar Script<br>
alembic revision --autogenerate -m "Created location column on Store and removed enabled" <br>
ERRO => ModuleNotFoundError: No module named 'src' <br>
SOLUÇÃO => no arquivo env.py, no import from src.core.models import Base remover o src. <br>

### Aplicar migration
alembic upgrade head

Contornar problema do novo campo que é "Não nulo"
    op.add_column('stores', sa.Column('location', sa.String(), nullable=False, server_default=''))
    op.alter_column('stores', 'location', server_default=None)

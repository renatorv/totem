"""Created location column on Store and removed enabled

Revision ID: fb51fb9c7e56
Revises: 
Create Date: 2025-02-22 17:52:23.426677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb51fb9c7e56'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores', sa.Column('location', sa.String(), nullable=False, server_default=''))
    op.alter_column('stores', 'location', server_default=None)
    op.drop_column('stores', 'enabled')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores', sa.Column('enabled', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('stores', 'location')
    # ### end Alembic commands ###

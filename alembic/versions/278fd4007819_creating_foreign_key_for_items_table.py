"""creating foreign key for items table

Revision ID: 278fd4007819
Revises: 
Create Date: 2024-04-23 20:36:04.236920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '278fd4007819'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("items",sa.Column("category_id",sa.Integer(),nullable=False))
    op.create_foreign_key('items_category_id_fkey',
                          'items',
                          referent_table='categories',
                          local_cols=['category_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('items_category_id_fkey', 'items',)
    op.drop_column('items', 'category_id')

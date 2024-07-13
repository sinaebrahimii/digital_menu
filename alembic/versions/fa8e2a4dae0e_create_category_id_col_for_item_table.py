"""create category_id col for item table

Revision ID: fa8e2a4dae0e
Revises: 
Create Date: 2024-07-13 13:57:53.650015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa8e2a4dae0e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('items', sa.Column('category_id', sa.Integer(),nullable=False))
   op.create_foreign_key('category_items_fk', source_table="items", referent_table="categories", local_cols=['category_id'], remote_cols=['id'], ondelete="CASCADE")
    


def downgrade() -> None:
    op.drop_constraint('category_items_fk', table_name="items")
    op.drop_column('items', 'category_id')

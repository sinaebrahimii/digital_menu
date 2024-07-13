"""add constraint for option fkey

Revision ID: e2823dae28d7
Revises: fa8e2a4dae0e
Create Date: 2024-07-13 14:55:32.001404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2823dae28d7'
down_revision: Union[str, None] = 'fa8e2a4dae0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_foreign_key('options_items_fk', source_table="options", referent_table="items", local_cols=['item_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('options_items_fk', table_name="options")

"""created qty for items

Revision ID: b03d20af8a4a
Revises: eef4687d6638
Create Date: 2024-04-24 22:07:03.006593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b03d20af8a4a'
down_revision: Union[str, None] = 'eef4687d6638'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column("items",sa.Column("QTY",sa.Integer()))


def downgrade() -> None:
    op.drop_column(table_name="items",column_name='QTY')


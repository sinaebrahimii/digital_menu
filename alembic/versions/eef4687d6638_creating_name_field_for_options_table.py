"""creating name field for options table

Revision ID: eef4687d6638
Revises: 278fd4007819
Create Date: 2024-04-24 21:33:12.312295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eef4687d6638'
down_revision: Union[str, None] = '278fd4007819'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("options",sa.Column(name="name",type_=sa.String()))


def downgrade() -> None:
    pass

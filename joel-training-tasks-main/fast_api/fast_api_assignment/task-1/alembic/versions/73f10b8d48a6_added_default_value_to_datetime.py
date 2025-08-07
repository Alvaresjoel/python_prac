"""added default value to datetime

Revision ID: 73f10b8d48a6
Revises: b08c8b9c5bbf
Create Date: 2025-08-07 17:55:42.963052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73f10b8d48a6'
down_revision: Union[str, Sequence[str], None] = 'b08c8b9c5bbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

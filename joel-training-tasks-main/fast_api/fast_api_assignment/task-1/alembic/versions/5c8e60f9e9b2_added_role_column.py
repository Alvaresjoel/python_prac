"""added role column

Revision ID: 5c8e60f9e9b2
Revises: 4fcdf4ec58ed
Create Date: 2025-08-11 09:18:21.317624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c8e60f9e9b2'
down_revision: Union[str, Sequence[str], None] = '4fcdf4ec58ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

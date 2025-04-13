# mypy: ignore-errors

"""Convert colors field into JSONB

Revision ID: 303f31837bdb
Revises: c4d5420fd6be
Create Date: 2025-04-08 11:34:52.442588

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "303f31837bdb"
down_revision: Union[str, None] = "c4d5420fd6be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "cards",  # nom de la table
        "colors",  # nom de la colonne
        type_=postgresql.JSONB(),  # nouveau type
        postgresql_using="colors::jsonb",  # conversion explicite
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "cards",
        "colors",
        type_=sa.Text(),  # ou postgresql.JSON() si tu veux revenir en JSON
        postgresql_using="colors::text",
    )

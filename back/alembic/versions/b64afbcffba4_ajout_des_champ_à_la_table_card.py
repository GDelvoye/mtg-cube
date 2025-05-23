# mypy: ignore-errors
"""Ajout des champ à la table Card

Revision ID: b64afbcffba4
Revises:
Create Date: 2025-04-05 17:23:39.510565

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b64afbcffba4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("cards", sa.Column("id_full", sa.String(), nullable=False))
    op.create_unique_constraint(None, "cards", ["id_full"])
    op.create_foreign_key(None, "cube_card_association", "cards", ["card.id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "cube_card_association", type_="foreignkey")
    op.drop_constraint(None, "cards", type_="unique")
    op.drop_column("cards", "id_full")
    # ### end Alembic commands ###

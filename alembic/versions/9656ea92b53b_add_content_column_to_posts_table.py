"""add content column to posts table

Revision ID: 9656ea92b53b
Revises: 6e4278a3b671
Create Date: 2021-12-30 17:11:43.689133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9656ea92b53b'
down_revision = '6e4278a3b671'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

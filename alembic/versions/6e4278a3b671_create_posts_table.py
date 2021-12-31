"""create posts table

Revision ID: 6e4278a3b671
Revises: 
Create Date: 2021-12-30 17:02:52.347770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e4278a3b671'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass

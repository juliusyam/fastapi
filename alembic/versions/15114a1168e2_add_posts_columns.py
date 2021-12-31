"""add posts columns

Revision ID: 15114a1168e2
Revises: 810915553a99
Create Date: 2021-12-30 17:29:20.228407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15114a1168e2'
down_revision = '810915553a99'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE')
                  )
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                  )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

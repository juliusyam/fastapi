"""add foreign-key to posts table

Revision ID: 810915553a99
Revises: 98a79b7c68d6
Create Date: 2021-12-30 17:24:06.162844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '810915553a99'
down_revision = '98a79b7c68d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

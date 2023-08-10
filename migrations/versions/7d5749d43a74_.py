"""empty message

Revision ID: 7d5749d43a74
Revises: f203fd0afb89
Create Date: 2023-08-01 10:37:14.666949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5749d43a74'
down_revision = 'f203fd0afb89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('column_name', sa.String(length=100), nullable=True),
    sa.Column('another_column', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_table')
    # ### end Alembic commands ###
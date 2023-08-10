"""empty message

Revision ID: fabab8a85aea
Revises: 291888ff5605
Create Date: 2023-07-31 16:49:38.505228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fabab8a85aea'
down_revision = '291888ff5605'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('predict_result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.Column('numbers', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('predict_result')
    # ### end Alembic commands ###

"""empty message

Revision ID: 40a196e92d30
Revises: 2a3d452454bd
Create Date: 2023-07-20 09:36:16.286666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40a196e92d30'
down_revision = '2a3d452454bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('captcha', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_captcha')
    # ### end Alembic commands ###
